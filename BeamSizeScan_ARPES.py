import sys,time,os,traceback,json
from functools import partial
import pandas as pd
import serial
import serial.tools.list_ports
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize, Qt, QThread, QTimer, Signal, Slot,QUrl
from PySide6.QtGui import (QAction, QDoubleValidator, QIcon, QIntValidator,
                           QTextCursor)
from PySide6.QtWidgets import (QApplication, QFileDialog, QGridLayout,
                               QMainWindow, QMessageBox, QPushButton, QStyle,
                               QWidget)
from PySide6.QtWebSockets import QWebSocket
# import data view plot UI
from UI.Data_View_Plot import DataViewPlot
# import scan range UI
from UI.Input_scan_range import InputScanRange, calculate_scan_range
# import sub UI files
# import my message box
from UI.QtforPython_useful_tools import EmittingStr, MyMsgBox,RunQThread,AboutInfo
from UI.SQLDataViewPlot import ViewSQLiteData
# import data form to save dict data
from toolbox.Dict_DataFrame_Sqlite import (dict_to_csv, dict_to_excel,
                                             dict_to_json, dict_to_SQLTable)
# import my own matplotlib InitialPlot
from toolbox.My_Matplotlib_PySide6 import (InitialPlot, MonitorPlot, Myplot,NavigationToolbar)
  
# import main UI
from UI.UI_BeamSpotSizePlot import Ui_MainWindow
# import my tool functions for usage
from toolbox.Tools_functions import (createPath, deco_count_time,
                                       get_datetime, log_exception,
                                       log_exceptions, my_logger, to_log)
# stylesheets for use
from toolbox.QtStylesheets import (CSS_btn_on,CSS_btn_off,CSS_btn_stay,CSS_btn_shining,CSS_linE_done)
# import read thread for pAmeter 6514
from Architect.Keithley_pA6514_driver_R232 import Keithley6514Com, get_COM_port
# motion motor websocket driver
from Architect.MotionMotor_websocket_driver import MotionMotorWsThread
# for data save 
file_path=os.getcwd()
# save path info
save_path = os.path.join(file_path, 'save_data')
createPath(save_path)
# sqlite database path
SQLiteDB_path=save_path
MT_save_path = os.path.join(file_path, 'MT_data')
createPath(MT_save_path)
log_path = os.path.join(file_path, 'log_info')
createPath(log_path)

# logger
log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Limin')

"""UI application for Motor connection with websockets
For Motor motion control and pAmeter current read
Plot I_VS_axisPosition

Fermi Montion Manipulator 5/6 axis
axis:X Y Z R1 R2 R3
websocket channel: localhost:6341

DataFormat:
{'Position': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'MoveFlag': [False, False, False, False, False, False], 
            'MasterID': 'ED5840FE-CAA9-4DDC-AD38-B2B4164EF7BC'}

"""
# **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
class BeamSpotScanControl(QMainWindow,Ui_MainWindow):
    """BeamSpotSize scan program for Motor Motion control using websocket
        ## BL09U_ARPES
        Fermi Montion Manipulator 5/6 axis
        axis:X Y Z R1 R2 R3
        websocket channel: localhost:6341
    """
    scan_info_sig = Signal(dict)
    scan_start_sig = Signal(list)
    def __init__(self, parent=None):
        super(BeamSpotScanControl,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("ARPES@09U BeamSpot Size Scan ")
        self.port=6341
        self.run_flag=False
        self.connect_status_flag=False  
        self.data_num=0
        # initial parameter
        self.ini_pAmeter__()
        self.ini_websocket()
        self.ini_axis_info()
        self.__init_plot__()
        #self.ini_keithley6514_curr()
        self.ini_menu()
        self.__init__Icons()
        self.__ini_output()
        self.ini_MotionMotor_plot__()

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    MenuBar part
    """
    @log_exceptions(log_func=logger.error)
    def ini_menu(self):
        """
        for menuBar
        :return:
        """
        style = QApplication.style()
        # open data file
        OpenDATA = QAction('open data(&O)...', self)
        OpenDATA.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        OpenDATA.setShortcut(Qt.CTRL + Qt.Key_O)
        OpenDATA.triggered.connect(self.open_datafile)
        self.menuMenu.addAction(OpenDATA)
        # save data
        SaveDATA = QAction('save data(&S)...', self)
        SaveDATA.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        SaveDATA.setShortcut(Qt.CTRL + Qt.Key_S)
        SaveDATA.triggered.connect(self.save_all_data)
        self.menuMenu.addAction(SaveDATA)
        # show View data in analysis menuBar
        self.actionViewData.triggered.connect(self.show_full_data)
        self.actionDatabase.triggered.connect(self.view_sql_data)
        self.actionAbout.triggered.connect(self.show_about_info)
        # for user name
        self.username="BL09U"
        self.UserName_input.returnPressed.connect(self.set_username)
        self.__init__Icons()

    @log_exceptions(log_func=logger.error)
    def __init__Icons(self):
        """Initial all icons in the menuBar"""
        #icon_path=os.path.join(os.getcwd(),'icons')
        icon_path=os.path.realpath('icons')
        print(f'icon_path: %s' % icon_path)
        data_icon=QIcon(os.path.join(icon_path, 'databricks.svg'))
        database_icon=QIcon(os.path.join(icon_path, 'datacamp.svg'))
        motion_motor_icon=QIcon(os.path.join(icon_path, 'pkgsrc.svg'))
        pAmeter_icon=QIcon(os.path.join(icon_path, 'avast.svg'))
        About_icon=QIcon(os.path.join(icon_path, 'authy.svg'))
        self.actionViewData.setIcon(data_icon)
        self.actionDatabase.setIcon(database_icon)
        self.actionMotionMotor.setIcon(motion_motor_icon)
        self.actionpAmeter.setIcon(pAmeter_icon)
        self.actionAbout.setIcon(About_icon)
        Eline_icon=QIcon(os.path.join(icon_path, 'databricks.svg')) #databricks
        #Eline_icon=QIcon(os.path.join(icon_path, 'Eline20U_icons.svg'))
        self.setWindowIcon(Eline_icon)
        self.setIconSize(QSize(80,80))
    
    @log_exceptions(log_func=logger.error)
    def open_datafile(self):
        """
        open data file,file format should be excel(.xlsx)
        :return:
        """
        pd_data = pd.DataFrame()
        filename, filetype = QFileDialog.getOpenFileName(self, "read data file(supported filetype:xlsx/csv/json)",
                                                         './', '*.xlsx;;*.csv;;*.json')
        print(filename, filetype)
        if filename.endswith('.xlsx'):
            # add dtype={'time stamp': 'datetime64[ns]'} if have 'time stamp'
            pd_data = pd.read_excel(filename, index_col=0, na_values=["NA"], engine='openpyxl')
            # print(pd_data)
        if filename.endswith('.csv'):
            pd_data = pd.read_csv(filename, index_col=0)
        if filename.endswith('.json'):
            pd_data = pd.read_json(filename)
        # drop the row with NaN and return
        valid_pd_data = pd_data
        self.ViewopenData = DataViewPlot(valid_pd_data)
        self.ViewopenData.show_data_table(valid_pd_data)
        self.ViewopenData.show()
    
    @log_exceptions(log_func=logger.error)
    def save_all_data(self):
        """
        save all data to usr defined location and name,
        file format should be excel(.xlsx)
        :return:
        """
        print('save data')
        scan_data = self.get_full_data()
        self.usr_save_full_data(scan_data, save_path, usr_define=1)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def view_sql_data(self):
        self.ViewSqlData = ViewSQLiteData()
        self.ViewSqlData.show()


    @log_exceptions(log_func=logger.error)
    def show_full_data(self):
        self.ViewData = DataViewPlot()
        full_dict_data = self.get_full_data()
        full_pd_data = self.ViewData.dict_to_pd(full_dict_data)
        self.ViewData.show_data_table(full_pd_data)
        self.ViewData.show()

    @Slot()
    def show_about_info(self):
        self.about_info=AboutInfo()
        self.about_info.show()


    @Slot()
    def set_username(self):
        """set username
        """
        username=self.UserName_input.text()
        print("username")
        self.username=username
        print(f'current-user:{self.username}')
        self.UserName_input.setStyleSheet(CSS_linE_done)

    """
    end of MenuBar part
    """

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    @log_exceptions(log_func=logger.error)
    def __ini_output(self):
        # set a timer to show current time
        self.cur_timer = QTimer()
        self.cur_timer.timeout.connect(self.set_cur_time)
        self.cur_timer.start(100)
        # out put all to status_box
        sys.stdout = EmittingStr()
        sys.stderr = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)
        sys.stderr.textWritten.connect(self.outputWritten)
        # program start info
        start_info = f'Beam position plot program \n\tby Limin Zhou @SSRF' \
                     f'\n\t{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}'
        print(start_info)

    # out put info into the status msg box
    def outputWritten(self, text):
        cursor = self.Msg_box.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.Msg_box.setTextCursor(cursor)
        self.Msg_box.ensureCursorVisible()

    def set_cur_time(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.Now_T.setText(f'Now: {timestamp}')

    # raise info part
    def raise_warning(self, text):
        return QMessageBox.warning(self, 'ERROR', text, QMessageBox.Yes | QMessageBox.Cancel)

    def raise_info(self, text):
        return QMessageBox.information(self, 'info', text, QMessageBox.Yes | QMessageBox.Cancel)

    @log_exceptions(log_func=logger.error)
    def __init_plot__(self):        # initialize BPM figure Myplot for usage
        self.figure = InitialPlot()
        # add NavigationToolbar in the figure (widgets)
        self.fig_ntb = NavigationToolbar(self.figure, self)
        # add the figure into the Plot box
        self.gridlayout = QGridLayout(self.Plot_box)
        self.gridlayout.addWidget(self.figure)
        self.gridlayout.addWidget(self.fig_ntb)

        # initialize PD Monitor figure Myplot for pAmeter electrometer 6517B usage
        self.pAmeter_figure = MonitorPlot()

        self.fig_ntb2 = NavigationToolbar(self.pAmeter_figure, self)
        # add the figure into the Plot box
        self.gridlayout2 = QGridLayout(self.pAmeter_plot)
        self.gridlayout2.addWidget(self.pAmeter_figure)
        self.gridlayout2.addWidget(self.fig_ntb2)

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of the pA electrometer part
    """

    def ini_pAmeter__(self):
        self._MT_pA_currents = []
        self._MT_pA_delay = []
        self._pA_monitor_flag = 0
        self._pA_start_t = 0
        self._MT_save_N=0
        self._pAmeter_started=False
        self.Selected_port=''
        # list all port
        self.pAmeter_connection = False
        self.list_all_COM_port()
        self._status_timer=QTimer() # status timer
        self._status_timer.timeout.connect(self.update_pAmeter_status)
        self._shining_flag=0 # to indicate pAmeter connection
        self.serial_port=None

    def list_all_COM_port(self):
        COM_ports = get_COM_port()
        print(COM_ports)
        for COM, port in COM_ports.items():
            self.Port_cbx.addItem(f'{COM}:{port}')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Connect_pAmeter_btn_clicked(self):
        """connect pAmeter 6514

        Returns:
            _type_: _description_
        """
        print(self.Port_cbx.currentText())
        if self.Port_cbx.currentText() and not self.pAmeter_connection:
            Selected_port = self.Port_cbx.currentText().split(':')[0]
            status = "Not Open"
            connection_msg = self.Port_cbx.currentText() + ':\n' + str(status)
            try:
                self.serial_port=serial.Serial(Selected_port)
                self.pAmeter6514 = Keithley6514Com(port=self.serial_port, func='currents', points=5,full_time=100,keep_on=0)
                
                status = "OK"
                connection_msg = self.Port_cbx.currentText() + ':\n' + str(status)
                #version=self.pAmeter6514.version
                #print(f'get version: {version}')
            except Exception as e: 
                #pAmeter6514=None
                self._msgbox = MyMsgBox(title="Connection msg", text="Connect to Electrometer6514 Fail", details=connection_msg+traceback.format_exc() + str(e))
                self._msgbox.show()
            else:
                if status == "OK":
                    self._msgbox = MyMsgBox(title="Connection msg", text="Connection to Electrometer6514 Success", details=connection_msg)
                    print(f'Electrometer6514 at {Selected_port}:connected')
                    self.pAmeter6514.clear_status()
                    #self.MT_pAmeter6514.zero_check(status='OFF')
                    time.sleep(0.5)
                    self.pAmeter6514.conf_function('current',wait=500)
                    self.Connect_pAmeter_btn.setEnabled(False)
                    self.Connect_pAmeter_btn.setText("Connected")
                    self.pAmeter_connection = True
                    self.Selected_port=Selected_port
                #self.pAmeter6514.close_port()
                    self._msgbox.show()
            self._status_timer.start(1000)
    
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Port_cbx_currentIndexChanged(self):
        # choose another port
        Selected_port = self.Port_cbx.currentText().split(':')[0]
        print(Selected_port)
        if self.pAmeter_connection and not self.Connect_pAmeter_btn.isEnabled():
            # pump connected, should disconnect and enable connection button
            self.Connect_pAmeter_btn.setEnabled(True)
            self.pAmeter6514 = None
            self.pAmeter_connection = False
            self.Connect_pAmeter_btn.setText("Connect")
    @Slot()
    def update_pAmeter_status(self):
        if self.pAmeter_connection:
            self.Connect_pAmeter_btn.setText("Connected")
            if self._shining_flag==0:
                self.Connect_pAmeter_btn.setStyleSheet(CSS_btn_shining)
                self._shining_flag=1
            elif self._shining_flag==1:
                self.Connect_pAmeter_btn.setStyleSheet(CSS_btn_on)
                self._shining_flag=0
        else:
            #self.Connect_pAmeter_btn.setStyleSheet("QPushButton{background-color: rgb(98, 98, 98)}")
            self.Connect_pAmeter_btn.setText("Connect6514")

    def ini_keithley6514_curr(self,nplc=5,points=10):
        if self.pAmeter_connection:
            self.pAmeter6514.zero_check(status='OFF')
            self.pAmeter6514.conf_function('current')
            resp = self.pAmeter6514.read_data(wait=100)
            data = self.pAmeter6514.get_value(resp)
            print(f'get value:{data:.4e}A')
        else:
            self._msgbox = MyMsgBox(
                    title="Connection msg", text="Electrometer6514  initialize Fail", details='should connect Electrometer6514 ')
            self._msgbox.show()


    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Monitor_pA_clicked(self):
        if self._pA_monitor_flag == 0:
            self.clear_MT_data()
            print('Start monitoring pAmeter')
            self._pA_start_t = time.time()
            try:
                self.MT_pAmeter6514 = Keithley6514Com(port=self.serial_port, func='currents', points=5,full_time=1000,keep_on=1)
                self.MT_pAmeter6514.data_sig.connect(self.get_pAmonitor_data)
                #status = self.MT_pAmeter6514.open_port(self.Selected_port)
                # initialize keithley 6514 for current measurement
                status='OK'
                print(status)
                if  status=='OK':
                    #self.ini_keithley6514_curr(nplc=5,points=10)
                    #self.MT_pAmeter6514.clear_status()
                    #self.MT_pAmeter6514.zero_check(status='OFF')
                    #self.MT_pAmeter6514.conf_function('current',wait=100)
                    resp = self.MT_pAmeter6514.read_data(wait=100)
                    data = self.MT_pAmeter6514.get_value(resp)
                    print(f'get value:{data:.4e}A')
            except Exception as e:
                print(e)
            else:
                self._pA_monitor_flag = 1
                self._pAmeter_started=True
                print(f"status:{status}")
                self.MT_pAmeter6514.start()
        else:
            self.raise_warning('already monitoring')


    # @log_exceptions(log_func=logger.error)
    @Slot(list)
    def get_pAmonitor_data(self, resp: list):
        """
        fix
        :param resp:
        :return:
        """
        # assert resp[-1] == 'OK', self.raise_warning('error in reading pAmeter')
        if resp[-1] == 'OK' or resp[0] == 0.0:
            #self.lcd_pA.display(resp[0] * 1.0e12)
            self.lcd_display(resp[0])
            self._MT_pA_currents.append(resp[0] * 1.0e12)
            self._MT_pA_delay.append(time.time() - self._pA_start_t)
            # plot the data [value,delays]
            plot_delay = self._MT_pA_delay
            plot_read = self._MT_pA_currents
            if len(self._MT_pA_currents) > 200:
                plot_delay = self._MT_pA_delay[-200:]
                plot_read = self._MT_pA_currents[-200:]
            # plot
            self.pAmeter_figure.axes.cla()
            self.pAmeter_figure.axes.plot(plot_delay, plot_read, '-oc', markersize=1)
            self.pAmeter_figure.axes.set_title("pAmeter read", fontsize=10, color='m')
            self.pAmeter_figure.axes.set_xlabel("Delay(s)", fontsize=10, color='m')
            self.pAmeter_figure.axes.set_ylabel("currents value", fontsize=10, color='m')
            self.pAmeter_figure.draw()

    def lcd_display(self,current):
        """display current by uA, nA or pA

        Args:
            current (_type_): _description_

        Returns:
            _type_: _description_
        """
        lcd_value=-1.0
        if current*1.0e6>=1:
            # > 1uA
            lcd_value=current*1.0e6
            self.Current_label.setText('uA')
        elif current*1.0e6<1 and current*1.0e9>=1:
            # 1nA~1uA
            lcd_value=current*1.0e9
            self.Current_label.setText('nA')
        else:
            # < 1nA
            lcd_value=current*1.0e12
            self.Current_label.setText('pA')
        self.lcd_pA.display(lcd_value)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Stop_Monitor_pA_clicked(self):
        if self._pA_monitor_flag == 1:
            print('stop monitor pAmeter')
            self.MT_pAmeter6514.data_sig.disconnect(self.get_pAmonitor_data)
            self.MT_pAmeter6514.__del__()
            self._pA_monitor_flag = 0
            # save monitor data
            full_data = {'pA_delay': self._MT_pA_delay, 'current(pA)': self._MT_pA_currents
                         }
            t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
            self._MT_save_N += 1
            filename = f'MT_pA_data_{t_stamp}_{self._MT_save_N}'
            folder = time.strftime('%Y-%m-%d', time.localtime())
            save_folder = createPath(os.path.join(MT_save_path, folder))
            self.save_scan_data(full_data, save_folder, filename)
        else:
            self.raise_info('not monitoring')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Clear_Monitor_pA_clicked(self):
        self.clear_MT_data()
        if self._pA_monitor_flag == 1:
            self.MT_pAmeter6514.data_sig.disconnect(self.get_pAmonitor_data)
            self.MT_pAmeter6514.__del__()
            self._pA_monitor_flag = 0
        else:
            pass
    
    def clear_MT_data(self):
        self._MT_pA_delay = []
        self._MT_pA_currents = []
        self._pA_start_t = 0
        self.pAmeter_figure.axes.cla()
        self.pAmeter_figure.draw()
    """
    end of the pAmeter part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of Montion Motor control by websockets
    """

    def ini_websocket(self):
        """initialize parameters for Qtwebsockets 
        """
        #QWebsocket test
        self.ws_client=QWebSocket()
        self.ws_url=QUrl(f'ws://localhost:{self.port}')
         # connect slot
        self.ws_client.connected.connect(self.ws_connected)
        self.ws_client.disconnected.connect(self.ws_disconnected)
        self.ws_client.textMessageReceived[str].connect(self.ws_msgReceived)
        #for websocket motor status
        self.ws_status_timer=QTimer() # status timer
        self.ws_status_timer.timeout.connect(self.update_ws_status)
        self.ws_shining_flag=0 # for indicate websocket connection
        self.ws_status_timer.start(1000) 

    @Slot()
    def update_ws_status(self):
        if self.connect_status_flag:
            if self.ws_shining_flag==0:
                self.ConnectWS_btn.setStyleSheet(CSS_btn_shining)
                self.ws_shining_flag=1
            elif self.ws_shining_flag==1:
                self.ConnectWS_btn.setStyleSheet(CSS_btn_stay)
                self.ws_shining_flag=0
        else:
            pass

    def ini_axis_info(self):
        """initialize all axis info
        """
        #preset all motor status
        self.update_once_flag=False
        self.all_axis=["X","Y","Z","R1","R2","R3"]
        self.all_motor_status={'Position': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'MoveFlag': [False, False, False, False, False, False], 
            'MasterID': 'ED5840FE-CAA9-4DDC-AD38-B2B4164EF7BC'}
        self.axis_target_input={"X":self.X_SpinBox,"Y":self.Y_SpinBox,"Z":self.Z_SpinBox,"R1":self.R1_SpinBox,"R2":self.R2_SpinBox,"R3":self.R3_SpinBox}
        self.axis_move_btns={"X":self.X_move_btn,"Y":self.Y_move_btn,"Z":self.Z_move_btn,"R1":self.R1_move_btn,"R2":self.R2_move_btn,"R3":self.R3_move_btn}
        self.axis_lcd={"X":self.lcd_X_pos,"Y":self.lcd_Y_pos,"Z":self.lcd_Z_pos,"R1":self.lcd_R1_pos,"R2":self.lcd_R2_pos,"R3":self.lcd_R3_pos}
        for axis,move_btn in self.axis_move_btns.items():
            move_btn.clicked.connect(partial(self.move_axis_motor,axis)) 

    @Slot(str)
    def move_axis_motor(self,axis):
        """move the "axis" motor to target position

        Args:
            axis (_type_): _description_
        """
        target_pos=self.axis_target_input[axis].value()
        print(f'Move X to target pos:{target_pos}')
        axis_num=self.all_axis.index(axis)
        dest_pos=target_pos
        move_cd="MOVE"
        data="{\"Index\":%d,\"Destination\":%f}" %(axis_num,dest_pos)
        cmd_move={"command":move_cd,"data":data}
        move_msg=json.dumps(cmd_move)
        self.ws_client.sendTextMessage(move_msg)

    @log_exceptions(log_func=logger.error)
    def set_motor_position(self,axis_num:int,set_pos:float):
        """set the all_axis[axis_num] to set_pos

        Args:
            axis_num (int): all_axis=[X,Y,Z,R1,R2,R3]
            set_pos (float): target position

        Returns:
            _type_: _description_
        """
        # current pos and motor status[True,False]
        t0=time.monotonic()
        set_info="notSet"
        curr_axis_pos=self.all_motor_status['Position'][axis_num]
        new_pos=curr_axis_pos
        axis_motor_status=self.all_motor_status['MoveFlag'][axis_num]
        print(f'axis {self.all_axis[axis_num]} status:{axis_motor_status}')
        if self.connect_status_flag:
            set_flag=True
            print(f'Move X from {curr_axis_pos} to target pos:{set_pos}')
            move_cd="MOVE"
            data="{\"Index\":%d,\"Destination\":%f}" %(axis_num,set_pos)
            cmd_move={"command":move_cd,"data":data}
            move_msg=json.dumps(cmd_move)
            sendbytes=self.ws_client.sendTextMessage(move_msg)
            print(sendbytes)
            #set timeout for mortor motion
            timeout=abs(set_pos-curr_axis_pos)*0.6+10
            while set_flag and time.monotonic()-t0<timeout:
                new_pos=self.all_motor_status['Position'][axis_num]
                new_status=self.all_motor_status['MoveFlag'][axis_num]
                if abs(set_pos-new_pos)<0.1 and not new_status:
                    # motor motion has stoped
                    set_flag=False
                    set_info="done"
                else:
                    pass
            # jump out time
            used_time=time.monotonic() - t0
            print(f"set axis position done after: {used_time:.2f}s with timeout of {timeout}s\n"
                f"average time:{used_time/abs(set_pos-curr_axis_pos):0.3f}")
            #info = [new_pos, set_pos, axis_num, set_info] 
        else:
            print(f'Motionmotor not connected')
        info = [new_pos, set_pos, axis_num, set_info]
        print(info)
        return info
    
    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Clear_Save_clicked(self):
        axis_num=0
        set_pos=10
        print(f'set axis{self.all_axis[axis_num]} to {set_pos}')
        #self.set_motor_position(axis_num,set_pos)
        self.MotorSetThread=MotionMotorWsThread(axis_num,set_pos)
        self.MotorSetThread.done_sig.connect(self.motor_set_done)
        self.MotorSetThread.start()
    
    def motor_set_done(self,done_info:list):
        """_summary_
        done_info=[new_pos, set_pos, axis_num, set_info]
        Args:
            done_info (list): [new_pos, set_pos, axis_num, set_info]

        Returns:
            _type_: _description_
        """
        print(done_info)
        # axis_num=done_info[0][2]
        # print(f'set axis {self.all_axis[axis_num]} done with info {done_info}')


    @Slot()
    def ws_connected(self):
        peerAddress=self.ws_client.peerAddress().toString()
        peerName=self.ws_client.peerName()
        peerPort=self.ws_client.peerPort()
        print(f'connect to ws://{peerAddress}:{peerPort} successful')
    
    @Slot()
    def ws_disconnected(self):
        peerName=self.ws_client.peerName()
        peerPort=self.ws_client.peerPort()
        print(f'localport:{self.ws_client.localPort()}')
        print(f'disconnect ws://{peerName}:{peerPort} successful')

    @Slot(str)
    def ws_msgReceived(self,msg:str):
        #print(f'recevied message:\n{msg}')
        self.all_motor_status=self.extract_motor_status(msg)
        self.update_all_motors(self.all_motor_status)

    @Slot()
    def on_ConnectWS_btn_clicked(self):
        """connect the motor websocket

        """
        if not self.connect_status_flag:
            print(f"start connect to websocket://localhost:{self.port}")
            self.connect_motorws()
        else:
            # disconnect websocket
            self.disconnect_motorws()
        
    def connect_motorws(self,ip:str="127.0.0.1",port=6341):
        try:
            ws_url=QUrl(f'ws://{ip}:{port}')
            self.ws_client.open(ws_url)
        except Exception as e:
            error_info = traceback.format_exc()
            print(error_info)
        else:
            self.connect_status_flag=True  
            self.ConnectWS_btn.setText("Motor ON")
            self.ConnectWS_btn.setStyleSheet(CSS_btn_on)
            

    def disconnect_motorws(self,ip:str="127.0.0.1",port=6341):
        try:
            ws_url=QUrl(f'ws://{ip}:{port}')
            self.ws_client.close()
        except Exception as e:
            error_info = traceback.format_exc()
            print(error_info)
        else:
            self.connect_status_flag=False  
            self.ConnectWS_btn.setText("Motor OFF")
            self.ConnectWS_btn.setStyleSheet(CSS_btn_off)
               
    def extract_motor_status(self,motor_msg):
        """show motor status
        motor status:
            {'Position': [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
            'MoveFlag': [False, False, False, False, False, False], 
            'MasterID': 'ED5840FE-CAA9-4DDC-AD38-B2B4164EF7BC'}
        Args:
            motor_msg (_type_): _description_
        """
        dict_data=json.loads(motor_msg)
        motor_status={}
        if isinstance(dict_data,dict):
            motor_status['Position']=dict_data["Doubles"]
            motor_status["MoveFlag"]=dict_data["Booleans"][:6]
            motor_status["MasterID"]=dict_data["Master ID"]
        #print(motor_status)
        return motor_status
    
    def update_all_motors(self,motor_status:dict):
        """update motor position based on recived  motor_status
        motor status:
        {'Position': [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        'MoveFlag': [False, False, False, False, False, False], 
        'MasterID': 'ED5840FE-CAA9-4DDC-AD38-B2B4164EF7BC'}

        Args:
            motor_status (dict): _description_
        """
        # update each axis
        for axis_num,axis in enumerate(self.all_axis):
            new_pos=motor_status['Position'][axis_num]
            self.axis_lcd[axis].display(new_pos)
            if not self.update_once_flag:
                self.axis_target_input[axis].setValue(new_pos)
            if motor_status['MoveFlag'][axis_num]:
                #print(f'set stylesheet1')
                self.axis_move_btns[axis].setStyleSheet(CSS_btn_on)
            else:
                self.axis_move_btns[axis].setStyleSheet(CSS_btn_stay)
        self.update_once_flag=True


    """
    end of Montion Motor control by websockets
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of scan set part

    DataStructure={ch_name: self._plot_ch_list,  'current(pA)': self._plot_pAmeter_list,
    'time_stamp': self._time_stamp, 'scan set': self._scan_list}
    """
    @log_exceptions(log_func=logger.error)
    def ini_MotionMotor_plot__(self):
        #data structure
        self._plot_ch_list = []
        self._plot_pAmeter_list = []
        self._time_stamp = []
        #scan axis info
        self.scan_axis=self.all_axis.index(self.Scan_Axis_cbx.currentText())
        self.scan_axis_name=self.Scan_Axis_cbx.currentText()
        self.Scan_Axis_cbx.currentIndexChanged['int'].connect(self.set_scan_channel)
        # flag for status 1 is on , 0 is off
        self._start_plot_flag = 0
        self._scan_range_set_flag = 0
        self._scan_motor_ch_flag = 0
        self._scan_list = []
        self._scan_list_num = 0  # number of scan list
        self._scan_N = 0  # index of scan list
        self._save_file_flag = 0
        self._save_N = 0  # index for save order
        self.scan_axis_num=None
        self._scan_info=None
        
    @log_exceptions(log_func=logger.error)
    @Slot(int)
    def set_scan_channel(self, n: int):
        """
        choose the scan axis to measure current
        :return:
        """
        print(f'select scan axis:{self.all_axis[n]}')
        self.scan_axis_name=self.Scan_Axis_cbx.currentText()
        self.scan_axis=self.all_axis.index(self.Scan_Axis_cbx.currentText())
        self._scan_range_set_flag=0

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Input_scan_range_btn_clicked(self):
        """
        check which ch axis is chosen(X-Y-Z,R1-R3), get the scan range list and return
        :return: scan range list
        """
        self.scan_axis_name=self.Scan_Axis_cbx.currentText()
        print(f'choose scan Axis: {self.scan_axis_name}')
        axis_num=self.all_axis.index(self.scan_axis_name)
        scan_axis_pos=self.all_motor_status['Position'][axis_num]
        input_info = f'scan channel: {self.scan_axis_name}\nCurrent value:\n{self.scan_axis_name}:' \
                    f'{scan_axis_pos}'
        # input_info = f'Input BPM Z range:\nmin:{self._min_Z_pos}\nmax:{self._max_Z_pos}' \
        #                  f'\nstep range:{self._min_Z_step}-{self._max_Z_step}'
        self.inputRange_dialog = InputScanRange(f'{self.scan_axis_name}', input_info)
        self.inputRange_dialog.data_sig.connect(self.get_scan_range)
        self.inputRange_dialog.show()

    @Slot(list)
    def get_scan_range(self, scan_range_list: list):
        """
        get the scan range,\n
        scan range list: [scan_type,[min_E,min_E+1*step_E...max_E]] \n
        :return:
        """
        if scan_range_list[-1]:
            self._scan_info = scan_range_list
            self.raise_info(f'Next will scan {scan_range_list[0]}, scan range:\n{scan_range_list[-1]},'
                            f' total points: {len(scan_range_list[-1])}, you can start now')
            self._scan_range_set_flag = 1
            print(self._scan_info)
            logger.info(f'get scan info: {self._scan_info}')

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Start_plot_clicked(self):
        """
        check which channel to scan,choose channel by scan info[0] \n
        scan_info=[scan_type,[min_E,min_E+1*step_E...max_E]] \n
        :return:
        """
        # clear all previous scan data
        print(f'start scan process:{self._scan_info}')
        self.clear_all_data()
        print(f'start plot={self._start_plot_flag}-set scan range={self._scan_range_set_flag}')
        if self._start_plot_flag == 0 and self._scan_range_set_flag == 1 and isinstance(self._scan_info,list):
            # scan is off
            print(f'scan channel={self._scan_info[0]}')
            scan_axis_num=self.all_axis.index(self._scan_info[0])
            # scan the channel with the scan_list
            print(f"start scan, Channel:{self._scan_info[0]}, ch_num:{scan_axis_num}")
            self.scan_axis_pA(scan_axis_num,self._scan_info[-1])
        else:
            # scan is already on, can not start
            print('scan is already on, stop scan or wait!')
            self.raise_info('should set scan range first or scan is already on, stop scan or wait!')

    def set_progress_Bar(self,status:int):
        self.progressBar.setValue(status)

    """
    end of  scan set part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    start of Motor pos vs I_PD plot part
    full sequence of axisPos-pAmeter scan
    """
    @log_exceptions(log_func=logger.error)
    def scan_axis_pA(self,axis_num,range_list:list):
        """scan one channel and plot
        """
        self._start_plot_flag=1
        self._scan_motor_ch_flag=1
        if axis_num and isinstance(range_list,list):
            self.scan_axis_num=axis_num
            # set up time hint
            EP_Time = len(range_list) * 6.0
            t_done = time.time() + EP_Time
            tdone_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_done))
            self.Expect_FN_T.setText(f'finishT:{tdone_stamp}')
            self._scan_list = range_list
            self._scan_list_num = len(range_list)
            self._scan_N = 0
            self.scan_start_sig.connect(self.start_axis_pA_set)
            self.scan_start_sig.emit(['OK', self._scan_N])


    @log_exceptions(log_func=logger.error)
    @Slot(list)
    def start_axis_pA_set(self, cmd: list):
        if cmd[0] == 'OK':
            # set axis position
            #self.pmc_motor.set_pos(str(self.scan_ch_num),self._scan_list[self._scan_N])
            self.pmcsetQThread = pmcSetThread(self.pmc_motor,ch_num=self.scan_ch_num, pos=self._scan_list[self._scan_N],num=1)
            self.pmcsetQThread.done_signal.connect(self.pmc_set_done)
            self.pmcsetQThread.start()


    """
    end of Motor pos vs I_PD plot part
    """
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """close event
    """
    def closeEvent(self, event):
        if self.connect_status_flag:
            self.raise_info('Close Motor before exit!')
            event.ignore()
        else:
            close = QMessageBox.question(self,
                                                   "QUIT",
                                                   "Are you sure to exit?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BeamSpotScanControl()
    win.show()
    sys.exit(app.exec())
    
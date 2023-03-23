import socket,traceback
import time,sys,json
from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject,QUrl
from PySide6.QtWebSockets import QWebSocket,QWebSocketProtocol
from PySide6.QtWidgets import (QApplication, QFileDialog, QGridLayout,
                               QMainWindow, QMessageBox, QPushButton, QStyle,
                               QWidget)

class MotionMotorWsThread(QObject):
    """working thread for set position of motion Motors

    Args:
        QThread (_type_): _description_
    """
    done_signal = Signal(list)

    def __init__(self, axis_num:int, pos:int, num: int = 0,port=6341, wait=1000):
        super(MotionMotorWsThread,self).__init__()
        self.axis_num=axis_num
        self.set_pos=pos
        self.check_n=num
        self.set_flag=True
        self.port=port
        self.wait=wait
        self.ws_client=QWebSocket("", QWebSocketProtocol.Version13, None)
        #self.ini_websocket()

    def __del__(self):
        self.set_flag = False

    def ini_websocket(self):
        """initialize parameters for Qtwebsockets 
        """
        pass
        #self.connect_status_flag=False
        #QWebsocket test
        #self.ws_client=QWebSocket()
        #self.ws_url=QUrl(f'ws://localhost:{self.port}')
        #print(self.all_axis)
         # connect slot
        #self.ws_client.connected.connect(self.ws_connected)
        #self.ws_client.disconnected.connect(self.ws_disconnected)
        #self.ws_client.textMessageReceived[str].connect(self.ws_msgReceived)
        # store motor status
        #self.all_axis=["X","Y","Z","R1","R2","R3"]
        #self.all_motor_status={'Position': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'MoveFlag': [False, False, False, False, False, False], 
        #    'MasterID': 'ED5840FE-CAA9-4DDC-AD38-B2B4164EF7BC'}
        
        #self.connect_motorws()
        
    # def run(self):
    #     """set the all_axis[axis_num] to set_pos

    #     Args:
    #         axis_num (int): all_axis=[X,Y,Z,R1,R2,R3]
    #         set_pos (float): target position

    #     Returns:
    #         _type_: _description_
    #     """
    #     # current pos and motor status[True,False]
        
    #     t0=time.monotonic()
    #     set_info="notSet"
    #     curr_axis_pos=self.all_motor_status['Position'][self.axis_num]
    #     new_pos=curr_axis_pos
    #     axis_motor_status=self.all_motor_status['MoveFlag'][self.axis_num]
    #     print(f'axis {self.all_axis[self.axis_num]} status:{axis_motor_status}')
    #     if self.connect_status_flag:
    #         set_flag=True
    #         print(f'Move X from {curr_axis_pos} to target pos:{self.set_pos}')
    #         move_cd="MOVE"
    #         data="{\"Index\":%d,\"Destination\":%f}" %(self.axis_num,self.set_pos)
    #         cmd_move={"command":move_cd,"data":data}
    #         move_msg=json.dumps(cmd_move)
    #         sendbytes=self.ws_client.sendTextMessage(move_msg)
    #         print(sendbytes)
    #         #set timeout for mortor motion
    #         timeout=abs(self.set_pos-curr_axis_pos)*0.6+10
    #         while set_flag and time.monotonic()-t0<timeout:
    #             new_pos=self.all_motor_status['Position'][self.axis_num]
    #             new_status=self.all_motor_status['MoveFlag'][self.axis_num]
    #             if abs(self.set_pos-new_pos)<0.1 and not new_status:
    #                 # motor motion has stoped
    #                 self.msleep(200)
    #                 set_flag=False
    #                 set_info="done"
    #             else:
    #                 self.msleep(200)
    #         # jump out time
    #         used_time=time.monotonic() - t0
    #         print(f"set axis position done after: {used_time:.2f}s with timeout of {timeout}s\n"
    #             f"average time:{used_time/abs(self.set_pos-curr_axis_pos):0.3f}")
    #         #info = [new_pos, set_pos, axis_num, set_info] 
    #     else:
    #         print(f'Motionmotor not connected')
    #     info = [new_pos, self.set_pos, self.axis_num, set_info]
    #     print(info)
    #     #self.done_signal.emit(info)

    # def move_axis_motor(self,axis_num,target_pos):
    #     """move the "axis" motor to target position

    #     Args:
    #         axis (_type_): _description_
    #     """

    #     print(f'Move X to target pos:{target_pos}')
    #     dest_pos=target_pos
    #     move_cd="MOVE"
    #     data="{\"Index\":%d,\"Destination\":%f}" %(axis_num,dest_pos)
    #     cmd_move={"command":move_cd,"data":data}
    #     move_msg=json.dumps(cmd_move)
    #     self.ws_client.sendTextMessage(move_msg)

    # @Slot()
    # def ws_connected(self):
    #     peerAddress=self.ws_client.peerAddress().toString()
    #     peerName=self.ws_client.peerName()
    #     peerPort=self.ws_client.peerPort()
    #     print(f'connect to ws://{peerAddress}:{peerPort} successful')
    
    # @Slot()
    # def ws_disconnected(self):
    #     peerName=self.ws_client.peerName()
    #     peerPort=self.ws_client.peerPort()
    #     print(f'localport:{self.ws_client.localPort()}')
    #     print(f'disconnect ws://{peerName}:{peerPort} successful')

    # @Slot(str)
    # def ws_msgReceived(self,msg:str):
    #     #print(f'recevied message:\n{msg}')
    #     self.all_motor_status=self.extract_motor_status(msg)
    
    # def connect_motorws(self,ip:str="127.0.0.1",port=6341):
    #     try:
    #         ws_url=QUrl(f'ws://{ip}:{port}')
    #         self.ws_client.open(ws_url)
    #     except Exception as e:
    #         error_info = traceback.format_exc()
    #         print(error_info)
    #     else:
    #         self.connect_status_flag=True  

    # def disconnect_motorws(self,ip:str="127.0.0.1",port=6341):
    #     try:
    #         ws_url=QUrl(f'ws://{ip}:{port}')
    #         self.ws_client.close()
    #     except Exception as e:
    #         error_info = traceback.format_exc()
    #         print(error_info)
    #     else:
    #         self.connect_status_flag=False  
                       
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

    @Slot()
    def motor_set_done(self,done_info:list):
        """_summary_
        done_info=[new_pos, set_pos, axis_num, set_info]
        Args:
            done_info (list): [new_pos, set_pos, axis_num, set_info]

        Returns:
            _type_: _description_
        """
        print(done_info)


if __name__=="__main__":
    axis_num=0
    set_pos=10
    testChat=WsClient()
    #MotorSetThread=MotionMotorWsThread(axis_num,set_pos)
    #MotorSetThread.done_signal.connect(motor_set_done)
    #MotorSetThread.move_axis_motor(axis_num,set_pos)


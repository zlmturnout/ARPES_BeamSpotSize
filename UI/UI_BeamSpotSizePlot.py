# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_BeamSpotSizePlot.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)
import qrc_bg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        self.actionViewData = QAction(MainWindow)
        self.actionViewData.setObjectName(u"actionViewData")
        self.actionDatabase = QAction(MainWindow)
        self.actionDatabase.setObjectName(u"actionDatabase")
        self.actionMotionMotor = QAction(MainWindow)
        self.actionMotionMotor.setObjectName(u"actionMotionMotor")
        self.actionpAmeter = QAction(MainWindow)
        self.actionpAmeter.setObjectName(u"actionpAmeter")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Msg_box_2 = QTextBrowser(self.centralwidget)
        self.Msg_box_2.setObjectName(u"Msg_box_2")
        self.Msg_box_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Msg_box_2.sizePolicy().hasHeightForWidth())
        self.Msg_box_2.setSizePolicy(sizePolicy)
        self.Msg_box_2.setMinimumSize(QSize(360, 120))
        self.Msg_box_2.setMaximumSize(QSize(600, 120))
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(0, 170, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.Msg_box_2.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.Msg_box_2.setFont(font)
        self.Msg_box_2.setStyleSheet(u"")
        self.Msg_box_2.setFrameShape(QFrame.Panel)
        self.Msg_box_2.setFrameShadow(QFrame.Sunken)
        self.Msg_box_2.setLineWidth(1)
        self.Msg_box_2.setMidLineWidth(1)

        self.verticalLayout_2.addWidget(self.Msg_box_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.UserName_input = QLineEdit(self.centralwidget)
        self.UserName_input.setObjectName(u"UserName_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UserName_input.sizePolicy().hasHeightForWidth())
        self.UserName_input.setSizePolicy(sizePolicy1)
        self.UserName_input.setMinimumSize(QSize(120, 40))
        self.UserName_input.setMaximumSize(QSize(400, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.UserName_input.setFont(font1)
        self.UserName_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.UserName_input)

        self.ConnectWS_btn = QPushButton(self.centralwidget)
        self.ConnectWS_btn.setObjectName(u"ConnectWS_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ConnectWS_btn.sizePolicy().hasHeightForWidth())
        self.ConnectWS_btn.setSizePolicy(sizePolicy2)
        self.ConnectWS_btn.setMinimumSize(QSize(160, 40))
        self.ConnectWS_btn.setMaximumSize(QSize(250, 16777215))
        self.ConnectWS_btn.setFont(font1)
        self.ConnectWS_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);}\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);color: rgb(255, 255, 255);}")

        self.horizontalLayout.addWidget(self.ConnectWS_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Port_cbx = QComboBox(self.centralwidget)
        self.Port_cbx.setObjectName(u"Port_cbx")
        self.Port_cbx.setMinimumSize(QSize(120, 40))
        self.Port_cbx.setMaximumSize(QSize(400, 40))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.Port_cbx.setFont(font2)
        self.Port_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Port_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_2.addWidget(self.Port_cbx)

        self.Connect_pAmeter_btn = QPushButton(self.centralwidget)
        self.Connect_pAmeter_btn.setObjectName(u"Connect_pAmeter_btn")
        sizePolicy2.setHeightForWidth(self.Connect_pAmeter_btn.sizePolicy().hasHeightForWidth())
        self.Connect_pAmeter_btn.setSizePolicy(sizePolicy2)
        self.Connect_pAmeter_btn.setMinimumSize(QSize(160, 40))
        self.Connect_pAmeter_btn.setMaximumSize(QSize(250, 16777215))
        self.Connect_pAmeter_btn.setFont(font1)
        self.Connect_pAmeter_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);}\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);color: rgb(255, 255, 255);}")

        self.horizontalLayout_2.addWidget(self.Connect_pAmeter_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ARPES_label = QLabel(self.centralwidget)
        self.ARPES_label.setObjectName(u"ARPES_label")
        sizePolicy2.setHeightForWidth(self.ARPES_label.sizePolicy().hasHeightForWidth())
        self.ARPES_label.setSizePolicy(sizePolicy2)
        self.ARPES_label.setMinimumSize(QSize(327, 120))
        self.ARPES_label.setMaximumSize(QSize(327, 120))
        palette1 = QPalette()
        brush7 = QBrush(QColor(255, 106, 60, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush8)
        brush9 = QBrush(QColor(85, 170, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.ARPES_label.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.ARPES_label.setFont(font3)
        self.ARPES_label.setStyleSheet(u"background-image: url(:/icons/icons/Beamspotsize_120.png);")
        self.ARPES_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ARPES_label, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Channel_txt_1 = QLabel(self.centralwidget)
        self.Channel_txt_1.setObjectName(u"Channel_txt_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Channel_txt_1.sizePolicy().hasHeightForWidth())
        self.Channel_txt_1.setSizePolicy(sizePolicy3)
        self.Channel_txt_1.setMinimumSize(QSize(75, 40))
        self.Channel_txt_1.setMaximumSize(QSize(100, 40))
        self.Channel_txt_1.setFont(font1)
        self.Channel_txt_1.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Channel_txt_1)

        self.lcd_X_pos = QLCDNumber(self.centralwidget)
        self.lcd_X_pos.setObjectName(u"lcd_X_pos")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcd_X_pos.sizePolicy().hasHeightForWidth())
        self.lcd_X_pos.setSizePolicy(sizePolicy4)
        self.lcd_X_pos.setMinimumSize(QSize(80, 40))
        self.lcd_X_pos.setMaximumSize(QSize(150, 16777215))
        palette2 = QPalette()
        brush10 = QBrush(QColor(255, 11, 222, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.lcd_X_pos.setPalette(palette2)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.lcd_X_pos.setFont(font4)
        self.lcd_X_pos.setStyleSheet(u"\n"
"color: rgb(255, 11, 222);")
        self.lcd_X_pos.setFrameShadow(QFrame.Sunken)
        self.lcd_X_pos.setSmallDecimalPoint(False)
        self.lcd_X_pos.setDigitCount(5)
        self.lcd_X_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_3.addWidget(self.lcd_X_pos)

        self.X_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.X_SpinBox.setObjectName(u"X_SpinBox")
        self.X_SpinBox.setMinimumSize(QSize(100, 40))
        self.X_SpinBox.setMaximumSize(QSize(150, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(12)
        self.X_SpinBox.setFont(font5)
        self.X_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.X_SpinBox)

        self.X_move_btn = QPushButton(self.centralwidget)
        self.X_move_btn.setObjectName(u"X_move_btn")
        sizePolicy.setHeightForWidth(self.X_move_btn.sizePolicy().hasHeightForWidth())
        self.X_move_btn.setSizePolicy(sizePolicy)
        self.X_move_btn.setMinimumSize(QSize(100, 40))
        self.X_move_btn.setMaximumSize(QSize(150, 16777215))
        self.X_move_btn.setFont(font)
        self.X_move_btn.setStyleSheet(u"QPushButton{background-color: rgb(33, 190, 193);color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 102, 42);}\n"
"")

        self.horizontalLayout_3.addWidget(self.X_move_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Channel_txt_2 = QLabel(self.centralwidget)
        self.Channel_txt_2.setObjectName(u"Channel_txt_2")
        sizePolicy3.setHeightForWidth(self.Channel_txt_2.sizePolicy().hasHeightForWidth())
        self.Channel_txt_2.setSizePolicy(sizePolicy3)
        self.Channel_txt_2.setMinimumSize(QSize(75, 40))
        self.Channel_txt_2.setMaximumSize(QSize(100, 40))
        self.Channel_txt_2.setFont(font1)
        self.Channel_txt_2.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Channel_txt_2)

        self.lcd_Y_pos = QLCDNumber(self.centralwidget)
        self.lcd_Y_pos.setObjectName(u"lcd_Y_pos")
        sizePolicy4.setHeightForWidth(self.lcd_Y_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Y_pos.setSizePolicy(sizePolicy4)
        self.lcd_Y_pos.setMinimumSize(QSize(80, 40))
        self.lcd_Y_pos.setMaximumSize(QSize(150, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.lcd_Y_pos.setPalette(palette3)
        self.lcd_Y_pos.setFont(font4)
        self.lcd_Y_pos.setStyleSheet(u"\n"
"color: rgb(255, 11, 222);")
        self.lcd_Y_pos.setFrameShadow(QFrame.Sunken)
        self.lcd_Y_pos.setSmallDecimalPoint(False)
        self.lcd_Y_pos.setDigitCount(5)
        self.lcd_Y_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_4.addWidget(self.lcd_Y_pos)

        self.Y_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.Y_SpinBox.setObjectName(u"Y_SpinBox")
        self.Y_SpinBox.setMinimumSize(QSize(100, 40))
        self.Y_SpinBox.setMaximumSize(QSize(150, 16777215))
        self.Y_SpinBox.setFont(font5)
        self.Y_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.Y_SpinBox)

        self.Y_move_btn = QPushButton(self.centralwidget)
        self.Y_move_btn.setObjectName(u"Y_move_btn")
        sizePolicy4.setHeightForWidth(self.Y_move_btn.sizePolicy().hasHeightForWidth())
        self.Y_move_btn.setSizePolicy(sizePolicy4)
        self.Y_move_btn.setMinimumSize(QSize(100, 40))
        self.Y_move_btn.setMaximumSize(QSize(150, 16777215))
        self.Y_move_btn.setFont(font)
        self.Y_move_btn.setStyleSheet(u"QPushButton{background-color: rgb(33, 190, 193);color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 102, 42);}")

        self.horizontalLayout_4.addWidget(self.Y_move_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Channel_txt_3 = QLabel(self.centralwidget)
        self.Channel_txt_3.setObjectName(u"Channel_txt_3")
        sizePolicy3.setHeightForWidth(self.Channel_txt_3.sizePolicy().hasHeightForWidth())
        self.Channel_txt_3.setSizePolicy(sizePolicy3)
        self.Channel_txt_3.setMinimumSize(QSize(75, 40))
        self.Channel_txt_3.setMaximumSize(QSize(100, 40))
        self.Channel_txt_3.setFont(font1)
        self.Channel_txt_3.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.Channel_txt_3)

        self.lcd_Z_pos = QLCDNumber(self.centralwidget)
        self.lcd_Z_pos.setObjectName(u"lcd_Z_pos")
        sizePolicy4.setHeightForWidth(self.lcd_Z_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Z_pos.setSizePolicy(sizePolicy4)
        self.lcd_Z_pos.setMinimumSize(QSize(80, 40))
        self.lcd_Z_pos.setMaximumSize(QSize(150, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.lcd_Z_pos.setPalette(palette4)
        self.lcd_Z_pos.setFont(font4)
        self.lcd_Z_pos.setStyleSheet(u"\n"
"color: rgb(255, 11, 222);")
        self.lcd_Z_pos.setFrameShadow(QFrame.Sunken)
        self.lcd_Z_pos.setSmallDecimalPoint(False)
        self.lcd_Z_pos.setDigitCount(5)
        self.lcd_Z_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_5.addWidget(self.lcd_Z_pos)

        self.Z_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.Z_SpinBox.setObjectName(u"Z_SpinBox")
        self.Z_SpinBox.setMinimumSize(QSize(100, 40))
        self.Z_SpinBox.setMaximumSize(QSize(150, 16777215))
        self.Z_SpinBox.setFont(font5)
        self.Z_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.Z_SpinBox)

        self.Z_move_btn = QPushButton(self.centralwidget)
        self.Z_move_btn.setObjectName(u"Z_move_btn")
        sizePolicy4.setHeightForWidth(self.Z_move_btn.sizePolicy().hasHeightForWidth())
        self.Z_move_btn.setSizePolicy(sizePolicy4)
        self.Z_move_btn.setMinimumSize(QSize(100, 40))
        self.Z_move_btn.setMaximumSize(QSize(150, 16777215))
        self.Z_move_btn.setFont(font)
        self.Z_move_btn.setStyleSheet(u"QPushButton{background-color: rgb(33, 190, 193);color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 102, 42);}")

        self.horizontalLayout_5.addWidget(self.Z_move_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Channel_txt_4 = QLabel(self.centralwidget)
        self.Channel_txt_4.setObjectName(u"Channel_txt_4")
        sizePolicy3.setHeightForWidth(self.Channel_txt_4.sizePolicy().hasHeightForWidth())
        self.Channel_txt_4.setSizePolicy(sizePolicy3)
        self.Channel_txt_4.setMinimumSize(QSize(75, 30))
        self.Channel_txt_4.setMaximumSize(QSize(100, 40))
        self.Channel_txt_4.setFont(font)
        self.Channel_txt_4.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.Channel_txt_4)

        self.lcd_R1_pos = QLCDNumber(self.centralwidget)
        self.lcd_R1_pos.setObjectName(u"lcd_R1_pos")
        sizePolicy4.setHeightForWidth(self.lcd_R1_pos.sizePolicy().hasHeightForWidth())
        self.lcd_R1_pos.setSizePolicy(sizePolicy4)
        self.lcd_R1_pos.setMinimumSize(QSize(80, 40))
        self.lcd_R1_pos.setMaximumSize(QSize(150, 16777215))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.lcd_R1_pos.setPalette(palette5)
        self.lcd_R1_pos.setFont(font4)
        self.lcd_R1_pos.setStyleSheet(u"\n"
"color: rgb(255, 11, 222);")
        self.lcd_R1_pos.setFrameShadow(QFrame.Sunken)
        self.lcd_R1_pos.setSmallDecimalPoint(False)
        self.lcd_R1_pos.setDigitCount(5)
        self.lcd_R1_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_6.addWidget(self.lcd_R1_pos)

        self.R1_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.R1_SpinBox.setObjectName(u"R1_SpinBox")
        self.R1_SpinBox.setMinimumSize(QSize(100, 40))
        self.R1_SpinBox.setMaximumSize(QSize(150, 16777215))
        self.R1_SpinBox.setFont(font5)
        self.R1_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_6.addWidget(self.R1_SpinBox)

        self.R1_move_btn = QPushButton(self.centralwidget)
        self.R1_move_btn.setObjectName(u"R1_move_btn")
        sizePolicy4.setHeightForWidth(self.R1_move_btn.sizePolicy().hasHeightForWidth())
        self.R1_move_btn.setSizePolicy(sizePolicy4)
        self.R1_move_btn.setMinimumSize(QSize(100, 40))
        self.R1_move_btn.setMaximumSize(QSize(150, 16777215))
        self.R1_move_btn.setFont(font)
        self.R1_move_btn.setStyleSheet(u"QPushButton{background-color: rgb(33, 190, 193);color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 102, 42);}")

        self.horizontalLayout_6.addWidget(self.R1_move_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Channel_txt_5 = QLabel(self.centralwidget)
        self.Channel_txt_5.setObjectName(u"Channel_txt_5")
        sizePolicy3.setHeightForWidth(self.Channel_txt_5.sizePolicy().hasHeightForWidth())
        self.Channel_txt_5.setSizePolicy(sizePolicy3)
        self.Channel_txt_5.setMinimumSize(QSize(75, 40))
        self.Channel_txt_5.setMaximumSize(QSize(100, 40))
        self.Channel_txt_5.setFont(font)
        self.Channel_txt_5.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.Channel_txt_5)

        self.lcd_R2_pos = QLCDNumber(self.centralwidget)
        self.lcd_R2_pos.setObjectName(u"lcd_R2_pos")
        sizePolicy4.setHeightForWidth(self.lcd_R2_pos.sizePolicy().hasHeightForWidth())
        self.lcd_R2_pos.setSizePolicy(sizePolicy4)
        self.lcd_R2_pos.setMinimumSize(QSize(80, 40))
        self.lcd_R2_pos.setMaximumSize(QSize(150, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.lcd_R2_pos.setPalette(palette6)
        self.lcd_R2_pos.setFont(font4)
        self.lcd_R2_pos.setStyleSheet(u"color: rgb(255, 11, 222);")
        self.lcd_R2_pos.setFrameShadow(QFrame.Sunken)
        self.lcd_R2_pos.setSmallDecimalPoint(False)
        self.lcd_R2_pos.setDigitCount(5)
        self.lcd_R2_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_7.addWidget(self.lcd_R2_pos)

        self.R2_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.R2_SpinBox.setObjectName(u"R2_SpinBox")
        self.R2_SpinBox.setMinimumSize(QSize(100, 40))
        self.R2_SpinBox.setMaximumSize(QSize(150, 16777215))
        self.R2_SpinBox.setFont(font5)
        self.R2_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_7.addWidget(self.R2_SpinBox)

        self.R2_move_btn = QPushButton(self.centralwidget)
        self.R2_move_btn.setObjectName(u"R2_move_btn")
        sizePolicy4.setHeightForWidth(self.R2_move_btn.sizePolicy().hasHeightForWidth())
        self.R2_move_btn.setSizePolicy(sizePolicy4)
        self.R2_move_btn.setMinimumSize(QSize(100, 40))
        self.R2_move_btn.setMaximumSize(QSize(150, 16777215))
        self.R2_move_btn.setFont(font)
        self.R2_move_btn.setStyleSheet(u"QPushButton{background-color: rgb(33, 190, 193);color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 102, 42);}")

        self.horizontalLayout_7.addWidget(self.R2_move_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Channel_txt_6 = QLabel(self.centralwidget)
        self.Channel_txt_6.setObjectName(u"Channel_txt_6")
        sizePolicy3.setHeightForWidth(self.Channel_txt_6.sizePolicy().hasHeightForWidth())
        self.Channel_txt_6.setSizePolicy(sizePolicy3)
        self.Channel_txt_6.setMinimumSize(QSize(75, 40))
        self.Channel_txt_6.setMaximumSize(QSize(100, 40))
        self.Channel_txt_6.setFont(font)
        self.Channel_txt_6.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.Channel_txt_6)

        self.lcd_R3_pos = QLCDNumber(self.centralwidget)
        self.lcd_R3_pos.setObjectName(u"lcd_R3_pos")
        sizePolicy4.setHeightForWidth(self.lcd_R3_pos.sizePolicy().hasHeightForWidth())
        self.lcd_R3_pos.setSizePolicy(sizePolicy4)
        self.lcd_R3_pos.setMinimumSize(QSize(80, 40))
        self.lcd_R3_pos.setMaximumSize(QSize(150, 16777215))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.lcd_R3_pos.setPalette(palette7)
        self.lcd_R3_pos.setFont(font4)
        self.lcd_R3_pos.setStyleSheet(u"color: rgb(255, 11, 222);")
        self.lcd_R3_pos.setFrameShadow(QFrame.Sunken)
        self.lcd_R3_pos.setSmallDecimalPoint(False)
        self.lcd_R3_pos.setDigitCount(5)
        self.lcd_R3_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_9.addWidget(self.lcd_R3_pos)

        self.R3_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.R3_SpinBox.setObjectName(u"R3_SpinBox")
        self.R3_SpinBox.setMinimumSize(QSize(100, 40))
        self.R3_SpinBox.setMaximumSize(QSize(150, 16777215))
        self.R3_SpinBox.setFont(font5)
        self.R3_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_9.addWidget(self.R3_SpinBox)

        self.R3_move_btn = QPushButton(self.centralwidget)
        self.R3_move_btn.setObjectName(u"R3_move_btn")
        sizePolicy4.setHeightForWidth(self.R3_move_btn.sizePolicy().hasHeightForWidth())
        self.R3_move_btn.setSizePolicy(sizePolicy4)
        self.R3_move_btn.setMinimumSize(QSize(100, 40))
        self.R3_move_btn.setMaximumSize(QSize(150, 16777215))
        self.R3_move_btn.setFont(font)
        self.R3_move_btn.setStyleSheet(u"QPushButton{background-color: rgb(33, 190, 193);color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 102, 42);}")

        self.horizontalLayout_9.addWidget(self.R3_move_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.Msg_box = QTextBrowser(self.centralwidget)
        self.Msg_box.setObjectName(u"Msg_box")
        self.Msg_box.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Msg_box.sizePolicy().hasHeightForWidth())
        self.Msg_box.setSizePolicy(sizePolicy5)
        self.Msg_box.setMinimumSize(QSize(360, 120))
        self.Msg_box.setMaximumSize(QSize(600, 300))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.Msg_box.setPalette(palette8)
        self.Msg_box.setFont(font)
        self.Msg_box.setStyleSheet(u"")
        self.Msg_box.setFrameShadow(QFrame.Plain)

        self.verticalLayout_6.addWidget(self.Msg_box)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Select_Plot_Option = QTabWidget(self.centralwidget)
        self.Select_Plot_Option.setObjectName(u"Select_Plot_Option")
        sizePolicy5.setHeightForWidth(self.Select_Plot_Option.sizePolicy().hasHeightForWidth())
        self.Select_Plot_Option.setSizePolicy(sizePolicy5)
        self.Select_Plot_Option.setMinimumSize(QSize(650, 600))
        self.Select_Plot_Option.setMaximumSize(QSize(3000, 1900))
        palette9 = QPalette()
        brush14 = QBrush(QColor(255, 85, 0, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        brush15 = QBrush(QColor(255, 85, 0, 128))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.Select_Plot_Option.setPalette(palette9)
        self.Select_Plot_Option.setFont(font)
        self.Select_Plot_Option.setTabPosition(QTabWidget.North)
        self.Select_Plot_Option.setTabShape(QTabWidget.Rounded)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Plot_box = QGroupBox(self.tab_2)
        self.Plot_box.setObjectName(u"Plot_box")
        sizePolicy5.setHeightForWidth(self.Plot_box.sizePolicy().hasHeightForWidth())
        self.Plot_box.setSizePolicy(sizePolicy5)
        self.Plot_box.setMinimumSize(QSize(600, 400))
        self.Plot_box.setFont(font)
        self.Plot_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout.addWidget(self.Plot_box)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 50))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.label_3.setPalette(palette10)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.Scan_Axis_cbx = QComboBox(self.tab_2)
        self.Scan_Axis_cbx.addItem("")
        self.Scan_Axis_cbx.addItem("")
        self.Scan_Axis_cbx.addItem("")
        self.Scan_Axis_cbx.setObjectName(u"Scan_Axis_cbx")
        self.Scan_Axis_cbx.setMinimumSize(QSize(100, 50))
        self.Scan_Axis_cbx.setMaximumSize(QSize(220, 16777215))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        brush16 = QBrush(QColor(180, 249, 255, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush17 = QBrush(QColor(255, 0, 127, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Highlight, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush18 = QBrush(QColor(240, 240, 240, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Inactive, QPalette.Highlight, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush19 = QBrush(QColor(0, 120, 215, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Disabled, QPalette.Highlight, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Scan_Axis_cbx.setPalette(palette11)
        self.Scan_Axis_cbx.setFont(font1)
        self.Scan_Axis_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Scan_Axis_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_8.addWidget(self.Scan_Axis_cbx)

        self.Input_scan_range_btn = QPushButton(self.tab_2)
        self.Input_scan_range_btn.setObjectName(u"Input_scan_range_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Input_scan_range_btn.sizePolicy().hasHeightForWidth())
        self.Input_scan_range_btn.setSizePolicy(sizePolicy6)
        self.Input_scan_range_btn.setMinimumSize(QSize(150, 50))
        self.Input_scan_range_btn.setMaximumSize(QSize(200, 16777215))
        palette12 = QPalette()
        brush20 = QBrush(QColor(255, 255, 255, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush20)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush20)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        brush21 = QBrush(QColor(255, 85, 127, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.HighlightedText, brush21)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush20)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush20)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush20)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush21)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush21)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.Input_scan_range_btn.setPalette(palette12)
        self.Input_scan_range_btn.setFont(font)
        self.Input_scan_range_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_8.addWidget(self.Input_scan_range_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.Start_plot = QPushButton(self.tab_2)
        self.Start_plot.setObjectName(u"Start_plot")
        sizePolicy4.setHeightForWidth(self.Start_plot.sizePolicy().hasHeightForWidth())
        self.Start_plot.setSizePolicy(sizePolicy4)
        self.Start_plot.setMinimumSize(QSize(120, 50))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush20)
        brush22 = QBrush(QColor(127, 127, 127, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush22)
        brush23 = QBrush(QColor(170, 170, 170, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush23)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush20)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush20)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        brush24 = QBrush(QColor(0, 0, 0, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush24)
        palette13.setBrush(QPalette.Active, QPalette.HighlightedText, brush21)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush20)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush20)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush23)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush20)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush20)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush21)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush20)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush23)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush24)
        palette13.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush21)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.Start_plot.setPalette(palette13)
        self.Start_plot.setFont(font1)
        self.Start_plot.setFocusPolicy(Qt.ClickFocus)
        self.Start_plot.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.Start_plot.setCheckable(False)
        self.Start_plot.setAutoDefault(False)
        self.Start_plot.setFlat(False)

        self.horizontalLayout_8.addWidget(self.Start_plot)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.Stop_plot = QPushButton(self.tab_2)
        self.Stop_plot.setObjectName(u"Stop_plot")
        sizePolicy4.setHeightForWidth(self.Stop_plot.sizePolicy().hasHeightForWidth())
        self.Stop_plot.setSizePolicy(sizePolicy4)
        self.Stop_plot.setMinimumSize(QSize(120, 50))
        self.Stop_plot.setFont(font1)
        self.Stop_plot.setFocusPolicy(Qt.WheelFocus)
        self.Stop_plot.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 117, 0) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_8.addWidget(self.Stop_plot)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.Clear_Save = QPushButton(self.tab_2)
        self.Clear_Save.setObjectName(u"Clear_Save")
        sizePolicy2.setHeightForWidth(self.Clear_Save.sizePolicy().hasHeightForWidth())
        self.Clear_Save.setSizePolicy(sizePolicy2)
        self.Clear_Save.setMinimumSize(QSize(150, 50))
        self.Clear_Save.setFont(font1)
        self.Clear_Save.setStyleSheet(u"\n"
"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 3"
                        "3);}\n"
"")

        self.horizontalLayout_8.addWidget(self.Clear_Save)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.Select_Plot_Option.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout = QGridLayout(self.tab_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pAmeter_plot = QGroupBox(self.tab_5)
        self.pAmeter_plot.setObjectName(u"pAmeter_plot")
        sizePolicy5.setHeightForWidth(self.pAmeter_plot.sizePolicy().hasHeightForWidth())
        self.pAmeter_plot.setSizePolicy(sizePolicy5)
        self.pAmeter_plot.setMinimumSize(QSize(600, 400))
        self.pAmeter_plot.setFont(font)
        self.pAmeter_plot.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout_3.addWidget(self.pAmeter_plot)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lcd_pA = QLCDNumber(self.tab_5)
        self.lcd_pA.setObjectName(u"lcd_pA")
        sizePolicy4.setHeightForWidth(self.lcd_pA.sizePolicy().hasHeightForWidth())
        self.lcd_pA.setSizePolicy(sizePolicy4)
        self.lcd_pA.setMinimumSize(QSize(200, 50))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.lcd_pA.setPalette(palette14)
        self.lcd_pA.setFont(font)
        self.lcd_pA.setDigitCount(8)
        self.lcd_pA.setSegmentStyle(QLCDNumber.Filled)

        self.horizontalLayout_10.addWidget(self.lcd_pA)

        self.Current_label = QLabel(self.tab_5)
        self.Current_label.setObjectName(u"Current_label")
        self.Current_label.setMinimumSize(QSize(30, 50))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.Current_label.setPalette(palette15)
        self.Current_label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.Current_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.Monitor_pA = QPushButton(self.tab_5)
        self.Monitor_pA.setObjectName(u"Monitor_pA")
        sizePolicy2.setHeightForWidth(self.Monitor_pA.sizePolicy().hasHeightForWidth())
        self.Monitor_pA.setSizePolicy(sizePolicy2)
        self.Monitor_pA.setMinimumSize(QSize(125, 50))
        self.Monitor_pA.setFont(font1)
        self.Monitor_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.Monitor_pA.setFlat(False)

        self.horizontalLayout_10.addWidget(self.Monitor_pA)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.Stop_Monitor_pA = QPushButton(self.tab_5)
        self.Stop_Monitor_pA.setObjectName(u"Stop_Monitor_pA")
        sizePolicy2.setHeightForWidth(self.Stop_Monitor_pA.sizePolicy().hasHeightForWidth())
        self.Stop_Monitor_pA.setSizePolicy(sizePolicy2)
        self.Stop_Monitor_pA.setMinimumSize(QSize(125, 50))
        self.Stop_Monitor_pA.setFont(font1)
        self.Stop_Monitor_pA.setStyleSheet(u"QPushButton{background-color:  rgb(255, 91, 58);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 85, 127) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);"
                        "}")

        self.horizontalLayout_10.addWidget(self.Stop_Monitor_pA)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.Clear_Monitor_pA = QPushButton(self.tab_5)
        self.Clear_Monitor_pA.setObjectName(u"Clear_Monitor_pA")
        sizePolicy2.setHeightForWidth(self.Clear_Monitor_pA.sizePolicy().hasHeightForWidth())
        self.Clear_Monitor_pA.setSizePolicy(sizePolicy2)
        self.Clear_Monitor_pA.setMinimumSize(QSize(125, 50))
        self.Clear_Monitor_pA.setFont(font1)
        self.Clear_Monitor_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:1px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_10.addWidget(self.Clear_Monitor_pA)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.Select_Plot_Option.addTab(self.tab_5, "")

        self.verticalLayout_5.addWidget(self.Select_Plot_Option)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Now_T = QLabel(self.centralwidget)
        self.Now_T.setObjectName(u"Now_T")
        sizePolicy.setHeightForWidth(self.Now_T.sizePolicy().hasHeightForWidth())
        self.Now_T.setSizePolicy(sizePolicy)
        self.Now_T.setMinimumSize(QSize(250, 30))
        self.Now_T.setMaximumSize(QSize(1000, 40))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        brush25 = QBrush(QColor(44, 213, 196, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush25)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush20)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush20)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush25)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush20)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush25)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush20)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush20)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush25)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush25)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush25)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.Now_T.setPalette(palette16)
        self.Now_T.setFont(font)
        self.Now_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Now_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Now_T)

        self.Expect_FN_T = QLabel(self.centralwidget)
        self.Expect_FN_T.setObjectName(u"Expect_FN_T")
        sizePolicy.setHeightForWidth(self.Expect_FN_T.sizePolicy().hasHeightForWidth())
        self.Expect_FN_T.setSizePolicy(sizePolicy)
        self.Expect_FN_T.setMinimumSize(QSize(250, 30))
        self.Expect_FN_T.setMaximumSize(QSize(1000, 40))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush25)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush20)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush25)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush25)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush25)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush25)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush25)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.Expect_FN_T.setPalette(palette17)
        self.Expect_FN_T.setFont(font)
        self.Expect_FN_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Expect_FN_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Expect_FN_T)

        self.Done_time = QLabel(self.centralwidget)
        self.Done_time.setObjectName(u"Done_time")
        sizePolicy.setHeightForWidth(self.Done_time.sizePolicy().hasHeightForWidth())
        self.Done_time.setSizePolicy(sizePolicy)
        self.Done_time.setMinimumSize(QSize(250, 30))
        self.Done_time.setMaximumSize(QSize(1000, 40))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush20)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush25)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush20)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush20)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush25)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush20)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush25)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush20)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush20)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush25)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush25)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush25)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.Done_time.setPalette(palette18)
        self.Done_time.setFont(font)
        self.Done_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Done_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Done_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 30))
        palette19 = QPalette()
        self.menubar.setPalette(palette19)
        self.menubar.setFont(font1)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.menuMenu.setFont(font6)
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        self.menuAnalysis.setFont(font6)
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        self.menuInstrument.setFont(font6)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setFont(font6)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuInstrument.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuAnalysis.addAction(self.actionViewData)
        self.menuAnalysis.addAction(self.actionDatabase)
        self.menuInstrument.addAction(self.actionMotionMotor)
        self.menuInstrument.addAction(self.actionpAmeter)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.Select_Plot_Option.setCurrentIndex(0)
        self.Start_plot.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionViewData.setText(QCoreApplication.translate("MainWindow", u"ViewData", None))
        self.actionDatabase.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.actionMotionMotor.setText(QCoreApplication.translate("MainWindow", u"MotionMotor", None))
        self.actionpAmeter.setText(QCoreApplication.translate("MainWindow", u"pAmeter", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Msg_box_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ff5500;\">BeamSpotScan@09U-ARPES</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Developer: LiminZhou@SSRF</span></p>\n"
"<p align=\""
                        "center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Current version:1.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2023-03</span></p></body></html>", None))
        self.UserName_input.setInputMask("")
        self.UserName_input.setText("")
        self.UserName_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.ConnectWS_btn.setText(QCoreApplication.translate("MainWindow", u"MotionMotor", None))
#if QT_CONFIG(tooltip)
        self.Connect_pAmeter_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Electrometer6514", None))
#endif // QT_CONFIG(tooltip)
        self.Connect_pAmeter_btn.setText(QCoreApplication.translate("MainWindow", u"Connect 6514", None))
        self.ARPES_label.setText("")
        self.Channel_txt_1.setText(QCoreApplication.translate("MainWindow", u"X(mm)", None))
#if QT_CONFIG(tooltip)
        self.lcd_X_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.X_move_btn.setText(QCoreApplication.translate("MainWindow", u"move", None))
        self.Channel_txt_2.setText(QCoreApplication.translate("MainWindow", u"Y(mm)", None))
#if QT_CONFIG(tooltip)
        self.lcd_Y_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.Y_move_btn.setText(QCoreApplication.translate("MainWindow", u"move", None))
        self.Channel_txt_3.setText(QCoreApplication.translate("MainWindow", u"Z(mm)", None))
#if QT_CONFIG(tooltip)
        self.lcd_Z_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.Z_move_btn.setText(QCoreApplication.translate("MainWindow", u"move", None))
        self.Channel_txt_4.setText(QCoreApplication.translate("MainWindow", u"R1(deg)", None))
#if QT_CONFIG(tooltip)
        self.lcd_R1_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.R1_move_btn.setText(QCoreApplication.translate("MainWindow", u"move", None))
        self.Channel_txt_5.setText(QCoreApplication.translate("MainWindow", u"R2(deg)", None))
#if QT_CONFIG(tooltip)
        self.lcd_R2_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.R2_move_btn.setText(QCoreApplication.translate("MainWindow", u"move", None))
        self.Channel_txt_6.setText(QCoreApplication.translate("MainWindow", u"R3(deg)", None))
#if QT_CONFIG(tooltip)
        self.lcd_R3_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.R3_move_btn.setText(QCoreApplication.translate("MainWindow", u"move", None))
        self.Msg_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt;&gt;</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.Plot_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot_area", None))
#endif // QT_CONFIG(statustip)
        self.Plot_box.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Scan Axis", None))
        self.Scan_Axis_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.Scan_Axis_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.Scan_Axis_cbx.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.Input_scan_range_btn.setText(QCoreApplication.translate("MainWindow", u"ScanRange", None))
#if QT_CONFIG(tooltip)
        self.Start_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Start_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"begin scan,should choose scan mode and scan range", None))
#endif // QT_CONFIG(statustip)
        self.Start_plot.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.Stop_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Stop_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"Stop scan", None))
#endif // QT_CONFIG(statustip)
        self.Stop_plot.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.Clear_Save.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Clear_Save.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear data in the plot and save ", None))
#endif // QT_CONFIG(statustip)
        self.Clear_Save.setText(QCoreApplication.translate("MainWindow", u"Clear+Save", None))
        self.Select_Plot_Option.setTabText(self.Select_Plot_Option.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"BeamSpotSize", None))
#if QT_CONFIG(statustip)
        self.pAmeter_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot_area", None))
#endif // QT_CONFIG(statustip)
        self.pAmeter_plot.setTitle("")
#if QT_CONFIG(tooltip)
        self.lcd_pA.setToolTip(QCoreApplication.translate("MainWindow", u"read value", None))
#endif // QT_CONFIG(tooltip)
        self.Current_label.setText(QCoreApplication.translate("MainWindow", u"pA", None))
        self.Monitor_pA.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.Stop_Monitor_pA.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Clear_Monitor_pA.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Select_Plot_Option.setTabText(self.Select_Plot_Option.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"pAmeterMonitor", None))
        self.Now_T.setText(QCoreApplication.translate("MainWindow", u"Now", None))
        self.Expect_FN_T.setText("")
        self.Done_time.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuInstrument.setTitle(QCoreApplication.translate("MainWindow", u"Instrument", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


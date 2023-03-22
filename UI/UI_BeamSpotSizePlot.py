# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_BeamSpotSizePlot.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 850)
        MainWindow.setMinimumSize(QSize(1600, 850))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 60))
        self.label_4.setMaximumSize(QSize(470, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 106, 60, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(85, 170, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_4.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Ch_data = QLineEdit(self.centralwidget)
        self.Ch_data.setObjectName(u"Ch_data")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Ch_data.sizePolicy().hasHeightForWidth())
        self.Ch_data.setSizePolicy(sizePolicy1)
        self.Ch_data.setMinimumSize(QSize(170, 40))
        self.Ch_data.setMaximumSize(QSize(400, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.Ch_data.setFont(font1)
        self.Ch_data.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Ch_data)

        self.ConnectWS_btn = QPushButton(self.centralwidget)
        self.ConnectWS_btn.setObjectName(u"ConnectWS_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ConnectWS_btn.sizePolicy().hasHeightForWidth())
        self.ConnectWS_btn.setSizePolicy(sizePolicy2)
        self.ConnectWS_btn.setMinimumSize(QSize(180, 40))
        self.ConnectWS_btn.setMaximumSize(QSize(250, 16777215))
        self.ConnectWS_btn.setFont(font1)
        self.ConnectWS_btn.setStyleSheet(u"background-color: rgb(255, 109, 60);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ConnectWS_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Port_cbx = QComboBox(self.centralwidget)
        self.Port_cbx.setObjectName(u"Port_cbx")
        self.Port_cbx.setMinimumSize(QSize(170, 40))
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
        self.Connect_pAmeter_btn.setMinimumSize(QSize(180, 40))
        self.Connect_pAmeter_btn.setMaximumSize(QSize(250, 16777215))
        self.Connect_pAmeter_btn.setFont(font1)
        self.Connect_pAmeter_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);}\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);color: rgb(255, 255, 255);}")

        self.horizontalLayout_2.addWidget(self.Connect_pAmeter_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

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
        sizePolicy.setHeightForWidth(self.lcd_X_pos.sizePolicy().hasHeightForWidth())
        self.lcd_X_pos.setSizePolicy(sizePolicy)
        self.lcd_X_pos.setMinimumSize(QSize(70, 40))
        self.lcd_X_pos.setMaximumSize(QSize(150, 16777215))
        palette1 = QPalette()
        brush5 = QBrush(QColor(255, 11, 222, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.lcd_X_pos.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.lcd_X_pos.setFont(font3)
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
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        self.X_SpinBox.setFont(font4)
        self.X_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.X_SpinBox)

        self.X_move_btn = QPushButton(self.centralwidget)
        self.X_move_btn.setObjectName(u"X_move_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.X_move_btn.sizePolicy().hasHeightForWidth())
        self.X_move_btn.setSizePolicy(sizePolicy4)
        self.X_move_btn.setMinimumSize(QSize(100, 40))
        self.X_move_btn.setMaximumSize(QSize(150, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.X_move_btn.setFont(font5)
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
        sizePolicy.setHeightForWidth(self.lcd_Y_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Y_pos.setSizePolicy(sizePolicy)
        self.lcd_Y_pos.setMinimumSize(QSize(70, 40))
        self.lcd_Y_pos.setMaximumSize(QSize(150, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.lcd_Y_pos.setPalette(palette2)
        self.lcd_Y_pos.setFont(font3)
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
        self.Y_SpinBox.setFont(font4)
        self.Y_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.Y_SpinBox)

        self.Y_move_btn = QPushButton(self.centralwidget)
        self.Y_move_btn.setObjectName(u"Y_move_btn")
        sizePolicy.setHeightForWidth(self.Y_move_btn.sizePolicy().hasHeightForWidth())
        self.Y_move_btn.setSizePolicy(sizePolicy)
        self.Y_move_btn.setMinimumSize(QSize(100, 40))
        self.Y_move_btn.setMaximumSize(QSize(150, 16777215))
        self.Y_move_btn.setFont(font5)
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
        sizePolicy.setHeightForWidth(self.lcd_Z_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Z_pos.setSizePolicy(sizePolicy)
        self.lcd_Z_pos.setMinimumSize(QSize(80, 40))
        self.lcd_Z_pos.setMaximumSize(QSize(150, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.lcd_Z_pos.setPalette(palette3)
        self.lcd_Z_pos.setFont(font3)
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
        self.Z_SpinBox.setFont(font4)
        self.Z_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.Z_SpinBox)

        self.Z_move_btn = QPushButton(self.centralwidget)
        self.Z_move_btn.setObjectName(u"Z_move_btn")
        sizePolicy.setHeightForWidth(self.Z_move_btn.sizePolicy().hasHeightForWidth())
        self.Z_move_btn.setSizePolicy(sizePolicy)
        self.Z_move_btn.setMinimumSize(QSize(100, 40))
        self.Z_move_btn.setMaximumSize(QSize(150, 16777215))
        self.Z_move_btn.setFont(font5)
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
        self.Channel_txt_4.setFont(font5)
        self.Channel_txt_4.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.Channel_txt_4)

        self.lcd_R1_pos = QLCDNumber(self.centralwidget)
        self.lcd_R1_pos.setObjectName(u"lcd_R1_pos")
        sizePolicy.setHeightForWidth(self.lcd_R1_pos.sizePolicy().hasHeightForWidth())
        self.lcd_R1_pos.setSizePolicy(sizePolicy)
        self.lcd_R1_pos.setMinimumSize(QSize(80, 40))
        self.lcd_R1_pos.setMaximumSize(QSize(150, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.lcd_R1_pos.setPalette(palette4)
        self.lcd_R1_pos.setFont(font3)
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
        self.R1_SpinBox.setFont(font4)
        self.R1_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_6.addWidget(self.R1_SpinBox)

        self.R1_move_btn = QPushButton(self.centralwidget)
        self.R1_move_btn.setObjectName(u"R1_move_btn")
        sizePolicy.setHeightForWidth(self.R1_move_btn.sizePolicy().hasHeightForWidth())
        self.R1_move_btn.setSizePolicy(sizePolicy)
        self.R1_move_btn.setMinimumSize(QSize(100, 40))
        self.R1_move_btn.setMaximumSize(QSize(150, 16777215))
        self.R1_move_btn.setFont(font5)
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
        self.Channel_txt_5.setFont(font5)
        self.Channel_txt_5.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.Channel_txt_5)

        self.lcd_R2_pos = QLCDNumber(self.centralwidget)
        self.lcd_R2_pos.setObjectName(u"lcd_R2_pos")
        sizePolicy.setHeightForWidth(self.lcd_R2_pos.sizePolicy().hasHeightForWidth())
        self.lcd_R2_pos.setSizePolicy(sizePolicy)
        self.lcd_R2_pos.setMinimumSize(QSize(80, 40))
        self.lcd_R2_pos.setMaximumSize(QSize(150, 16777215))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.lcd_R2_pos.setPalette(palette5)
        self.lcd_R2_pos.setFont(font3)
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
        self.R2_SpinBox.setFont(font4)
        self.R2_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_7.addWidget(self.R2_SpinBox)

        self.R2_move_btn = QPushButton(self.centralwidget)
        self.R2_move_btn.setObjectName(u"R2_move_btn")
        sizePolicy.setHeightForWidth(self.R2_move_btn.sizePolicy().hasHeightForWidth())
        self.R2_move_btn.setSizePolicy(sizePolicy)
        self.R2_move_btn.setMinimumSize(QSize(100, 40))
        self.R2_move_btn.setMaximumSize(QSize(150, 16777215))
        self.R2_move_btn.setFont(font5)
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
        self.Channel_txt_6.setFont(font5)
        self.Channel_txt_6.setStyleSheet(u"color: rgb(255, 114, 20);")
        self.Channel_txt_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.Channel_txt_6)

        self.lcd_R3_pos = QLCDNumber(self.centralwidget)
        self.lcd_R3_pos.setObjectName(u"lcd_R3_pos")
        sizePolicy.setHeightForWidth(self.lcd_R3_pos.sizePolicy().hasHeightForWidth())
        self.lcd_R3_pos.setSizePolicy(sizePolicy)
        self.lcd_R3_pos.setMinimumSize(QSize(80, 40))
        self.lcd_R3_pos.setMaximumSize(QSize(150, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.lcd_R3_pos.setPalette(palette6)
        self.lcd_R3_pos.setFont(font3)
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
        self.R3_SpinBox.setFont(font4)
        self.R3_SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_9.addWidget(self.R3_SpinBox)

        self.R3_move_btn = QPushButton(self.centralwidget)
        self.R3_move_btn.setObjectName(u"R3_move_btn")
        sizePolicy.setHeightForWidth(self.R3_move_btn.sizePolicy().hasHeightForWidth())
        self.R3_move_btn.setSizePolicy(sizePolicy)
        self.R3_move_btn.setMinimumSize(QSize(100, 40))
        self.R3_move_btn.setMaximumSize(QSize(150, 16777215))
        self.R3_move_btn.setFont(font5)
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
        self.Msg_box.setMinimumSize(QSize(430, 100))
        self.Msg_box.setMaximumSize(QSize(600, 1000))
        palette7 = QPalette()
        brush6 = QBrush(QColor(0, 170, 127, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush7)
        brush8 = QBrush(QColor(0, 170, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Msg_box.setPalette(palette7)
        self.Msg_box.setFont(font5)
        self.Msg_box.setStyleSheet(u"background-image:url(:/icons/icons/my_style_signature.png)\n"
"")

        self.verticalLayout_6.addWidget(self.Msg_box)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Select_Plot_Option = QTabWidget(self.centralwidget)
        self.Select_Plot_Option.setObjectName(u"Select_Plot_Option")
        sizePolicy4.setHeightForWidth(self.Select_Plot_Option.sizePolicy().hasHeightForWidth())
        self.Select_Plot_Option.setSizePolicy(sizePolicy4)
        self.Select_Plot_Option.setMinimumSize(QSize(1100, 600))
        self.Select_Plot_Option.setMaximumSize(QSize(3000, 1900))
        palette8 = QPalette()
        brush11 = QBrush(QColor(255, 85, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        brush12 = QBrush(QColor(255, 85, 0, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Select_Plot_Option.setPalette(palette8)
        self.Select_Plot_Option.setFont(font5)
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
        self.Plot_box.setMinimumSize(QSize(800, 600))
        self.Plot_box.setFont(font5)
        self.Plot_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout.addWidget(self.Plot_box)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 50))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_3.setPalette(palette9)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.Axis_cbx = QComboBox(self.tab_2)
        self.Axis_cbx.addItem("")
        self.Axis_cbx.addItem("")
        self.Axis_cbx.addItem("")
        self.Axis_cbx.setObjectName(u"Axis_cbx")
        self.Axis_cbx.setMinimumSize(QSize(100, 50))
        self.Axis_cbx.setMaximumSize(QSize(220, 16777215))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        brush13 = QBrush(QColor(180, 249, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush13)
        brush14 = QBrush(QColor(255, 0, 127, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Highlight, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        brush15 = QBrush(QColor(240, 240, 240, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Inactive, QPalette.Highlight, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        brush16 = QBrush(QColor(0, 120, 215, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Disabled, QPalette.Highlight, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.Axis_cbx.setPalette(palette10)
        self.Axis_cbx.setFont(font1)
        self.Axis_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Axis_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_8.addWidget(self.Axis_cbx)

        self.Input_scan_range_btn = QPushButton(self.tab_2)
        self.Input_scan_range_btn.setObjectName(u"Input_scan_range_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Input_scan_range_btn.sizePolicy().hasHeightForWidth())
        self.Input_scan_range_btn.setSizePolicy(sizePolicy6)
        self.Input_scan_range_btn.setMinimumSize(QSize(150, 50))
        self.Input_scan_range_btn.setMaximumSize(QSize(200, 16777215))
        palette11 = QPalette()
        brush17 = QBrush(QColor(255, 255, 255, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush18 = QBrush(QColor(255, 85, 127, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.HighlightedText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.Input_scan_range_btn.setPalette(palette11)
        self.Input_scan_range_btn.setFont(font5)
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
        sizePolicy.setHeightForWidth(self.Start_plot.sizePolicy().hasHeightForWidth())
        self.Start_plot.setSizePolicy(sizePolicy)
        self.Start_plot.setMinimumSize(QSize(120, 50))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush17)
        brush19 = QBrush(QColor(127, 127, 127, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush19)
        brush20 = QBrush(QColor(170, 170, 170, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush20)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush21 = QBrush(QColor(0, 0, 0, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush21)
        palette12.setBrush(QPalette.Active, QPalette.HighlightedText, brush18)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush19)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush20)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush18)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush17)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush19)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.Start_plot.setPalette(palette12)
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
        sizePolicy.setHeightForWidth(self.Stop_plot.sizePolicy().hasHeightForWidth())
        self.Stop_plot.setSizePolicy(sizePolicy)
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
        self.pA_Plot_box = QGroupBox(self.tab_5)
        self.pA_Plot_box.setObjectName(u"pA_Plot_box")
        sizePolicy5.setHeightForWidth(self.pA_Plot_box.sizePolicy().hasHeightForWidth())
        self.pA_Plot_box.setSizePolicy(sizePolicy5)
        self.pA_Plot_box.setMinimumSize(QSize(800, 600))
        self.pA_Plot_box.setFont(font5)
        self.pA_Plot_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout_3.addWidget(self.pA_Plot_box)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lcd_pA = QLCDNumber(self.tab_5)
        self.lcd_pA.setObjectName(u"lcd_pA")
        sizePolicy.setHeightForWidth(self.lcd_pA.sizePolicy().hasHeightForWidth())
        self.lcd_pA.setSizePolicy(sizePolicy)
        self.lcd_pA.setMinimumSize(QSize(200, 50))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_pA.setPalette(palette13)
        self.lcd_pA.setFont(font5)
        self.lcd_pA.setDigitCount(8)
        self.lcd_pA.setSegmentStyle(QLCDNumber.Filled)

        self.horizontalLayout_10.addWidget(self.lcd_pA)

        self.Current_label = QLabel(self.tab_5)
        self.Current_label.setObjectName(u"Current_label")
        self.Current_label.setMinimumSize(QSize(30, 50))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Current_label.setPalette(palette14)
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
        self.Monitor_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
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
        self.Stop_Monitor_pA.setStyleSheet(u"QPushButton{background-color:  rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 85, 127) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
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
        self.Clear_Monitor_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
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
        sizePolicy4.setHeightForWidth(self.Now_T.sizePolicy().hasHeightForWidth())
        self.Now_T.setSizePolicy(sizePolicy4)
        self.Now_T.setMinimumSize(QSize(250, 30))
        self.Now_T.setMaximumSize(QSize(1000, 40))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        brush22 = QBrush(QColor(44, 213, 196, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush22)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush22)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush22)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush22)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush22)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.Now_T.setPalette(palette15)
        self.Now_T.setFont(font5)
        self.Now_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Now_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Now_T)

        self.Expect_FN_T = QLabel(self.centralwidget)
        self.Expect_FN_T.setObjectName(u"Expect_FN_T")
        sizePolicy4.setHeightForWidth(self.Expect_FN_T.sizePolicy().hasHeightForWidth())
        self.Expect_FN_T.setSizePolicy(sizePolicy4)
        self.Expect_FN_T.setMinimumSize(QSize(250, 30))
        self.Expect_FN_T.setMaximumSize(QSize(1000, 40))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush22)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush22)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush22)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush22)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush22)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.Expect_FN_T.setPalette(palette16)
        self.Expect_FN_T.setFont(font5)
        self.Expect_FN_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Expect_FN_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Expect_FN_T)

        self.Done_time = QLabel(self.centralwidget)
        self.Done_time.setObjectName(u"Done_time")
        sizePolicy4.setHeightForWidth(self.Done_time.sizePolicy().hasHeightForWidth())
        self.Done_time.setSizePolicy(sizePolicy4)
        self.Done_time.setMinimumSize(QSize(250, 30))
        self.Done_time.setMaximumSize(QSize(1000, 40))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush22)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush22)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush22)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush22)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush22)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.Done_time.setPalette(palette17)
        self.Done_time.setFont(font5)
        self.Done_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Done_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Done_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 30))
        palette18 = QPalette()
        brush23 = QBrush(QColor(255, 0, 0, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush23)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush23)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        brush24 = QBrush(QColor(160, 160, 160, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush24)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.menubar.setPalette(palette18)
        self.menubar.setFont(font1)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuInstrument.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.Select_Plot_Option.setCurrentIndex(1)
        self.Start_plot.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"BeamSpotScan@09U-ARPES", None))
        self.Ch_data.setInputMask("")
        self.Ch_data.setText("")
        self.Ch_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.ConnectWS_btn.setText(QCoreApplication.translate("MainWindow", u"MotionMotor", None))
#if QT_CONFIG(tooltip)
        self.Connect_pAmeter_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Electrometer6514", None))
#endif // QT_CONFIG(tooltip)
        self.Connect_pAmeter_btn.setText(QCoreApplication.translate("MainWindow", u"Connect 6514", None))
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
        self.Axis_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.Axis_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.Axis_cbx.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.Input_scan_range_btn.setText(QCoreApplication.translate("MainWindow", u"Input Scan Range", None))
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
        self.pA_Plot_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot_area", None))
#endif // QT_CONFIG(statustip)
        self.pA_Plot_box.setTitle("")
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


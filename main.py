import PySide6,sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
    
from BeamSizeScan_ARPES import *

"""Main entrance  

Start Project program
"""

"""
for bat file:

@echo off
E:
cd E:\Coding\Eline20U_Control\Beam_Position_Motion
start python main.py
pause

"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BeamSpotScanControl()
    win.show()
    sys.exit(app.exec())
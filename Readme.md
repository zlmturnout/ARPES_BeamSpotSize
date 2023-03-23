# BeamSpotSize Scan Project

## <font color=#ff5722>Introduction</font>

**This is a user interface program to acquire the  Size of BeamSpot at SSRF BL09U-ARPES endstation**

## <font color=#ff3d00>Developer</font>

<font color=#00b8d4>**LiminZhou @SSRF20U**</font>

## <font color=#ff5722>Contact Author</font>

Email: zlmturnout@hotmail.com

Github page: *https://github.com/zlmturnout*

## <font color=#ff5722>Copyright</font>

Full code are hosted on Github repository: *https://github.com/zlmturnout/ARPES_BeamSpotSize*

Copyright (c) 2023 LiminZhou/zlmturnout

<font color=#00e5ff> Please Contact the Author for Any Usage</font>

## <font color=#2962ff>Basic Strategy</font>

1. Python+Qt6+Matplotlib+SciPy+Pandas+Sqlite

## <font color=#2962ff>Main Purpose</font>

1. control motor move of motion manipulator
2. acquire the PD current at different position
3. obtain the I_vs_pos plot
4. fit gauss peak to obtain the beamspot size by First Derivative of the I_vs_pos line 
5. save all processed data into multiple file types (xlsx,csv,txt,sqlitebase)
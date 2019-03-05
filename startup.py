#!/usr/bin/python
# -*- coding: utf-8 -*-

from Npp import *
import os


# D:\python_demo\qt5\logAnalytics\dist\filter_config
# D:\adbTools\notpad\LogKeyWord_config

#default_dir_path = "d:" + os.sep + "adbTools" + os.sep + "notpad" +  os.sep 
#default_file_path = default_dir_path + "LogKeyWord_config"

default_dir_path = "d:" + os.sep + "python_demo" + os.sep + "qt5" +  os.sep + "logAnalytics" +  os.sep + "dist" + os.sep 
default_file_path = default_dir_path + "filter_config"

def isFileOrDirExist(filePath):
    return os.path.exists(filePath)

def mkdirNotExist(directory):
	#console.write("---> mkdirNotExist \n")
	# 防止创建文件目录时乱码
	directory = directory.decode('utf8')
	if not os.path.exists(directory):
		os.makedirs(directory)
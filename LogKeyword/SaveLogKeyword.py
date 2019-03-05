#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

select = editor.getSelText()
#console.write("---> select: " + select + "\n")

#console.write("---> default_dir_path: " + default_dir_path + "\n")
mkdirNotExist(default_dir_path)

def saveKeyword(keword):
	#console.write("---> saveKeyword: " + keword + "\n")
	if not select:
		return
	keywork_file_obj = open(default_file_path, "a+")
	allFilter = keywork_file_obj.readline()
	filterStr = str(select).lower()
	if allFilter:
		allFilterList = allFilter.split('#@$')
		for oneFilter in allFilterList:
			if oneFilter == filterStr:
				console.write("\n");
				console.write("Appended filter log [%s] exist!" % filterStr);
				console.write("\n");
				return
	#console.write(allFilter);
	appendSelect = "#@$" + filterStr
	keywork_file_obj.write(appendSelect)
	keywork_file_obj.close()
	console.write("\n");
	console.write("Appended filter log [%s]" % filterStr);
	console.write("\n");


saveKeyword(select)
	
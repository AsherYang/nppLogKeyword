#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

import sys


reload(sys)
sys.setdefaultencoding('utf8')

class Notepad(QtGui.QMainWindow):
	def __init__(self):
		super(Notepad, self).__init__()
		self.initUi()
		self.filterList = []
	
	def initUi(self):
		centralWidget = QtGui.QWidget()
		mainLayout = QtGui.QVBoxLayout()
		self.searchEdit = QtGui.QLineEdit()
		self.edit = QtGui.QTextEdit()
		self.setGeometry(300,300,300,300)
		self.setWindowTitle('Filter')
		
		self.searchEdit.connect(self.searchEdit, QtCore.SIGNAL('textChanged(QString)'), self.searchEditChange)
		
		mainLayout.addWidget(self.searchEdit)
		mainLayout.addWidget(self.edit)
		centralWidget.setLayout(mainLayout)
		self.setCentralWidget(centralWidget)
		self.show()
	
	def setEdit(self, text):
		if not text:
			return
		self.edit.setText(text.decode("utf8"))

	def loadKeyword(self):
		keyword_file_obj = open(default_file_path, "a+")
		allFilter = keyword_file_obj.readline()
		if allFilter:
			allFilterList = allFilter.encode("utf8").split('#@$')
			self.filterList = allFilterList
			#for oneFilter in allFilterList:
			#	console.write(oneFilter)
			#	console.write("\n")
			filterStr = "\n".join(allFilterList)
		keyword_file_obj.close()
		return filterStr

	def searchEditChange(self, text):
		if not self.filterList:
			return
		searchList = []
		for filterStr in self.filterList:
			if filterStr.find(text) != -1:
				#console.write("--> filterStr: %s \n" %filterStr)
				searchList.append(filterStr.encode("utf8"))
		if searchList:
			self.setEdit("\n".join(searchList))

def main():
	app = QtGui.QApplication(sys.argv)
	notepad = Notepad()
	keyword = notepad.loadKeyword()
	notepad.setEdit(keyword)
	app.exec_()

if __name__ == '__main__':
	main()



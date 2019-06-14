#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import subprocess

class PullSprdLog():
	def __init__(self):
		self.sprd_cmd_path = 'D:\\AndroidLogger\\sprd_pull_log.bat'
		
	def pull(self):
		thread = threading.Thread(target=self.copy_log)
		thread.setDaemon(True)
		thread.start()

	def copy_log(self):
		runSysCmd = RunSysCommand()
		runSysCmd.run(self.sprd_cmd_path)

class RunSysCommand:
    def __init__(self):
        pass

    # 这种方法直接调用，不输出结果
    # def run(self, command):
    #     return subprocess.call(command, shell=True)

    # 该种方法可以获取到终端输出结果
    # 通过 callback 把 msg 传递出去。
    # should_process=True, 默认解析数据，并通过callBack回调出去。
    def run(self, command, callback=None, should_process=True, shell=True):
        process = subprocess.Popen(command, shell=shell, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        while should_process and process.poll() is None:
            line = process.stdout.readline()
            line = line.strip()
            if line:
                # print "out put = ", format(line)
                if callback:
                    callback(format(line))
        if process.returncode == 0:
            # print 'sub process success.'
            if callback:
                callback('sub process success.')
        else:
            # print 'sub process fail.'
            if callback:
                callback('sub process fail.')
        return process
		

if __name__ == '__main__':
	sprdLog = PullSprdLog()
	sprdLog.copy_log()
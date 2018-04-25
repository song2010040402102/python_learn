#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
类似mysql的source命令，可以批量执行sql文件，默认操作与sql文件名对应的数据库
用法：./source.py [dir/file]
对于数据库host、port、user、password，可自行修改
目前支持ansi和utf-8编码的sql文件
脚本执行过程中可能会有warning，可忽略
'''

import os
import sys
import MySQLdb
	
def clear_comment(data):
	#clear multi-line comment
	pos1, pos2 = 0, 0
	while True:
		pos2 = data.find("/*", pos1)
		if(pos2 == -1):
			break
		else:
			pos1 = pos2
			pos2 = data.find("*/", pos1)
			if(pos2 == -1):
				data = data[:pos1]
			else:				
				data = data[:pos1] + data[pos2+2:]
	#clear single-line comment
	pos1, pos2 = 0, 0
	while True:
		p1 = data.find("#", pos1)
		p2 = data.find("-- ", pos1)		
		if(p1 == -1):
			pos2 = p2
		elif(p2 == -1):
			pos2 = p1
		elif(p1 > p2):
			pos2 = p2
		else:
			pos2 = p1
		if(pos2 == -1):
			break
		else:
			pos1 = pos2
			pos2 = data.find("\n", pos1)			
			if(pos2 == -1):
				data = data[:pos1]
			else:				
				data = data[:pos1] + data[pos2+1:]
	return data

def parse_sql(data):	
	data = clear_comment(data)
	data = data.replace("\xef\xbb\xbf", "")
	data = data.replace("\r", "")
	data = data.replace("\n", "")
	data = data.split(";")
	sqls = []
	for s in data:
		s.strip(" \t")
		if(len(s) > 0):	
			sqls.append(s)
	return sqls

def execute_sql_dir(cur, dir):
	if(dir[-1] != '/'):
		dir += '/'
	files = os.listdir(dir)
	for file in files:
		if(os.path.isfile(dir + file)):
			execute_sql_file(cur, dir + file)

def execute_sql_file(cur, file):
	spath, sfile = os.path.split(file)
	sname, sext = os.path.splitext(sfile)
	if(len(sname) > 0):
		cur.execute("CREATE DATABASE IF NOT EXISTS %s" %sname)
		cur.execute("USE %s" %sname)
	else:
		print("invalid sql file!")
		return

	sqls = []
	with open(file, "r") as fobj:
		sqls = parse_sql(fobj.read())

	for sql in sqls:
		cur.execute(sql)
		print("[SQL]: %s" %sql)

def main(argc, argv):
	if(argc < 2):
		print("please input directory or path for sql file!")
		return

	if(os.path.exists(argv[1]) == False):
		print("%s not exist!" %argv[1])
		return

	try:
		conn = MySQLdb.connect("localhost", "root", "123456")
		cur = conn.cursor()		
		if(os.path.isdir(argv[1])):
			execute_sql_dir(cur, argv[1])
		else:
			execute_sql_file(cur, argv[1])	
		cur.close()
		conn.commit()
		conn.close()
	except MySQLdb.Error,e:
		print("ERROR %d: %s" %(e.args[0], e.args[1]))	

if __name__ == '__main__':
	main(len(sys.argv), sys.argv)
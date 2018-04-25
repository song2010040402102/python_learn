#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string
import getpass
import MySQLdb

def parse_login_info(info):
	host = info[info.find('@')+1 : info.find(':')]
	port = string.atoi(info[info.find(':')+1:])
	user = info[0:info.find('@')]		
	return host, port, user	

def execute_sql(cur):
	while(True):
		sql = raw_input(">>> ").strip('\r\n')
		if(sql == "q" or sql == "quit"):
			break
		cur.execute(sql)
		result = cur.fetchall()
		for row in result:
			print(row)
			
def main(argc, argv):
	host = "localhost"
	port = 3306
	user = "root"

	if(argc >= 2):
		host, port, user = parse_login_info(argv[1])

	pswd = getpass.getpass()

	try:
		conn = MySQLdb.connect(host, user, pswd, "", port)
		cur = conn.cursor()		
		execute_sql(cur)
		cur.close()
		conn.commit()
		conn.close()
	except MySQLdb.Error,e:
		print("ERROR %d: %s" %(e.args[0], e.args[1]))
	
if __name__ == '__main__':
	main(len(sys.argv), sys.argv)
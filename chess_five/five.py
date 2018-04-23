#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class chess:
	def __init__(self, size):		
		self.m_size = size
		self.m_board = [[0 for i in range(size)] for i in range(size)]
		self.m_side = 0

	def __board2str(self):
		ss = ("  ")
		for i in range(self.m_size):
			ss += chr(ord('A') + i) + ' '

		for i in range(self.m_size):
			ss += '\n' + chr(ord('A') + i) + ' '
			for j in range(self.m_size):
				if self.m_board[i][j] == 1:
					ch = '* '
				elif self.m_board[i][j] == 2:
					ch = 'o '
				else:
					ch = '. '				
				ss += ch
		return ss	

	def print_board(self):
		print(self.__board2str())

	def check_pos(self, x, y):
		if x >= 0 and x < self.m_size and y >= 0 and y < self.m_size:
			return True
		return False

class chess_five(chess):
	def __init__(self):
		chess.__init__(self, 15)			
		self.m_side = 1

	def move(self, x, y):
		self.m_board[x][y] = self.m_side

	def next_player(self):
		self.m_side ^= 3
		
def main(argc, argv):
	five = chess_five()	
	while True:
		five.print_board();				
		ri = raw_input("please input your step: ").strip('\r\n\t ')		
		
		x, y = -1, -1
		if ri[0] >= 'A' and ri[0] <= 'O':
			x = ord(ri[0])-ord('A')
		elif ri[0] >= 'a' and ri[0] <= 'o':
			x = ord(ri[0])-ord('a')
		if ri[-1] >= 'A' and ri[-1] <= 'O':
			y = ord(ri[-1])-ord('A')
		elif ri[-1] >= 'a' and ri[-1] <= 'o':
			y = ord(ri[-1])-ord('a')
		if five.check_pos(x, y) == False:
			print("invalid step!")
			continue
		
		five.move(x, y)
		five.next_player()

if __name__ == "__main__":
	main(len(sys.argv), sys.argv)

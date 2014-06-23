import random

__author__ = '@masterfung'


class Board(object):
	def draw_board(self):
		print '   |   |'
		print ' ' + object[7] + ' | ' + object[8] + ' | ' + object[9]
		print '   |   |'
		print '-----------'
		print '   |   |'
		print ' ' + object[4] + ' | ' + object[5] + ' | ' + object[6]
		print '   |   |'
		print '-----------'
		print '   |   |'
		print ' ' + object[1] + ' | ' + object[2] + ' | ' + object[3]
		print '   |   |'


	def display_board(self):
		pass

class Player(object):
	def __init__(self, name):
		self.name = name

	def ask_player_name(self):
		self.name = raw_input('What is your name? ')
		print 'Welcome {} to a game of tic-tac-toe.'.format(self.name)

	def input_player_letter(self):
		letter = ''
		while not (letter == 'X' or letter == 'O'):
			letter = raw_input('Do you want X or O').upper()

class Computer(object):
	pass

class GameLogic(object):
	pass
#Board().draw_board()
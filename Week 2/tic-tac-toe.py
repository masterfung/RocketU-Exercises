import random
import sys

__author__ = '@masterfung'


class Board(object):
	def __init__(self):
		self.board = [' '] * 10

	def draw_board(self):
		print '   |   |'
		print ' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9]
		print '   |   |'
		print '-----------'
		print '   |   |'
		print ' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6]
		print '   |   |'
		print '-----------'
		print '   |   |'
		print ' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3]
		print '   |   |'


	def display_board(self):
		pass

class Player(object):
	def __init__(self):
		self.ask_player_name()

	def ask_player_name(self):
		self.name = raw_input('What is your name? ')
		print 'Welcome {} to a game of tic-tac-toe.'.format(self.name)

	def input_player_letter(self):
		letter = ''
		while not (letter == 'X' or letter == 'O'):
			letter = raw_input('Do you want X or O? ').upper()
		if letter == 'X':
			return ['X', 'O']
		else:
			return ['O', 'X']

class Computer(object):
	def computer_name(self):
		computer_names = ['Billy', 'Sandy', 'Charles', 'Jeanne', 'Parker', 'Nicole']
		return random.choice(computer_names)

class GameLogic(object):
	def welcome(self):
		print 'Welcome to the game of Tic-Tac-Toe.'

	def who_goes_first(self):
		heads_tails = raw_input('Head or Tail? ').lower()
		coin_flip = ['head', 'tail']
		coin_flip_result = random.choice(coin_flip)
		print coin_flip_result
		if coin_flip_result == heads_tails:
			print '{} the Computer starts first.'.format(computer_name)
		else:
			print 'You start first.'


	def play_again(self):
		play_again = raw_input('Do you want to play again? (Y/N) ').lower()
		if play_again == 'y':
			pass
		elif play_again == 'n':
			pass
		else:
			print 'Please enter a valid input.'

	def winner_determination(self):
		pass


# GameLogic().welcome()
#
# user_name = Player()
# computer_name = Computer().computer_name()
something = Player().input_player_letter()
computer_name = Computer().computer_name()
GameLogic().who_goes_first()
# Board().draw_board()


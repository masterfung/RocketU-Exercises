import random

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
		first_to_go = random.randint(0, 1)
		if first_to_go == '0':
			return 'player'
		else:
			return 'computer'

	def play_again(self):
		play_again = raw_input('Do you want to play again? (Y/N) ').lower()
		if play_again == 'y':
			pass
		elif play_again == 'n':
			pass
		else:
			print 'Please enter a valid input.'


# GameLogic().welcome()
#
# user_name = Player()
# computer_name = Computer().computer_name()
Player().input_player_letter()
# Board().draw_board()


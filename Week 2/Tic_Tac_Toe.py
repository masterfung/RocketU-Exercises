# import modules
import random
import sys
import copy

class Computer(object):
	def computer_name(self):
		computer_names = ['Billy', 'Sandy', 'Charles', 'Jeanne', 'Parker', 'Nicole']
		return random.choice(computer_names)


class Player(object):
	def ask_player_name(self):
		self.name = raw_input('What is your name? ')
		return self.name

	def player_greeting(self):
		name = self.ask_player_name()
		print 'Welcome {} to a game of tic-tac-toe.'.format(name)

class Game(object):
	def __init__(self):
		self.board = [' '] * 9
		# self.player_name = Player().ask_player_name()
		self.player_marker = ''
		self.computer_name = Computer().computer_name()
		self.computer_marker = ''
		self.winning_combos = (
		[6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
		[0, 4, 8], [2, 4, 6],
		)
		self.corners = [0, 2, 6, 8]
		self.sides = [1, 3, 5, 7]
		self.middle = 4

		self.form = '''
		   \t| %s | %s | %s |
		   \t-------------
		   \t| %s | %s | %s |
		   \t-------------
		   \t| %s | %s | %s |
		   '''

	def draw_board(self, board=None):
		if board is None:
			print self.form % tuple(self.board[6:9] + self.board[3:6] + self.board[0:3])
		else:
			# when the game starts, display numbers on all the grids
			print self.form % tuple(board[6:9] + board[3:6] + board[0:3])

	def get_marker(self):
		marker = raw_input("Would you like your marker to be X or O?: ").upper()
		while marker not in ["X", "O"]:
			marker = raw_input("Would you like your marker to be X  or O? :").upper()
		if marker == "X":
			return ('X', 'O')
		else:
			return ('O', 'X')


	def help(self):
		print '''
\n\t The game board contains 9 squares. 1 starts @ the bottom left.).
\n\t You will need to input your choice when it is your turn via your keyboard.
\n\t To win, you will want to have 3 pieces in a horizontal, vertical or diagonal. 
\n\t Press Ctrl + C to quit
'''

	def quit_game(self):
		self.draw_board
		print "\n\t Thanks for playing TTT! \n\t We hope to see you soon!\n"
		sys.exit()

	def is_winner(self, board, marker):
		# order of checks:
		# 1. across the horizontal top
		# 2. across the horizontal middle
		# 3. across the horizontal bottom
		# 4. across the vertical left
		# 5. across the vertical middle
		# 6. across the vertical right
		# 7. across first diagonal
		# 8. across second diagonal
		for combo in self.winning_combos:
			if (board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
				return True
		return False

	def get_computer_move(self):
		# check if bot can win in the next move
		for i in range(0, len(self.board)):
			board_copy = copy.deepcopy(self.board)
			if self.is_space_free(board_copy, i):
				self.make_move(board_copy, i, self.computer_marker)
				if self.is_winner(board_copy, self.computer_marker):
					return i

		# check if player could win on his next move
		for i in range(0, len(self.board)):
			board_copy = copy.deepcopy(self.board)
			if self.is_space_free(board_copy, i):
				self.make_move(board_copy, i, self.player_marker)
				if self.is_winner(board_copy, self.player_marker):
					return i

		# check for space in the corners, and take it
		move = self.choose_random_move(self.corners)
		if move != None:
			return move

		# If the middle is free, take it
		if self.is_space_free(self.board, self.middle):
			return self.middle


		# else, take one free space on the sides
		return self.choose_random_move(self.sides)

	def is_space_free(self, board, index):
		# print "SPACE %s is taken" % index
		return board[index] == ' '

	def is_board_full(self):
		for i in range(1, 9):
			if self.is_space_free(self.board, i):
				return False
		return True

	def make_move(self, board, index, move):
		board[index] = move

	def choose_random_move(self, move_list):
		possible_winning_moves = []
		for index in move_list:
			if self.is_space_free(self.board, index):
				possible_winning_moves.append(index)
				if len(possible_winning_moves) != 0:
					return random.choice(possible_winning_moves)
				else:
					return None

	def start_game(self):
		self.draw_board(range(1, 10))
		self.help()
		self.player_name = self.get_player_name()

		# obtain user preference
		self.player_marker, self.computer_marker = self.get_marker()
		print "Your marker is " + self.player_marker

		# coin toss who goes first using randint
		if random.randint(0, 1) == 0:
			print "I will go first"
			# self.make_move(self.board,random.choice(self.corners), self.computer_marker)
			# self.draw_board()
			self.game_engine('c')
		else:
			print "You will go first"
			# now, enter the main game loop
			self.game_engine('h')

	def get_player_move(self):
		move = int(input("Pick a spot to move: (1-9) "))
		while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.is_space_free(self.board, move - 1):
			move = int(input("Your input is invalid. Please select input: (1-9) "))
		return move - 1

	def get_player_name(self):
		return "Welcome! I am %s" % self.computer_name

	def game_engine(self, turn):
		is_running = True
		player = turn  # h for human, c for computer
		computer_score = 0
		user_score = 0
		Player().player_greeting()
		while is_running:
			if player == 'h':
				user_input = self.get_player_move()
				self.make_move(self.board, user_input, self.player_marker)
				if (self.is_winner(self.board, self.player_marker)):
					self.draw_board()
					print "\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \\tn" % self.player_name
					# self.incr_score(self.player_name)
					user_score += 1
					is_running = False
					#break
				else:
					if self.is_board_full():
						self.draw_board()
						print "\n\t-- Match Draw --\t\n"
						is_running = False
						# break
					else:
						self.draw_board()
						player = 'c'
				# computer's turn to play
			else:
				computer_move = self.get_computer_move()
				self.make_move(self.board, computer_move, self.computer_marker)
				if (self.is_winner(self.board, self.computer_marker)):
					self.draw_board()
					print "\n\t%s HAS WON!!!!\t\n" % self.computer_name
					# self.incr_score(self.computer_name)
					computer_score += 1
					is_running = False
					break
				else:
					if self.is_board_full():
						self.draw_board()
						print "\n\t -- Draw -- \n\t"
						is_running = False
						# break
					else:
						self.draw_board()
						player = 'h'
		print 'Your Score: {} \t {} Score: {}'.format(user_score, self.computer_name, computer_score)
		# when you break out of the loop, end the game
		self.end_game()

	def end_game(self):
		play_again = raw_input("Do you like to play again? (y/n): ").lower()
		if play_again == 'y':
			self.__init__()  # necessary for re-initialization of the board etc
			self.start_game()
		else:
			print "\n\t-- GAME OVER!!!--\n\t"
			self.quit_game()


if __name__ == "__main__":
	TicTacToe = Game()
	TicTacToe.start_game()
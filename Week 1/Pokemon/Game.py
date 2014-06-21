import random
from pokemon import Pokemon
from trainer import Trainer

__author__ = 'htm'

BATTLE_WINNER_USER = 0
BATTLE_WINNER_COMPUTER = 1

scores = {}

class Game(object):

	def print_battle_status(self, turns, total_pokemon):
		print 'Turn {}: you have {} pokemon in your stash.'.format(turns, total_pokemon)

	def battle(self, substance, computer):
		print 'Let the battle begin!'
		print 'You have {} Pokemon, type: {}, hitpoints ' \
			  'of: {}, attacks with {}. Weakness:' \
			  ' {}.'.format(substance.name, substance.type, substance.health_points,
		substance.powers, substance.weakness)

		print 'Your opponent have {} Pokemon, type: {}, hitpoints ' \
			  'of: {}, attacks with {}. Weakness:' \
			  ' {}.'.format(computer.name, computer.type, computer.health_points,
		computer.powers, computer.weakness)

		if computer.powers == substance.weakness:
			print 'Your opponent\'s attack was super effective!'
			substance.health_points -= 10
			print 'Your pokemon has fainted!'
		elif substance.powers == computer.weakness:
			print 'Your attack was super effective!'
			computer.health_points -= 10
			print 'Your opponent\'s pokemon has fainted!'

		while computer.health_points > 0 and substance.health_points > 0:
			hit_point = self.hit_point_randomizer()
			if .5 < hit_point <= 1:
				print 'You took a hit!'
				substance.health_points -= 1
			else:
				print 'Your opponent took a hit!'
				computer.health_points -= 1

		winner = BATTLE_WINNER_USER
		if computer.health_points == 0:
			print 'You have won this match!'
		else:
			print 'Darn! You lost! Hope is not lost!'
			winner = BATTLE_WINNER_COMPUTER
		return winner


	def add_trainer(self):
		name = raw_input('What is your name? ')
		age = int(raw_input('What is your age? '))
		return Trainer(name=name, age=age)

	def computer(self):
		return Pokemon.randomizer()

	def chance(self):
		return random.uniform(0,1)

	def hit_point_randomizer(self):
		return random.uniform(0,1)

	def get_user_input(self):
		return raw_input('A egotistic trainer approaches you, '
						 'you either have to (b)attle or (r)etreat him/her: ').lower()

	def play(self):
		response = self.get_user_input()

		while True:
			total_pokemon = 6
			user_switch = 0
			turns = 1
			user_tally = 0
			computer_tally = 0

			trainer = self.add_trainer()
			print 'Welcome, {}!'.format(trainer.name)

			while response != 'r':
				if response == 'b':
					choice = self.print_battle_status(turns, total_pokemon)
					player = Pokemon.randomizer()
					computer = Pokemon.randomizer()
					prompt = raw_input('You selected ' + player.name + '. Do you want to keep? (Y/N) ').lower()
					if prompt == 'y':
						winner = self.battle(player, computer)

						if winner == BATTLE_WINNER_COMPUTER:
							computer_tally += 1
						else:
							user_tally += 1

						turns += 1
						total_pokemon -= 1

						print 'Your score: {}.'.format(user_tally)
						print 'Opponent score: {}.'.format(computer_tally)

						if total_pokemon == 0:
							if trainer.name not in scores:
								scores[trainer.name] = user_tally
							else:
								scores[trainer.name] += user_tally

							print "Scorez, bitches: {}".format(scores)

							response = self.get_user_input()
							break

					elif prompt == 'n':
						user_switch += 1
						player = Pokemon.randomizer()
						print 'The new selection is: {}.'.format(player.name)
						print 'Egotistical narsassictic trainer is ' \
							  'getting annoyed! Limit how often you use your re-select!'
				elif response == 'r':
					break
				else:
					print 'Please select a valid keystroke.'
			if response == 'r':
				break
			else:
				print 'Please enter a valid response.'
import random
from trainer import Trainer
from pokemon import Pokemon

__author__ = 'htm'

def battle():
	pokemon_choice = raw_input('Turn {}: you have {} pokemon in your stash.'
							   'This is the first pokemon: ').format(turns, total_pokemon)
	return pokemon_choice

print 'Welcome to Pokemon Trainer Battle'

user_name = raw_input('What is your name? ')

print 'Welcome, {}!'.format(user_name)

response = raw_input('A egotistic trainer approaches you, '
					 'you either have to (b)attle or (r)etreat him/her: ').lower()
total_pokemon = 6
user_switch = 0
turns = 1
pokedex = {}

while response != 'r':
	if response == 'b':
		choice = battle()
		substance = Pokemon()
		name = substance.name

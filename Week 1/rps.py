import random
import sys

def computer_random():
	options = ["Rock", "Paper", "Scissors"]
	rand = random.randint(0, 2)
	return options[rand]

def user():
	print "Press (R) for Rock, (P) for Paper, (P) for Paper, (Q) to quit!"
	user_choice = raw_input("Please make a decision: ").lower()

	if user_choice == "r":
		return "Rock"
	if user_choice == "p":
		return "Paper"
	if user_choice == "s":
		return "Scissors"
	if user_choice == "q":
		sys.exit(0)
	else:
		user()

def user_name():
	user_name = raw_input('What is your name? ')
	return user_name #when None is the output, make sure return is used!

def comparison(human_choice, computer_choice):
	if human_choice == computer_choice:
		return "Draw"
	if human_choice == "Rock" and computer_choice == "Paper":
		return "Computer Wins"
	if human_choice == "Paper" and computer_choice == "Scissors":
		return "Computer Wins"
	if human_choice == "Scissors" and computer_choice == "Rock":
		return "Computer Wins"
	else:
		return "You win"

def play_again():
	feedback = raw_input('Do you want to play again? (Y/N) ').lower()
	if feedback == 'y':
		print 'Lets play again.'
		main()
	else:
		print 'Come back again. We will miss you greatly until you return.'

def main():
	print 'Welcome to Rock, Paper, Scissors Game!'
	username = user_name()
	winning_req = int(raw_input('How many wins will it take to become the champion of this round? '))
	user_score = 0
	computer_score = 0
	while user_score < winning_req and computer_score < winning_req:
		human_choice = user()
		computer_choice = computer_random()

		print username, "chose", human_choice
		print "The mighty computer chose", computer_choice

		result = comparison(human_choice, computer_choice)

		if result == "Draw":
			print "Its a draw"
		elif result == "Computer Wins":
			print "Sorry the computer won but do not lose hope!"
			computer_score += 1
		else:
			print "Well done! Awesome Awesome. {} won!".format(username)
			user_score += 1
		print 'Final Score: Human {}		Computer {}'.format(user_score, computer_score)
		print " "
	play_again()

main()
# Program (Yatzy™ Protocol) written by: ADDI DJIKIC  (2013/2014)
# Addi 2013 KTH (Royal Institute of Technology)
# addi@kth.se
                 #------------DICES------------#
import random
import sys
import os


def roll_dice(dice_list=[]): 
	#The dice list is set to alwas have five dices to roll
    rolls = 5 - len(dice_list)

    for x in range(rolls):
    	dice_list.append(random.randint(1,6))

    return dice_list


def throw_dice():
	"""Asks the player which dices to save for the next round and rolls them"""

	saved_dices = []
	number_of_rolls = 2

	rolls = 0
	while rolls < number_of_rolls:
		
		new_dices = roll_dice(saved_dices)
		print("DICE NUMBER:		(1)(2)(3)(4)(5)")
		print("Your rolled dices are: ", new_dices)
		saved_dices = [] #clears 'saved_dices'

		dice_save = input("""\n(Input the dices you want with a space between them)
	WHICH DICES DO YOU WANT FOR THE NEXT ROUND?(1-5):""")
		print("\n")

		if dice_save.lower() == 'quit':
		 	sys.exit("PROTOCOL ENDS")	
			
		split = dice_save.split(" ")
			
		try:
			if(len(split) <= 5):
				for try_dice in split:
					picked_dice = int(try_dice)
					saved_dices.append(new_dices[picked_dice -1]) 

		except:
			print("\n\tNO dice input, ALL dices shuffled\n")

		rolls += 1

	
	new_dices = roll_dice(saved_dices)
	print("\nYOUR DICES FOR THIS ROUND IS:\n ", new_dices)
	return new_dices



		


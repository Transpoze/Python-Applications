# coding: latin1
# Program (Yatzy™ Protocol) written by: ADDI DJIKIC  (2013/2014)
# Addi 2013 KTH (Royal Institute of Technology)
# addi@kth.se

                        #-----------Functions------------#
import sys
import random
import os
from dice import *
from classes import *

def show_welcomescreen():
    """Welcome screen"""
                                   
    print("     ---------------------------------       ")
    print("         *** WELCOME TO YATZY! ***           ")
    print("     ---------------------------------       ")

#-----------------------------------------------------------------------------

def set_reminder():
    """Displays a 'remainder' at the first print of the protocol"""

    print("-Remember, you can always press 'Q' when it's your turn\nto quit the game")
    print("-Press any key in the dice mode to shuffle all dices") 
    print("-Write 'quit' in dice mode to kill the program") 
    print("-Apply a '0' to scratch a score")
    print("-Dont forget to yell Yatzhee!\n\n\n")   


#-----------------------------------------------------------------------------

def show_rules():      
    """This is used to display 'How to play' rules of the protocol if the user inputs 'R'"""

    see_rules = str(input("Press 'R' to see game rules or press 'enter' continue: "))
    if see_rules == str('r') or see_rules == str('R'):

        print("""    - Select how many players their will be playing
    - Input all the players names
    - To choose the position you want to apply the score on
    of the specific player, enter the number next to a 'Score'
    (the program will display which player turn it is)
    - After each round you MUST input a score on a position OR 
    scratch that score, you can do that with a 'zero'(0)
    - You will get a bonus if you have 63 points or more on the first six scores
    - There are 14 rounds total in Yatzy, that is when the whole 
    protocol has been filled in
    - You can always quit the game by pressing 'Q'
    - Write "quit" in dice mode to kill the program
    - To choose specific 'rolled dices' insert the dice numbers with a space between
    them, for exampel: 1 3 5 will give you the first third and fifth dice you rolled
    - You can roll dices TWO times
    - To see further rules of Yatzy visit http://en.wikipedia.org/wiki/Yatzy
        """)
        
#-----------------------------------------------------------------------------

def input_players():          
    """This adds the total players that are joining the game""" 
    
    while True:

        try:  
            max_players = 5 #Set this to change maximum players you can add to the game

            print("(Maximum numbers of players are:", max_players, ")")
            number_of_players = int(input("How many players are in the game?:"))
            print("")
        
            if number_of_players > max_players or number_of_players <= 0:
                print("\n\tINVALID NUMBER OF PLAYERS, Please try a new number\n")

            else:
                break

        except:
            print("\n\tPLEASE WRITE A NUMBER OF TOTAL PLAYERS\n")
    #os.system('clear')

    return number_of_players
#-----------------------------------------------------------------------------

def get_player_names(total_players): 
    """Function to loop and ask every player that joins to input their name,
        takes one argument, 'total_players'"""

    #This is the list that holds the player
    player_list = [] 

    for x in range(total_players):
        name_of_player = str(input("Name of player " + str(x + 1) + ":"))
        player_list.append(Player(name_of_player))

    print("") 

    return player_list

#----------------------------------------------------------------------------- 

def ask_player_score(player_list): 
    """Asks every player where to input the score and how much points,
        takes one argument player_list"""

    for every_player in range(len(player_list)): 

        print(" PLAYER:",player_list[every_player].name_of_player)
        print(" ---------")
        throw_dice() 

        while True:
            
            print(" PLAYER:", player_list[every_player].name_of_player)
            print(" ---------")

            score_position  = input("\nWrite The Number Of The Score From The List You Want To Apply At:\n(Press 'Q' to Quit the game)")
           
             
             # This code is used to exit the program 
            if score_position.lower() == 'q':

                print("\n\t(!)ALL THE PROTOCOL SCORES ARE ABOUT TO BE DELETED(!)\n")
                safe_quit = str(input("Are you sure you want to quit? (Y/N):"))

                #As a saftey, any other key will be seen as 'No'
                if safe_quit.lower() == 'y':
                    sys.exit("\nEND OF PROTOCOL") # kills the program
      
            else:
                try:
            
                    if player_list[every_player].scores.get(int(score_position) -1, False):
                        print("\n\tTHERE IS ALREADY A SCORE ON THIS POSITION!, Please try another\n")

                    elif int(score_position) in range(7,11) or int(score_position) > 18 or int(score_position) < 0:
                        print("\n\tYOU HAVE TO CHOOSE A VALID SCORE POSITION! Please check the scorelist\n")

                    else:
                        break
                
                except:

                    print("\n\tPLEASE, WRITE A NUMBER OF THE SCORE POSITION FROM THE PROTOCOL!\n")

        query_points(player_list, every_player, score_position)
        os.system('clear')
        print_protocol(player_list)
        

#-----------------------------------------------------------------------------  

def query_points(player_list, every_player, score_position):
    """This function is used to ask the player how much points to apply 
        to the protocol, takes three arguments, 'players', 'every_player' and 'score_position'"""

    while True: 

        try:
            score_points = int(input("How Many Points?:"))
            print("\nApply a '0' to scratch a score,")

            if score_points > 50 or score_points < 0:
                print("\tTHAT IS AN INVALID SCORE POINT, Please try again\n")

            else:
                #Applys the score on the right position that the user inputs
                player_list[every_player].scores[int(score_position) -1] = score_points
                print(" ")

                break
        
        except:
            print("\t\nPLEASE, WRITE A NUMBER OF A VALID SCORE POINT\n")      

#-----------------------------------------------------------------------------  
        
def print_protocol(player_list): 
    """This function creates the protocol and stores every player and its scores,
        takes one argument, 'players'"""

    #List of all the fixed Yatzy scores
    all_scores = ["ONES(1)  ", "TWOES(2) ","THREES(3)","FOURS(4) ", "FIVES(5) ", "SIXES(6) ",
                  "---------","BONUS    ","FIRSTSUM ","---------", "PARE(11) ", "2PARE(12)", 
                  "TRISS(13)","4ROW(14) ","S.LAD(15)","B.LAD(16)", "FULLH(17)","YATZY(18)",
                  "---------","TOTALSUM:"]
    
    print("***********************PROTOCOL************************")
    print("NAME:    ", end = "\t") 

    #Adds every player in a column 
    for display_player in player_list:
        print("%-7.6s" %display_player.name_of_player , end="\t")

    print ("\n")

    #Add all the score names in first column
    for list_scores in range(len(all_scores)): 
        print(all_scores[list_scores], end = "\t")
        
        #Applys the correct score on the correct position of the player
        for y in player_list: 
            added_score = y.scores.get(list_scores, "")

            if added_score == 0:
                added_score = "-"

            print("%-7.6s" %added_score, end = " ")
        print("")

    print("---------")
    print("=======================================================")
        
#-----------------------------------------------------------------------------


def main_looprounds(player_list):
    """This function loops the game rounds and uppdates the main player scores,
        takes one argument, 'players'"""


    #Change to how many rounds there will be played, 14 rounds is the default of a Yatzy game
    set_rounds = 14 


    for loop_rounds in range(set_rounds): #This is the main loop for the protocol of every round.

        #Runs the function for every player to input their score on the correct position   
        ask_player_score(player_list) 
        
        #Loop to apply all the score sums on the correct position
        for add_to_player in player_list: 
            
            add_to_player.first_sum() 
            add_to_player.bonus() 
            add_to_player.total_sum() 
            os.system('clear')
            print_protocol(player_list)
         
            loop_rounds += 1

#-----------------------------------------------------------------------------

def print_score_board(player_list):
    """This method is used at the end of the game to display all final scores,
        takes one argument, 'players'"""

    print("\n---SCORE BOARD---") 
    print("=================================") 

    for winner_to_loser in player_list:
        print("%-7.6s" %winner_to_loser.name_of_player ,":", end="\t")
        print(winner_to_loser.total_sum(),"P")
 
    print("=================================")   

    #Represents the winner of the game,player with highest 'total_sum'
    print("\tTHE WINNER IS:",player_list[0].name_of_player,"!!!")

#-----------------------------------------------------------------------------

        
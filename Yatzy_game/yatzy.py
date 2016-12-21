# Program (Yatzy™ Protocol) written by: ADDI DJIKIC  (2013/2014) 
# Addi 2013 KTH (Royal Institute of Technology)
# addi@kth.se

                        #------------------MAIN-------------------#
#This program is a Yatzy protocol that are set by the number of players the user chooses

from classes import* 
from defs import*  
import os

def main():
    
    os.system('clear') #clears the terminal/window
    show_welcomescreen()

    #Displays the rules of Yatzy protocol
    show_rules()

    #Allowes the user to input how many players there will be in the game
    number_of_players = input_players()

    # Calls the function to add all the joined players
    player_list = get_player_names(number_of_players)

    # Runs the function to print out the protocol 
    print_protocol(player_list)

    #Prints some remainders at the beginning of the game
    set_reminder()

    #This function loops the game rounds and updates the main player scores
    main_looprounds(player_list)
        
    # This function sort the scores from highest to lowest
    player_list.sort(key=lambda winner_to_loser: -winner_to_loser.scores[19])

    #Displays scoreboard att the end of the game 
    print_score_board(player_list)

main()


           
    
    

    



    
    
    
    

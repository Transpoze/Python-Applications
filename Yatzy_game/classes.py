# coding: latin1
# Program (Yatzy™ Protocol) written by: ADDI DJIKIC  (2013/2014) 
# Addi 2013 KTH (Royal Institute of Technology) 
# addi@kth.se


                        #------------Class and class methods------------#
class Player(object):
    def __init__(self, name_of_player):
        """Every "Player" object is in this class. With The
            attributes, 'scores' and 'name_of_player'"""

        self.scores = {} 
        self.name_of_player = name_of_player 
        
#######################ClassFunctions

    
    def total_sum(self): 
        """The final score of each player"""

        tot_sum = 0
        for get_total_sum in range(7,18):
            tot_sum += self.scores.get(get_total_sum,0)
            
        self.scores[19] = tot_sum

        return tot_sum

    
    def bonus(self):    
        """Gives every player a bonus if a certain score is reached (on position 1-6)"""

        if self.first_sum() >= 63: #The default minimum score is 63 to get a bonus
            self.scores[7] = 50 #Bonus points are set to 50 points, position '7' is the 'bonus'


        
    def first_sum(self):
        """Sums up "ones" to "sixes" (this is used to check if the player will get a bonus)"""

        sum = 0
        for get_first_sum in range(6):
            sum += self.scores.get(get_first_sum, 0)
            
        self.scores[8] = sum 

        return sum

#######################
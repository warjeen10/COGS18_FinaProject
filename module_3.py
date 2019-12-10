#this will randomly generate 50 winning numbers and store it in a varible called chosen
import random

to_choose_from = range(1,101)
number_to_choose = 50

chosen = random.chosen = random.sample(to_choose_from, number_to_choose)

#this is to create a matrix later on (that will become the 5x5 Bingocard
import numpy as np

#these are my functions:
def split_into_int(row):
    """
    calling the split_into_int function on the rrows that were created by the user
    parameters:
    row (string) = the 5 rrows that were created by the user
    
    returns:
    row = list of integers
    """ 

    row = ([int(x) for x in row.split()])
    return row

def check_for_row_repeats(row_bingo):
    """
    this function will ensure there are no repeated inputs within the same row    
    if there are repeats it will ask the user to input a unique number to replace it
    parameters:
    row_bingo (list) = the 5 rrows that were created by the user
    
    returns:
    new_list = list of unique integers
    """ 

    new_list = []
    dup_num = 0 
    for value in row_bingo:
        if row_bingo.count(value) == 2:
            if dup_num >= 1:
                new_value = input("🤭 The number {} has already been entered, please enter a number to replace it:  ".format(value) )
                new_value = int(new_value)
                new_list.append(new_value)
            else:
                new_list.append(value)
                dup_num +=1
       

        else:
            new_list.append(value)

    return new_list

def check_for_all_repeats(the_row, all_rows):
    """this function will ensure there are no repeated inputs from previous rows    
    if there are repeats it will ask the user to input a unique number to replace it
    parameters:
    the_row (list) = the 5 rrows that were created by the user
    all_rows (list) = list of all (unique) integers that were previously inputted
    
    returns:
    new_list = list of total inputs (unique integers)
    """ 
    
    new_list = []
    for value in the_row:
        if value in all_rows:
            new_value = input("🤭 The number {} has already been entered, please enter a number to replace it:  ".format(value))
            new_value = int(new_value)
            new_list.append(new_value)

        else:
            new_list.append(value)
    return new_list

def cmn_bingo(cmn_bingocard):
    """
    this function will count how many 0s there are in the columns of cmn_bingo (which will be Bingocard) 
    once it counts the 0s in each column it will add it to a list called my_cmns
    
    parameters:
    cmn_bingocard (numpy array) = a 5x5 matrix that represents the Bingocard that was created by the user
    
    returns:
    my_cmns = list of total 0s in the 5 columns
    """
    cmn1 = list(cmn_bingocard[:,0]).count(0)
    cmn2 = list(cmn_bingocard[:, 1]).count(0)
    cmn3 = list(cmn_bingocard[:, 2]).count(0)
    cmn4 = list(cmn_bingocard[:, 3]).count(0)
    cmn5 = list(cmn_bingocard[:, 4]).count(0)

    my_cmns = [cmn1, cmn2, cmn3, cmn4, cmn5]
    return my_cmns

def row_bingo(row_bingocard):
    """
    this function will count how many 0s there are in the rows of row_bingo (which will be Bingocard)
    once it counts the 0s in each column it will add it to a list called my_rows
    
    parameters:
    row_bingocard (numpy array) = a 5x5 matrix that represents the Bingocard that was created by the user
    
    returns:
    my_rows = list of total 0s in the 5 rows
    """
    row1 = list(row_bingocard[0,:]).count(0)
    row2 = list(row_bingocard[1,:]).count(0)
    row3 = list(row_bingocard[2,:]).count(0)
    row4 = list(row_bingocard[3,:]).count(0)
    row5 = list(row_bingocard[4,:]).count(0)

    my_rows =  [row1, row2, row3, row4, row5]
    return my_rows


def dia_bingo(dia_bingocard):
    """
    this function will count how many 0s there are in the rows of dia_bingocard (which will be Bingocard)
    
    short summary:
    once it counts the 0s in each diagnoals it will add it to a list called my_dias
    
    parameters:
    dia_bingocard (numpy array) = a 5x5 matrix that represents the Bingocard that was created by the user
    
    returns:
    my_dias = list of total 0s in the 5 diagonals
    """
    dia1 = list(dia_bingocard.diagonal()).count(0)
    dia2 = list(np.fliplr(dia_bingocard).diagonal()).count(0)

    my_dias = [dia1, dia2]
    return my_dias



def check_bingo(cmns, rows, dias):
    """
    this function will see if any of the columns, rows, and/or diagonals have 5 0s
    
    short summary:
    first it will put the total 0s of the rows, columns, and diagonals (information from the other functionss)
    into a list called my_power_list, then it will loop through to see if 5 is in that list
    5 0s means that a bingo is present so it will print 'BINGO!' bc the user has won"
    
    parameters:
    cmns (list) = a list of how many 0s are in the columns of bingo (will be my_cmns)
    rows (list) = a list of how many 0s are in the rows of bingo (will be my_rows)
    dias (list) = a list of how many 0s are in the diagonals of bingo (will be my_dias)
    
    returns:
    win = string '🥳 BINGO!' -- if bingo was won, if not nothing (an empty string) will be returned
    """
    win = ''
    my_power_list = cmns + rows + dias
    for item1 in my_power_list:
        if item1 == 5:
            win = win + '🥳 BINGO!'
            break
    
    print(win)


def mark_card(number, card):
    """
    this function will see if the winning numbers are present on the user's Bingocard
    short summary:
    if so it will replace the winning number with 0
    
    parameters:
    number (integer) = a list of random winning numbers (chosen) that were generated at the beginning of the game
    card (numpy array) = a 5x5 matrix that represents the Bingocard that was created by the user
    
    returns:
    True = string '🥳 BINGO!', if bingo was won
    False = break out of the loop, if bingo was not won
    """
    for row in range(5):    
            for clm in range(5):
                if number == card[row][clm]:
                    print('You have the winning number {}! So we\'ll mark it with {}  '.format(card[row][clm], 0))
                    card[row][clm] = 0

                    val4 = input("Type Go to mark that winning number ")
                    if val4 == "Go" or val4 == "go" or val4 == "Go " or val4 == "go ":
                        print(card)

                        all_cmns = cmn_bingo(card)

                        all_rows = row_bingo(card)

                        all_dias = dia_bingo(card)
                        
                        
                        val_5 = check_bingo(all_cmns, all_rows, all_dias)
                        
                        if val_5 == "🥳 BINGO!":
                            break                        
                        
                        else:
                            return False
                        
    return False



def play_game():
    #instructions on how to create the bingocard
    val = input("Type the word Begin in the box to play: ")
    #using or statements to account for user inputs: Begin, begin, space after Begin, or space after begin
    if val == "Begin" or val == "begin" or val == "Begin " or val == "begin ":

        total_user_inputs = []
        print("Now we will begin creating your very own bingo card!")

        #the user will now input 5 numbers that will become the first row of BingoCard
        print("Now enter five numbers within the range of 1-100 to represent the first row of your BingoCard, BE SURE TO SEPARATE USING ONLY A SPACE FOR EX-- 1 2 3 4 5: ")
        rrow1 = input()
        rrow1 = split_into_int(rrow1)

        #this is ensure the user inputs 5 numbers (no more, no less)
        while len(rrow1) != 5:
            rrow1 = input('🥺 Please put 5 numbers down')
            break


        #this for loop is to ensure that there are no repeated input values
        new_rrow1 = check_for_row_repeats(rrow1)

        total_user_inputs = total_user_inputs + new_rrow1






         #the user will now input 5 numbers that will become the 2nd row of BingoCard
        print("Now enter the second row of your BingoCard")
        rrow2 = input()
        rrow2 = split_into_int(rrow2)


            #this is ensure the user inputs 5 numbers (no more, no less)
        while len(rrow2) != 5:
            rrow2 = input('🥺 Please put 5 numbers down')
            break

        #the function check_for_row_repeats is called to ensure that there are no repeated input values within the row
        new_rrow2 = check_for_row_repeats(rrow2)

        #the function check_for_all_repeats is called to ensure that there are no repeated input values from previous rows
        new_rrow2 = check_for_all_repeats(rrow2, total_user_inputs)

        total_user_inputs = total_user_inputs + new_rrow2






         #the user will now input 5 numbers that will become the 3rd row of BingoCard
        print("**READ ME** If you would like a **Free Space** use 0 as your third input")
        rrow3 = input()
        rrow3 = split_into_int(rrow3)


        while len(rrow3) != 5:
            rrow3 = input('🥺 Please put 5 numbers down')
            break

        new_rrow3 = check_for_row_repeats(rrow3)
        new_rrow3 = check_for_all_repeats(rrow3, total_user_inputs)

        total_user_inputs = total_user_inputs + new_rrow3






         #the user will now input 5 numbers that will become the 4th row of BingoCard
        print("Now enter the fourth row of your BingoCard")
        rrow4 = input()
        rrow4 = split_into_int(rrow4)


        while len(rrow4) != 5:
            rrow4 = input('🥺 Please put 5 numbers down')
            break

        new_rrow4 = check_for_row_repeats(rrow4)
        new_rrow4 = check_for_all_repeats(rrow4, total_user_inputs)

        total_user_inputs = total_user_inputs + new_rrow4






         #the user will now input 5 numbers that will become the 5th row of BingoCard
        print("Now enter the fifth row of your BingoCard")
        rrow5 = input()
        rrow5 = split_into_int(rrow5)


        while len(rrow5) != 5:
            rrow5 = input('🥺 Please put 5 numbers down')
            break

        new_rrow5 = check_for_row_repeats(rrow5)
        new_rrow5 = check_for_all_repeats(rrow5, total_user_inputs)

        total_user_inputs = total_user_inputs + new_rrow5


    #this will create the bingo card
    Bingocard = np.array([new_rrow1, new_rrow2, new_rrow3, new_rrow4, new_rrow5])



    val2 = input("Type See to see your BingoCard:  ")
    potential_see_inputs = ["See", "see","See ", "see "]
    if val2 in potential_see_inputs:
        print(Bingocard)
        print("Nice Job! Now let's see if you can get Bingo!")
    else:
        val2 = input("Please type See")
        print(Bingocard)
        print("Nice Job! Now let's see if you can get Bingo!")





    won = False
    for number in chosen:
        won = mark_card(number, Bingocard)

        if won:
            print("🥳 BINGO!")
            break

    if won == False:
        print("☹ Sorry you lost... please try again another time")
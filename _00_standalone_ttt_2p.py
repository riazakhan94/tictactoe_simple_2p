

#%%
import time
from itertools import combinations
import sys


#%% 
def any_key_proceed():
    input("Press any key to proceed ... ")




#%%
def print_status(x):
    print("")

    print(f"\t\t| {x[0]} | {x[1]} | {x[2]} |")
    #print("\t---------------------")
    print(f"\t\t| {x[3]} | {x[4]} | {x[5]} |")
    #print("\t---------------------")
    print(f"\t\t| {x[6]} | {x[7]} | {x[8]} |")

    



#%%
# this function prompts a player (p)
# to give the next input from available options (alist)



def player_input(p, alist, symbol):
    print("----------------------------------------------")
    print(f"{p}, select the position you want to occupy")
    print("----------------------------------------------")
    print(f"Your symbol : {symbol}" )
    print(f"Available positions are : {str(alist)[1:-1]} ")
    tmp_sts = 0
    while tmp_sts == 0:
        try:
            x = input("Select position : ")
            x = int(x)
            tmp_sts = 1
            if not (x in alist):
                raise ValueError("Invalid input, try again ...")
                tmp_sts = 0
        except ValueError:
            print("Invalid input, try again ...")
            tmp_sts = 0
    print("\n----------------------------------------------")
    return(x)
                
            
#k = player_input("Tom", [1,2, 4])
    




#%%

# this function takes the list of numbers 
# that a palyer occupies and determines if he won already!
# return: logical (True or False)
def did_player_win(player_list):
    if(len(player_list) < 3):
        return(False)
    
    grand_list = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}] + \
        [{0, 3, 6}, {1, 4, 7}, {2, 5, 8}] + \
            [{0, 4, 8}, {6, 4, 2}]
    

    all_comb = list(combinations(player_list, 3) )
    tmp_n_comb = len(all_comb)
    for i in range(0, tmp_n_comb):
        if set(all_comb[i]) in grand_list: # if mathces 
            return(True) # then return
    return(False)

#print(did_player_win([9, 2, 7, 8]))




#%%

def welcome_note():
    print("=========================================")
    print("=========================================")
    print(">>> Welcome to the Tic Tac Toe")
    print("=========================================")
    time.sleep(2)
    print("================ RULES ==================")
    time.sleep(1)
    print("Classical Tic Tac Toe rules! No surprise...\n"
    " Two players play agaianst each other.\n"
    " Player 1 gets to select first with 'X' and\n"
    " Player 2's symbol is 'O'.\n")
    time.sleep(2)
    print("=========================================")
    time.sleep(1)
    any_key_proceed()






#%% 

def winner_note(winner):
    print("*****************************************")
    print(f">>>>>  Winner is : {winner}")
    time.sleep(2)
    print(f"***** CONGRATULATIONS {winner}!")
    time.sleep(2)
    return()



#%% 

def draw_note(p1, p2):
    print("*****************************************")
    print(">>>>>  It's a DRAW!!!")
    time.sleep(2)
    print(f"***** Nice competition {p1} and {p2}")
    time.sleep(1)
    print("*****************************************")
    return()



#%% 
def input_pnames():
    print("----------------------------------------------")
    print(">>>> Players <<<<")
    print("----------------------------------------------")
    p1 = input("Player 1 name : ")
    p2 = input("Player 2 name : ")
    print("----------------------------------------------")
    print("Saving player names (thanks for patience) ...")
    time.sleep(1.5)
    print(f">>> Player {p1} and {p2} are saved successfully.") 
    print("----------------------------------------------")
    return(p1, p2)



#%%
def game_close():
    print("\n \n")
    time.sleep(2)
    print(" >>>>>> Thanks for playing the game <<<<<<")
    time.sleep(2)
    print(" >>>>>> ..... Have a good day ..... <<<<<<")
    time.sleep(2)
    print(" >>>>>> Closing program in a few seconds ...")
    time.sleep(4)
    sys.exit()


#%% 

# Main call
welcome_note()
p = input_pnames()
p1 = p[0]
p2 = p[1]

winner = "None"
result_sts = 0

# master list for printing
alist_print = list(range(0,9))
symbol_list = [" "] * 9
# available list of postions - dynamic change
alist = list(range(0,9))
# list for two players
p1_list = []
p2_list = []
# how many postions are occupied in real time
tmp_count = 0



print("------------------------------------------")
print(" >>> All set. The game starts now ....")
print("------------------------------------------\n\n\n")

time.sleep(2)



while True:
    if tmp_count == 9:
        break
    print("-----------------------------------")
    print(">>>>>>  Available positions <<<<<<")
    print_status(alist_print)
    
    print("-----------------------------------")
    print(">>>>>>  Current standings <<<<<<")
    print_status(symbol_list)
    
    
    
    tmp_pos = player_input(p1, alist, "X")
    #time.sleep(1)
    print(f">>> Saving {p1}'s response ...")
    #time.sleep(1)
    print(f">>> {p1}'s repsonse saved")
    time.sleep(1)
    alist_print[tmp_pos] = " "
    symbol_list[tmp_pos] = "X"
    p1_list = p1_list + [tmp_pos]
    alist.remove(tmp_pos)
    tmp_count = tmp_count + 1
    if tmp_count > 4:
        tmp_won = did_player_win(p1_list)
        if tmp_won:
            winner = p1
            time.sleep(2)
            print("-----------------------------------")
            print(" >>>>>>>  GAME OVER <<<<<<<<")
            print("-----------------------------------")
            time.sleep(2)
            print(" >>>>>>>  FINAL STATUS <<<<<<<<")
            print_status(symbol_list)
            print("-----------------------------------")
            time.sleep(2)
            break
    
    
    if tmp_count == 9:
        break
    
    print("-----------------------------------")
    print(">>>>>>  Available positions <<<<<<")
    print_status(alist_print)
    
    print("-----------------------------------")
    print(">>>>>>  Current standings <<<<<<")
    print_status(symbol_list)
    
    tmp_pos = player_input(p2, alist, "O")
    #time.sleep(1)
    print(f">>> Saving {p2}'s response ...")
    #time.sleep(1)
    print(f">>> {p2}'s repsonse saved")
    time.sleep(1)
    alist_print[tmp_pos] = " "
    symbol_list[tmp_pos] = "O"
    p2_list = p2_list + [tmp_pos]    
    alist.remove(tmp_pos)
    tmp_count = tmp_count + 1
    if tmp_count > 4:
        tmp_won = did_player_win(p2_list)
        if tmp_won:
            winner = p2
            time.sleep(2)
            print("-----------------------------------")
            print(" >>>>>>>  GAME OVER <<<<<<<<")
            print("-----------------------------------")
            time.sleep(2)
            print(" >>>>>>>  FINAL STATUS <<<<<<<<")
            print_status(symbol_list)
            print("-----------------------------------")
            time.sleep(2)
            break



if winner == "None":
    time.sleep(2)
    draw_note(p1, p2)
    
else:
    winner_note(winner)



game_close()
    
    

    
















# -------Stone Paper Scissor Game------
import random

player_wins = True
tie = True
round = 1
p_init = 0
c_init = 0
lst = ["Stone","Paper","Scissor"]

def Counter():
    global p_init
    global c_init
    if(player_wins):
        p_init += 1
    elif(player_wins != True):
        c_init += 1
    print("You :",p_init,"            Computer :",c_init)

def Result():
    # if(player!=lst[0] and player!=lst[1] and player!=lst[2]):
        # continue
    if(tie):
        print("Round Tied")
    elif(player_wins):
        print("You won")
    elif(player_wins != True):
        print("Computer won")

def final_counter():
    global p_init
    global c_init
    print("\nFinal Results----->")
    print("You :",p_init,"            Computer :",c_init)
    if(p_init == c_init):
        print("Game Drawn")
    elif(p_init > c_init):
        print("You won the Game!!\n")
    else:
        print("Sorry to say, but You are a LOSER\n")



    
    
    
    
print("\nLet's begin the STONE PAPER SCISSOR Game--------------->")
while(round <= 5):
    
    print("\nRound",round)
    computer = random.choice(lst)
    player = input("Stone Paper Scissor..Shoot \n")
    print("You :",player,"        Computer :",computer)

    if(player!=lst[0] and player!=lst[1] and player!=lst[2]):
        print("Incorrect choice entered")
        print("Reapeating this Round...")
        continue
        
        
    elif(player==computer):
        tie = True
        # Since when tie, player_wins= True, Hence in Counter p_init = +1, therefore i decreased p_init by 1
        p_init -= 1
        # print("Round Tied")
    elif(player=="Stone" and computer=="Paper"):
        player_wins = False
        tie = False
        # print("Computer won")   
    elif(computer=="Stone" and player=="Paper"):
        player_wins = True
        tie = False
        # print("You won")
    elif(player=="Paper" and computer=="Scissor"):
        player_wins = False
        tie = False
        # print("Computer won")
    elif(computer=="Paper" and player=="Scissor"):
        player_wins = True
        tie = False
        # print("You won")
    elif(player=="Scissor" and computer=="Stone"):
        player_wins = False
        tie = False
        # print("Computer won")
    elif(computer=="Scissor" and player=="Stone"):
        player_wins = True
        tie = False
        # print("You won")

    
    Result()
    Counter()
    player_wins = True
    tie = True
    round += 1
final_counter()


# Finally working properly
    
    


    








import random
key = random.randint(10,99)

print("Guess the number in 7 or less number of guesses")
print("Hint: Its a 2 digit number")
for i in range(1,8):

    
    n = int(input())
    if(n==key):
        print("Perfect Guess!")
        break
    elif(n>key):
        print("Go low")
        print("Guess left: ",7-(i))
    elif(n<key):
        print("Go high")
        print("Guess left: ",7-(i))
    
    

    else:
        print("Error. Start again")
if(i==7 and n!=key):
    print("Hard luck, Try again!")
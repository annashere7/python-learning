
''' 
1 for snake
-1 for water
0 for gun
'''
import random
computer =random.choice([1, -1, 0])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
revDict={1:"snake",-1:"water",0:"gun"}


you=youDict[youstr]
print(f" you chose  {revDict[you]} \n computer chose {revDict[computer]}")
if computer == 1 and you == -1:
    print("You win")
elif computer == -1 and you == 1:
    print("You lose")
elif computer == 0 and you == 1:
    print("You win")
elif computer == 1 and you == 0:
    print("You lose")
elif computer == -1 and you == 0:
    print("You win")
elif computer == you:
    print("tie")
else:
    print("something went wrong")

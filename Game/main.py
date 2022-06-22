import random

def game(comp , you,c,y,countyou,countcomp,countyou1,countcomp1 ):
    c=0
    y=0
    if comp == 3:
        if you== '2':
          c=1
        elif you=='1':
         y=1
        else:
         c=0
         y=0

    elif comp == 2:
        if you== '1':
           c=1
        elif you=='3':
            y=1
        else:
         c=0
         y=0

    elif comp == 1:
        if you== '3':
          c=1
        elif you=='2':
          y=1
        else:
         c=0 
         y=0
    
    if c==0 and y==0 : 
       print("The game is tied")
    elif y==1:
       print("You won the game")
       countyou1 = countyou1 + 1
    elif c==1:
       print("You lost the game")
       countcomp1 = countcomp1 + 1    
    m = int(input(" enter 0 to exit the game or 1 to continue :"))
    if(m==1):
       comp= input("computer Turn : Stone(1) Paper(2) or Scissor(3) ? ")
       randno = random.randint(1,3)
       comp = randno
       you= input("player's Turn : Stone(1) Paper(2) or Scissor(3) ? ")
       print(f"Computer chose {comp}")
       print(f"you chose {you}")
       game(comp , you,0,0,0,0,countyou1,countcomp1)
    else:
       print(" your score is  "+  str(countyou1)+ " and computer's score is  "+str(countcomp1))
       

countyou1=0
countcomp1 =0
comp= input("computer Turn : Stone(1) Paper(2) or Scissor(3) ? ")
randno = random.randint(1,3)
comp = randno
you= input("player's Turn : Stone(1) Paper(2) or Scissor(3) ? ")
print(f"Computer chose {comp}")
print(f"you chose {you}")
game(comp , you,0,0,0,0,0,0)


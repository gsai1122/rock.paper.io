import random 
while True:
    x =input("chouse rock,paper or scissors")
    y = random.randint(1,3)
    if x == "rock":
        x_num = 1
    elif x == "paper":
        x_num = 2
    elif x == "scissors":
        x_num = 3
    else:
        print("Invalid input. Try again.")
        continue
    words = {
        1:"rock",
        2:"paper",
        3:"scissors"
}
    
    print("Computer chose:", words[y])
    if x_num ==1 and y == 2:            #rock and paper 
        print("u lost bitch")
    elif x_num==1 and y==3:             #rock and scissors
        print("u won")
    elif x_num==1 and y==1:
        print("u tied fuck")        #rock and rock
    elif  x_num==2 and y==1:            #paper and rock
        print("you won hehe")
    elif x_num==2 and y==2:             #paper and paper 
        print("u tied it ohhhhh")
    elif  x_num==2 and y==3:            #paper and scissors
        print("u lost booooo")
    elif x_num==3 and y==1:             #scissors and rock 
       print("u lost")
    elif x_num==3 and y==2:
        print("u won")              #scissors and paper 
    elif x_num==3 and y==3:
        print("u tied bruhhh")      #scissors and scissors
    else:
        print("wtf its a rock paper scissor game")
        
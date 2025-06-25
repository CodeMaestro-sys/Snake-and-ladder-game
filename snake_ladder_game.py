import random
def board_game():#Making of board for snake-ladder game
    rows=10
    columns=10
    num=1
    board=[]
    for i in range(rows):
        row=[]
        if(i%2==0):
            for j in range(columns):
                row.append(num)
                num=num+1
        else:
            for i in range(columns):
                row.insert(0,num)
                num=num+1
        board.insert(0,row)
    for row in board:
        print(row)
def game():
    board_game()
    ladder={1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
    snakes={32:10,36:6,48:26,62:18,88:24,95:56,97:78}
    player1=input("Enter your name=")
    print("Player1 is ",player1)
    player2="Computer"
    print("Player2 is" ,player2)
    pos={player1:0,player2:0}
    while True:
        print("Turn of Player1")
        dice_roll=random.randint(1,6)
        print("Your number is",dice_roll)
        new_pos=pos[player1]+dice_roll
        if(new_pos>100):
            print("You stay at",pos[player1],"as roll exceed 100")
        else:
            pos[player1]=new_pos
            print("Your new position is",new_pos)
            if(new_pos in ladder):
                new_pos=ladder[new_pos]
                print("After climbing the ladder your new position is",new_pos)
                pos[player1]=new_pos
            elif(new_pos in snakes):
                new_pos=snakes[new_pos]
                print("After getting bitten by snake your new position is",new_pos)
                pos[player1]=new_pos
        if(pos[player1]==100):
                print("Congratulations!",player1,",you won the game")
                break
        print("----------+------+-------+----------")
        print("Turn of player2")
        dice_roll_2=random.randint(1,6)
        print("Your number is",dice_roll_2)
        new_pos_2=pos[player2]+dice_roll_2
        if(new_pos_2>100):
            print("You stay at ",pos[player2],"as roll exceed 100 ")
        else:
            pos[player2]=new_pos_2
            print("Your new position is",new_pos_2)
            if(new_pos_2 in ladder):
                new_pos_2=ladder[new_pos_2]
                print("After climbing the ladder your new position is",new_pos_2)
                pos[player2]=new_pos_2
            elif(new_pos_2 in snakes):
                new_pos_2=snakes[new_pos_2]
                print("After getting bitten by snake your new position is",new_pos_2)
                pos[player2]=new_pos_2
        if(pos[player2]==100):
                print("Congratulations!",player2,",you won the game")
                break
        print("Final position of player1 is=",pos[player1])
        print("Final position of player2 is=",pos[player2])

        ans=input("Do you want to play again(Y/N)?").capitalize()
        if(ans=="N"):
            break
    print("Thanks for playing")


game()



        
             



        
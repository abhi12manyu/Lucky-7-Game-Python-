


#import files for random
from random import *
user=0
comp=0
#Display the game title and brief introduction of the game
def intro():
    print('\n\t\t\t\t\t\t\t\t WELCOME TO LUCKY 7 GAME\n\nThe game uses 2 random fuctions to predict a random no from 1 to 6 and adds them both which exactly stmulates the throwing of 2 dice and ading their total.\nThe user predicts the sum to be less than 7 as DOWN or more than 7 as UP or 7 as Number 7.If predicted choice is showed then user wins else loose.\n\n\tScore Logic : The score is calculated by the following logic\n\t\tLess than 7 : Money Bet\n\t\tMore than 7 : Money Bet\n\t\tNumber 7    :  3 Times Money Bet\n\n')

#Genrates a random number
def generate():
    return(randint(1,6)+randint(1,6))

#Takes inputs by the user such as points(money bet) and choice(Down/7/Up) 
def inputbyuser():
    global points,choice
    points=int(input('\nHow much would you like to bet? Rs '))
    choice=int(input('1) DOWN \t 2)NUMBER 7 \t 3) UP \nYour Choice (1/2/3) : '))

#Check if user's win by comparing random no with user's choice and display result
def check(choice):
    Rn=generate()
    global res
    if ((choice==1 and Rn<7) or (choice==3 and Rn>7) or (choice==2 and Rn==7)):
        res='Win'
    else:
        res='Loose'

    print('Random Number : ',Rn)
    print('You ',res)

#Display user's and computer's score
def score(points,res,choice):
    global user
    global comp
    if choice==2:
        if res=='Win':
            user= user+3*points
        else:
            comp=comp+3*points
    else:
        if res=='Win':
            user=user+points
        else:
            comp=comp+points

    print('SCORE\nYour : ',user,'     Computer : ',comp)

#Handles sequence of events
def main():
    intro()
    con='yes'
    while(con=='Yes' or con=='yes'):
        inputbyuser()
        check(choice)
        score(points,res,choice)
        con=input('Contiinue? Yes or No : ')
    else:
        if(con=='No'or con=='no'):
            if(comp-user>0):
                print('\nYou lose Rs ',comp-user)
            elif(comp-user<0):
                print('\nYou won Rs ',user-comp)
            else:
                print('\nTie Match')
        else:
            print('\nInvalid input')


#Program begins here
main()


from random import randint, random

number = randint(1,9)

guess = int(input("Guess a number: "))
chances = 0

while chances < 5:
    print("chances", chances)
    if(guess == number):
     print("Your guess was right! Congratulations!!")
     break
    elif(guess < number):
       print("You are too close! The number is at your head!")
       break
    elif(guess > number):
        print("You are too near! The number is at your feet!")
        break
    chances = chances+1
    

if not chances < 5:
    print("You lose! The number is ", number)
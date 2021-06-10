# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:28:52 2021

@author: matth
"""
from random import randint

def guess_game():
    rand = randint(1,20)
    guess = 0
    
    while guess != rand:
        guess = int(input('Guess the number: '))
        if guess < rand:
            print('your number is lesser than actual')
        elif guess > rand:
            print('your number is greater than actual')
    else:
        print('Congrats!')

guess_game()
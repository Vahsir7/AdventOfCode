# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:43:27 2023

@author: RISHAV

https://adventofcode.com/2023/day/2
Cube Conundrum
"""
actual_ball=[12,14,13]
"""
    function check_ball

    Parameters:
    - line: original string from the file
    - ball: the ball whose number is to be checked

    Returns:
    max number of balls of the given color in the given string

    Example:
    ```
    result = my_function(Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green; red)
    print(result)

    result = 4
    ```
"""
def check_ball(line,ball):
    numbers=[]
    index=line.index(':')
    #number of red balls
    x=s[index:]
    offset=len(ball)
    while ball in x:
        index=x.index(ball)-2
        #print(index)
        #print(s[index])
        number_of_balls=""
        while x[index]!=' ':
            #print(x[index])
            number_of_balls=x[index]+number_of_balls
            index-=1
        number_of_balls=int(number_of_balls)
        #print(number_of_balls)
        numbers.append(number_of_balls)
        x=x[x.index(ball)+offset:]
    return max(numbers)
ADD=0
with open(r'D:\Coding\AdventOfCode\2023\Dec2input.txt', 'r', encoding='utf-8') as file:

    for s in file:
        s=s.strip()
        #print("test0")
        index=s.index(':')
        GameNumber=s[5:index]
        power=[]
        gamePower=1
        for i in ["red","blue","green"]:
            power.append(check_ball(s,i))
        for i in power:
            gamePower*=i
        ADD+=gamePower

print(ADD)

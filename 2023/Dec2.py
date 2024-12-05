# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:43:27 2023

@author: RISHAV

https://adventofcode.com/2023/day/2
Cube Conundrum
"""
actual_red_balls=12
actual_blue_balls=13
actual_green_balls=14

s=""
add=0
while s!='\n':
    
    try:
        #print("test0")
        s=input()
        index=s.index(':')
        GameNumber=s[5:index]
        
        
        game=True

        while(game==True):
            #number of red balls
            index=s.index(':')
            x=s[index:]
            while("red" in x):
                index=x.index("red")-2
                #print(index)
                #print(s[index])
                number_of_balls=""
                while(x[index]!=' '):
                    #print(x[index])
                    number_of_balls=x[index]+number_of_balls
                    index-=1
                number_of_balls=int(number_of_balls)
                #print(number_of_balls)
                if(number_of_balls>actual_red_balls):
                    game=False
                x=x[x.index("red")+3:]
                
            #number of blue balls
            index=s.index(':')
            x=s[index:]
            while("blue" in x):
                index=x.index("blue")-2
                #print(index)
                #print(s[index])
                number_of_balls=""
                while(x[index]!=' '):
                    #print(x[index])
                    number_of_balls=x[index]+number_of_balls
                    index-=1
                number_of_balls=int(number_of_balls)
                #print(number_of_balls)
                if(number_of_balls>actual_blue_balls):
                    game=False
                x=x[x.index("blue")+4:]
            
            #number of green balls
            index=s.index(':')
            x=s[index:]
            while("green" in x):
                index=x.index("green")-2
                #print(index)
                #print(s[index])
                number_of_balls=""
                while(x[index]!=' '):
                    #print(x[index])
                    number_of_balls=x[index]+number_of_balls
                    index-=1
                number_of_balls=int(number_of_balls)
                #print(number_of_balls)
                if(number_of_balls>actual_green_balls):
                    game=False
                x=x[x.index("green")+5:]
            if(game==False):
                break
            else:
                print(GameNumber)
                add=add+int(GameNumber)
            game=False
        #print(number_of_balls)





    except EOFError:
        break
print(add)

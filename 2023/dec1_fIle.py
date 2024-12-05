"""
https://adventofcode.com/2023/day/1
trebuchet problem
"""


add=0
num={"one":'o1ne',"two":'t2wo',"three":'th3ree',"four":'fo4ur',"five":'fi5ve',"six":'s6ix',"seven":'se7ven',
            "eight":'ei8ght',"nine":'ni9ne'}



with open(r'D:\Coding\AdventOfCode\2023\input.txt', 'r', encoding='utf-8') as file:

    for line in file:

        line=line.strip()

        x=y=0
        for key, value in num.items():  #replacing the string
            line=line.replace(key,value)


        #counting the tens digit
        count=0
        while(line[count].isdigit()==False):
            count+=1
        x=int(line[count])

        #counting the ones digit
        count=len(line)-1
        while(line[count].isdigit()==False):
            count-=1
        y=int(line[count])

        add=add+int(x*10+y)


print(add)
        
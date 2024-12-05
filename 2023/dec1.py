"""
https://adventofcode.com/2023/day/1
trebuchet problem
"""

s=""
add=0
while s!='\n':
    #print("test0")
    try:

        s=input()

        num={"one":'o1ne',"two":'t2wo',"three":'th3ree',"four":'fo4ur',"five":'fi5ve',"six":'s6ix',"seven":'se7ven',
            "eight":'ei8ght',"nine":'ni9ne'}
        
        x=y=0
        s2 = s #copy of s

        for key, value in num.items():  #replacing the string
            s2=s2.replace(key,value)
        #
        count=0
        while(s2[count].isdigit()==False):
            count+=1
        x=int(s2[count])
        #print(x)


        #counting the ones digit
        count=len(s2)-1
        while(s2[count].isdigit()==False):
            count-=1
        y=int(s2[count])
        #print(y)

        add=add+int(x*10+y)
        #print(x,y,sep="")

    except EOFError:
        break


print(add)
    
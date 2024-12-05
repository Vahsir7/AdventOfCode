"""
https://adventofcode.com/2023/day/3
trebuchet problem
"""

s=""
add=0
while s!='\n':
    #print("test0")
    try:
        s=input()
        symbol="!@#$%^&*()/\|{}[]<>?~`+=,.;:'\""

    except EOFError:
        break

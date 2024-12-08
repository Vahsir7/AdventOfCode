def check(input_string):
    # Define states
    state = "S0"
    ans = 0
    # Process each character in the input string
    input_string = input_string.strip().lower()
    #for char in input_string:
    for index, char in enumerate(input_string):
        if state == "S0": #check m
            a = ""
            b = ""
            if char == "m":
                state = "S1"
            else:
                state = "S0"  # Restart

        elif state == "S1": #check u
            if char == "u":
                state = "S2"
            else:
                state = "S0"  # Restart

        elif state == "S2": #check l
            if char == "l":
                state = "S3"
            else:
                state = "S0"  # Restart

        elif state == "S3": #check (
            if char == "(":
                state = "S4"
            else:
                state = "S0"  # Restart

        elif state == "S4": #first number and go from ,
            if char.isdigit():
                a += char
                state = "S4"  # Continue reading the first number
            elif char == ",":
                state = "S5"
            else:
                state = "S0"  # Restart

        elif state == "S5":
            if char.isdigit():
                state = "S5"  # Continue reading the second number
                b += char
            elif char == ")":
                #print(a,b)
                if a!='' and b!='':
                    ans+=int(a)*int(b)
                else:
                    ans+=0
                state = "S0"
            else:
                state = "S0"  # Restart 
        
        

    
    return ans

with open('input.txt') as f:
    lines = f.readlines()
    ans = 0
    for line in lines:
        ans += check(line)
    print(ans)
        

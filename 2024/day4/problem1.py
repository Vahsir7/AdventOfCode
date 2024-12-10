def vertical(line1, line2, line3, line4):
    ans = 0
    l = len(line1)
    for i in range(l):
        if (line1[i] == 'X' and line2[i] == 'M' and line3[i] == 'A' and line4[i] == 'S') or \
           (line1[i] == 'S' and line2[i] == 'A' and line3[i] == 'M' and line4[i] == 'X'):
            ans += 1
    #if ans!=0:
    #   print("Vertical matches:", ans)
    return ans

def horizontal(line):
    ans = 0
    l = len(line)
    for i in range(l - 3):  # Check every substring of length 4
        if line[i:i+4] == "XMAS" or line[i:i+4] == "SAMX":
            ans += 1
    #if ans!=0:
     #   print("Horizontal matches:", ans)
    return ans

def Ldiagonal(line1, line2, line3, line4):
    ans = 0
    l = len(line1)
    for i in range(l - 3):  # Ensure no out-of-bounds
        if (line1[i] == 'X' and line2[i+1] == 'M' and line3[i+2] == 'A' and line4[i+3] == 'S') or \
           (line1[i] == 'S' and line2[i+1] == 'A' and line3[i+2] == 'M' and line4[i+3] == 'X'):
            ans += 1
    return ans

def Rdiagonal(line1, line2, line3, line4):
    ans = 0
    l = len(line1)
    for i in range(3, l):  # Start from index 3 for reverse diagonals
        if (line1[i] == 'X' and line2[i-1] == 'M' and line3[i-2] == 'A' and line4[i-3] == 'S') or \
           (line1[i] == 'S' and line2[i-1] == 'A' and line3[i-2] == 'M' and line4[i-3] == 'X'):
            ans += 1
    return ans

# Reading the input file
with open('input.txt') as f:
    lines = [line.strip().upper() for line in f]  # Clean and standardize input
    ans = 0
    l = len(lines)
    
    for i in range(l - 3):  # Process sets of 4 consecutive lines
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        line4 = lines[i+3]
        
        ans += vertical(line1, line2, line3, line4)
        #ans += horizontal(line1) + horizontal(line2) + horizontal(line3) + horizontal(line4)
        ans += Ldiagonal(line1, line2, line3, line4)
        ans += Rdiagonal(line1, line2, line3, line4)
    for i in range(l):  
        ans += horizontal(lines[i])

    print("Total matches:", ans)

def mas(line1, line2, line3):
    # SHAPE IS
    # M.S
    # .A.
    # M.S
    ans = 0
    l = len(line1)
    for i in range(l - 2):  # Ensure we don't go out of bounds
        if (
            (line1[i] == 'M' and line1[i + 2] == 'S' and 
             line2[i + 1] == 'A' and 
             line3[i] == 'M' and line3[i + 2] == 'S') 
             or
            (line1[i] == 'S' and line1[i + 2] == 'M' and
             line2[i + 1] == 'A' and
             line3[i] == 'S' and line3[i + 2] == 'M') 
             or
            (line1[i] == 'S' and line1[i + 2] == 'S' and
             line2[i + 1] == 'A' and
             line3[i] == 'M' and line3[i + 2] == 'M') 
             or
            (line1[i] == 'M' and line1[i + 2] == 'M' and
             line2[i + 1] == 'A' and
             line3[i] == 'S' and line3[i + 2] == 'S')g
        ):
            ans += 1
    return ans

with open('input.txt') as f:
    lines = [line.strip().upper() for line in f]
    ans = 0
    l = len(lines)
    print("Input Lines:", lines)
    for i in range(l - 2):  # Iterate through sets of 3 consecutive lines
        line1 = lines[i]
        line2 = lines[i + 1]
        line3 = lines[i + 2]
        ans += mas(line1, line2, line3)

    print("Total matches:", ans)

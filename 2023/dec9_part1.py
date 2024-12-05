def extrapolate_left(a):
    b=[a[i]-a[i-1] for i in range(1,len(a))]
    #print()
    #print(a)
    #print(b)
    if all(x==b[0] for x in b):
        return(a[0]-b[0])
    else:
        return (a[0]-extrapolate_left(b))

def extrapolate_right(a):
    b=[a[i]-a[i-1] for i in range(1,len(a))]
    #print()
    #print(a)
    #print(b)
    if all(x==b[0] for x in b):
        return(b[-1]+a[-1])
    else:
        return (a[-1]+extrapolate_right(b))

input_file_path = r"D:\Coding\AdventOfCode\2023\dec9input.txt"
with open(input_file_path, "r", encoding="utf-8") as f:
    sum_part1=0
    sum_part2=0
    for line in f:
        line=line.split(" ")
        line=[int(x) for x in line]
        sum_part1+=extrapolate_right(line)
        sum_part2+=extrapolate_left(line)
print(sum_part1)
print(sum_part2)
input_file_path = r"D:\Coding\AdventOfCode\2023\dec6input.txt"
with open (input_file_path, "r",encoding="utf-8") as file:
    line=file.readline().strip()
    times = line[line.index(":")+1:].strip()
    times=list(map(int,times.split()))
    
    line=(file.readline().strip())
    distance = line[line.index(":")+1:].strip()
    distance=list(map(int,distance.split()))
    start=end=0
    mul=1
    for i,time in enumerate(times):
        #print("highscore",distance[i])
        #print("Given time",time)
        for j in range(1,time):
            #print("time",j,"distance",(time-j)*j)
            if((time-j)*j>distance[i]):
                start=j
                break
        #print("start",start)
        for j in range(time-1,0,-1):
            #print("time",j,"distance",(time-(j))*j)
            if((time-j)*j>distance[i]):
                end=j+1
                break
        #print("end",end)    
        print(end-start)
        mul*=(end-start)
    print(mul)
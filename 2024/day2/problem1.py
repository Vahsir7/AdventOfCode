def is_valid(report):
    prev = report[0]
    curr = report[1]
    flag = -1

    # Determine the initial trend (ascending or descending)
    if curr - prev in [1, 2, 3]:
        flag = 1  # ascending
    elif prev - curr in [1, 2, 3]:
        flag = 2  # descending
    else:
        flag = -1  # neither

    prev = curr
    for index, curr in enumerate(report[2:], start=2):  
        if flag == -1:
            return False,index
        else:
            if flag == 1 and (curr - prev not in [1, 2, 3]):
                flag = -1
                return False,index
            elif flag == 2 and (prev - curr not in [1, 2, 3]):
                flag = -1
                return False,index
        prev = curr

    if flag != -1:
        return True,-1
    #return len(report)


with open ('input.txt', 'r') as file:
    data = file.read().splitlines()
    l = len(data)
    s=0
    for i in range(l):
        line = data[i].strip()  # Remove leading/trailing whitespace
        if not line:  # Check if the line is empty
            continue
        report = list(map(int,data[i].split(' ')))
        #print (report )
        if is_valid(report)[0]:
            s+=1
    print(s)


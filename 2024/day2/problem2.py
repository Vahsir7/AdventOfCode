def is_valid(report):
    prev = report[0]
    curr = report[1]
    flag = -1

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


def is_super_valid(report):
    if is_valid(report)[0]:
        return True
    else:
        for i in range(len(report)):
            if is_valid(report[:i]+report[i+1:])[0]:
                return True
        return False
    
answers = []
with open ('input.txt', 'r') as file:
    data = file.read().splitlines()
    l = len(data)
    s=0
    s2=0
    for i in range(l):
        line = data[i].strip()  
        if not line: 
            continue
        report = list(map(int,data[i].split(' ')))
        if is_valid(report)[0]:
            s+=1
        if is_super_valid(report):
            answers.append(report)
            s2+=1
    print(s)
    print(s2)

with open ('output.txt', 'w') as file:
    for i in answers:
        file.write(' '.join(map(str,i))+'\n')
    
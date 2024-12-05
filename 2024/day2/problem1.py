with open ('input.txt', 'r') as file:
    data = file.read().splitlines()
    l = len(data)
    s=0
    for i in range(l):
        report = list(map(int,data[i].split(' ')))
        print (report )
        
        a = report[0]
        i = report [1]
        flag = -1
        print(a,i,flag)
        if i>a and i<a+3:
            flag = 1
        elif i<a and a<i+3:
            flag=2
        else:
            flag = -1
        a=i
        for i in report[2:]:
            print(a,i,flag)
            if flag==-1:
                break
            else:
                if flag == 1 and( i<=a or i>=a+3):
                    flag = -1
                elif flag == 2 and( i>=a or a>=i+3):
                    flag=-1
            a=i
        if flag != -1:
            s+=1
    print(s)


with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    list1  = [0]*len(data)
    list2  = [0]*len(data)
    s =0
    l = len(data)
    for i in range(l):
        list1[i],list2[i]= map(int,data[i].split('   '))
        
    list1.sort()
    list2.sort()

    for i in range(l):
        s += abs(list2[i]-list1[i])
    
    print(s)


    
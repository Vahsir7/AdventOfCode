with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    list1  = []
    list2  = {}
    s =0
    l = len(data)
    list1 = [0]*l
    for i in range(l):
        list1[i],temp = map(int,data[i].split('   '))
        if temp in list2:
            list2[temp]+=1
        else:
            list2[temp]=1
    
    for i in range(l):
        try :
            prod = list2[list1[i]]
        except:
            prod = 0
        s += abs(list1[i] * prod)
    
    print(s)
        
        
    

    
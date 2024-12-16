def is_valid(rules, update):
    #print(update)
    for index,page in enumerate(update):
        if page in rules.keys():
            #print(page, rules[page])
            for i in rules[page]:
                if i in update and i not in update[:index]:
                    #print(page, rules[page])
                    return False
    return True
            
with open('input.txt') as f:
    lines = [line.strip().upper() for line in f]  # Clean and standardize input
    ans = 0
    l = len(lines)
    rules = {}
    updates = []  
    flag = True
    #print(lines)
    for line in lines:
        #print(line)
        if line == '':
            flag = False
            continue
        if(flag):
            a,b = line.split('|')
            if b not in rules:
                rules[b] = []
            rules[b].append(a)
        else:
            updates.append(line.split(','))
        

    #print(rules)
    #print("updates")
    #print(updates)
    #print("---start---")
    for update in updates:
        if is_valid(rules, update):
           #print(update)
           #print(int(update[len(update)//2]))
           ans += int(update[len(update)//2])
    
    print(ans)
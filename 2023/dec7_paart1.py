input_file_path = r"D:\Coding\AdventOfCode\2023\dec7input.txt"

def zipping(l1,l2):
    dict1 = dict(zip(l1, l2))
    dict1 = dict(sorted(dict1.items(),reverse=True))
    return dict1
def adding(total,dict1,num):
    for i in dict1:
        total+=int(dict1[i])*num
        num-=1
    return (total,num)

with open(input_file_path, "r", encoding="utf-8") as f:
    num=len(f.readlines())
    f.seek(0)
    content = f.read()

    # Replace characters in the content
    content = content.replace("A", "Z")
    content = content.replace("K", "Y")
    content = content.replace("Q", "X")
    content = content.replace("J", "W")
    content = content.replace("T", "V")

    #print(content)  # Print the modified content

    sorted_cards = ["".join(i[:6].strip()) for i in content.split('\n')]
    bidding_amt = [i[6:].strip() for i in content.split('\n')]
    #print(sorted_cards)
    #print(bidding_amt)
    game=dict(zip(sorted_cards,bidding_amt))
    #game=dict(sorted(game.items(),reverse=True))

    #print(game)
    kind5=[]
    kind5amt=[]

    kind4=[]
    kind4amt=[]

    full_house=[]
    full_house_amt=[]

    kind3=[]
    kind3amt=[]

    two_pair=[]
    two_pair_amt=[]

    one_pair=[]
    one_pair_amt=[]

    high_card=[]
    high_card_amt=[]

    for i in game:
        if i.count(i[0]) == 5:
            kind5.append(i)
            kind5amt.append(game[i])
        elif i.count(i[0]) == 4 or i.count(i[-1]) == 4:
            kind4.append(i)
            kind4amt.append(game[i])
        elif i.count(i[0]) == 3 or i.count(i[1]) == 3 or i.count(i[2]) == 3 or i.count(i[3]) == 3 or i.count(i[4]) == 3:
            if i.count(i[0]) == 2 or i.count(i[-1]) == 2 or i.count(i[1]) == 2 or i.count(i[2]) == 2 or i.count(i[3]) == 2 or i.count(i[4]) == 2:
                full_house.append(i)
                full_house_amt.append(game[i])
            else:
                kind3.append(i)
                kind3amt.append(game[i])
        else:
            x="".join(sorted(i))
            #print(x)
            if (x.count(x[0]) == 2 and x.count(x[2]) == 2 ) or (x.count(x[1]) == 2 and x.count(x[3]) == 2 ):
                #print(x[0],x.count(x[0]),x[2],x.count(x[2]))
                #print(x[1],x.count(x[1]),x[3],x.count(x[3]))
                two_pair.append(i)
                two_pair_amt.append(game[i])
            elif x.count(x[0]) == 2 or x.count(x[1]) == 2 or x.count(x) == 2 or x.count(x[3]) == 2:
                one_pair.append(i)
                one_pair_amt.append(game[i])
            else:
                high_card.append(i)
                high_card_amt.append(game[i])


    five_kind=zipping(kind5,kind5amt)
    four_kind=zipping(kind4,kind4amt)
    full_house=zipping(full_house,full_house_amt)
    three_kind=zipping(kind3,kind3amt)
    two_pair=zipping(two_pair,two_pair_amt)
    one_pair=zipping(one_pair,one_pair_amt)
    high_card=zipping(high_card,high_card_amt)


    total=0
    total,num=adding(total,five_kind,num)
    total,num=adding(total,four_kind,num)
    total,num=adding(total,full_house,num)
    total,num=adding(total,three_kind,num)
    total,num=adding(total,two_pair,num)
    total,num=adding(total,one_pair,num)
    total,num=adding(total,high_card,num)

    print(total)
    #print(five_kind)
    #print(four_kind)
    exit()
    #print("full house")
    for content in full_house:
        content = content.replace("Z", "A")
        content = content.replace("Y", "K")
        content = content.replace("X", "Q")
        content = content.replace("W", "J")
        content = content.replace("V", "T")
        print(content)

    #print("three kind")
    for content in three_kind:
        content = content.replace("Z", "A")
        content = content.replace("Y", "K")
        content = content.replace("X", "Q")
        content = content.replace("W", "J")
        content = content.replace("V", "T")
        print(content)

    #print("two pair")
    for content in two_pair:
        content = content.replace("Z", "A")
        content = content.replace("Y", "K")
        content = content.replace("X", "Q")
        content = content.replace("W", "J")
        content = content.replace("V", "T")
        print(content)

    #print("one pair")
    for content in one_pair:
        content = content.replace("Z", "A")
        content = content.replace("Y", "K")
        content = content.replace("X", "Q")
        content = content.replace("W", "J")
        content = content.replace("V", "T")
        print(content)

    #print("high card")
    for content in high_card:
        content = content.replace("Z", "A")
        content = content.replace("Y", "K")
        content = content.replace("X", "Q")
        content = content.replace("W", "J")
        content = content.replace("V", "T")
        print(content)
        

        #print(i)
    
        

    

            
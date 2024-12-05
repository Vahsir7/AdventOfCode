seeds = []

with open("D:\\Coding\\AdventOfCode\\2023\\dec5.txt", "r") as file:
    content = file.read().split("\n\n")
    inputs = list(map(int, content[0].split(":")[1].split()))

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))
    print(seeds)


    for block in content[1:]:
        ranges = []
        print(block[:block.index(":")])
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))
            #print("new",new)
            #print("seeds",seeds)
        seeds = new

print(min(seeds)[0])

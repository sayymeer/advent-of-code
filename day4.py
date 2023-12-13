import sys
content = open(sys.argv[1]).read().strip().splitlines()

p1 = []
p2 = {i:1 for i in range(len(content))}

for line in content:
    numbers = line.split(":")[1].strip().split("|")
    winnum = set(map(int,numbers[0].split()))
    cardnum = set(map(int,numbers[1].split()))
    point = 0
    for num in cardnum:
        if num in winnum:     
            point+=1
    p1.append(point)

p2Sol = 0
for card in p2:
    num_of_win = p1[card]
    p2Sol += p2[card]
    for i in range(card+1,card+num_of_win+1):
        if i<len(p1):p2[i] += p2[card]

print(sum(list(map(lambda x:int(pow(2,x-1)),p1))))
print(p2Sol)
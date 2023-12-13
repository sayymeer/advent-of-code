import sys
content = open(sys.argv[1]).read().strip().split('\n')
pos1 = set()
pos2 = []
p1 = []
p2 = []

def getNumber(pos):
    s = ""
    r,c = pos
    while c<len(content[0]) and content[r][c].isdigit():
        s += content[r][c]
        c+=1
    return int(s)

for r,line in enumerate(content):
    for c,char in enumerate(line):
        if char.isdigit() or char == '.':
            continue
        num = []
        for cr in [r-1,r,r+1]:
            for cc in [c-1,c,c+1]:
                if cr<0 or cr>len(content) or cc<0 or cc>len(line) or not content[cr][cc].isdigit():
                    continue
                while cc>0 and content[cr][cc-1].isdigit():
                    cc -= 1
                num.append((cr,cc))
                pos1.add((cr,cc))
        set_num = set(num)
        if len(set_num)==2 and char=='*':
            if len(set_num) != 1:
                pos2.append(set_num)

for r,c in pos1:
    p1.append(getNumber((r,c)))


for idex in pos2:
    a,b = idex
    num1,num2 = getNumber(a),getNumber(b)
    p2.append(num1*num2)


print(sum(p1))
print(sum(p2))
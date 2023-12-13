import sys
content = open(sys.argv[1]).read().strip().split('\n')

#Max colors allowed for r g and b
colors = ['red','green','blue']
maxcolors = [12,13,14]
validGameNumber = []
powersOfCube = []

def getColors(s:str)->list[int]:
    s = s.strip().split(' ')
    result = {'red':0,'green':0,'blue':0}
    for i in range(len(s)):
        for c in colors:
            if s[i].startswith(c):
                result[c] = int(s[i-1])
    return [result['red'],result['green'],result['blue']]

for i,line in enumerate(content,start=1):
    line = line.split(': ')[1].split('; ')
    check = True
    cubes = [[],[],[]]
    for r in line:
        res = getColors(r)
        for k in range(3): cubes[k].append(res[k])
        if any(maxcolors[i] < res[i] for i in range(3)): check = False
    if check : validGameNumber.append(i)
    powerSet = list(map(max,cubes))
    powersOfCube.append(powerSet[0]*powerSet[1]*powerSet[2])

print(sum(validGameNumber))
print(sum(powersOfCube))

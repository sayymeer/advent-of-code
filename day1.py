import sys
data = open(sys.argv[1]).read().strip().split('\n')

answer1 = 0
answer2 = 0

for line in data:
    digits1 = []
    digits2 = []
    for i,c in enumerate(line):
        if c.isdigit(): digits1.append(c) or digits2.append(c)
        for d,digit in enumerate(['one','two','three','four','five','six','seven','eight','nine'],start=1):
            if line[i:].startswith(digit): digits2.append(str(d))
    answer1 += int(digits1[0]+digits1[-1])
    answer2 += int(digits2[0]+digits2[-1])

print(answer1,answer2,sep='\n')
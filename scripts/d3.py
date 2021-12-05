from collections import defaultdict


def colParse(vec, epsilon=False):
    OnesVal = sum(vec) # should be 1s
    getMax = len(vec)-OnesVal
    if epsilon:
        if getMax > OnesVal:
            return 1
        else:
            return 0
    if getMax > OnesVal:
        return 0
    else:
        return 1

def part1():
    bitDict = defaultdict(list)
    for row in open('inputs/d3.txt'):
        rowParse = [int(i) for i in list(row.strip())]
        for n, bit in enumerate(rowParse):
            bitDict[n].append(bit)
    epList=['0b']
    gaList=['0b']
    for key, val in bitDict.items():
        epList.append(str(colParse(val, epsilon=True)))
        gaList.append(str(colParse(val)))
    epDec = int(''.join(epList), 2)
    gaDec = int(''.join(gaList), 2)
    print('The Answer to Part1 is {}'.format(epDec*gaDec))

part1()
from collections import defaultdict
inputFile = 'inputs/d3.txt'

def colParse(vec, epsilon=False):
    OnesVal = sum(vec) # should be 1s
    getMax = len(vec)-OnesVal
    if epsilon:
        if getMax >= OnesVal:
            return 1
        else:
            return 0
    if getMax >= OnesVal:
        return 0
    else:
        return 1

def makeDict(bitFile):
    bitDict = defaultdict(list)
    rowList = []
    for row in open(bitFile):
        rowList.append(row.strip())
        rowParse = [int(i) for i in list(row.strip())]
        for n, bit in enumerate(rowParse):
            bitDict[n].append(bit)
    return bitDict, rowList

def part1(bitDict):
    epList=['0b']
    gaList=['0b']
    for key, val in bitDict.items():
        epList.append(str(colParse(val, epsilon=True)))
        gaList.append(str(colParse(val)))
    epDec = int(''.join(epList), 2)
    gaDec = int(''.join(gaList), 2)
    print('The Answer to Part1 is {}'.format(epDec*gaDec))

bitDict, rowList = makeDict(inputFile)
part1(bitDict)

## part2
def lifeSupRate(vec, CO=False):
    OnesVal = sum(vec) # should be 1s
    getMax = len(vec)-OnesVal
    if CO:
        if getMax > OnesVal:
            return 1
        else:
            return 0
    else:
        if getMax > OnesVal:
            return 0
        else:
            return 1


def getRating(bitDict, rowList, CO):
    bitMap = []
    for key, val in bitDict.items():
        bitMap.append(val)
    nList = []
    for n in range(0, len(bitMap)):
        val = bitMap[n]
        getO2=lifeSupRate(val, CO)
        nList=[n for n, i in enumerate(val) if i == getO2]
        #print(rowList)
        if nList:
            rowList = [rowList[n] for n, i in enumerate(val) if i == getO2]
            for i in range(n, len(bitMap)):
                temp = bitMap[i]
                bitMap[i]=[temp[i] for i in nList]
    return int('0b'+rowList[0], 2)


def part2(inputFile):
    bitDict, rowList = makeDict(inputFile)
    OXrate = getRating(bitDict, rowList, CO=False)
    bitDict, rowList = makeDict(inputFile)
    COrate=getRating(bitDict, rowList, CO=True)
    print('The Answer to Part2 is {}'.format(OXrate*COrate))

part2(inputFile)





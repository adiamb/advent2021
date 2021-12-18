from collections import defaultdict
import copy
inputFile = 'inputs/d4.txt'

def fileReader(inputFile):
    numList = []
    brdDictRsums= defaultdict(list)
    brdCnt =0
    rowC = 0
    with open(inputFile) as inFile:
        for n, line in enumerate(inFile):
            lineParse = line.strip()
            if n == 0:
                numList=lineParse.split(',')
            else:
                if lineParse:
                    rows = [i for i in lineParse.split(' ') if i]
                    rowC += 1
                    for n, num in enumerate(rows):
                        key = '{} {} {}'.format(brdCnt, rowC, n+1)
                        brdDictRsums[str(brdCnt)].append(num)
                else:
                    brdCnt += 1
                    rowC = 0
    return brdDictRsums, numList

brdDictRsums, numList = fileReader(inputFile)



dict = {}
n = 0
for i in range(1, 6):
    for j in range(1,6):
        n += 1
        dict[n] = [i, j]


checkDictRow = defaultdict(list)
checkDictCol = defaultdict(list)
unMarkedDict = copy.deepcopy(brdDictRsums)
stop=False
n = 0
while not stop:
    num = numList[n] ## check all boards for this num 
    for brd, item in brdDictRsums.items():
        if num in item: ##mark off the item in row dict
            index=item.index(num)+1
            rowPos, colPos = dict.get(index)
            makeKeyRow = tuple([brd, rowPos])
            makeKeyCol = tuple([brd, colPos])
            checkDictRow[makeKeyRow].append(num)
            checkDictCol[makeKeyCol].append(num)
            #remove the item from unMarkeddict
            #tempList=unMarkedDict[brd]
            unMarkedDict[brd] = [i for i in unMarkedDict[brd] if i != num] 
            if len(checkDictRow.get(makeKeyRow)) == 5 or len(checkDictCol.get(makeKeyCol)) == 5:
                #print('{} , {} , {}, {}'.format(num, brd, brdDictRsums[brd], checkDict[makeKey]))
                unmarkSum=sum([int(i) for i in  unMarkedDict[brd]])
                print('The Answer to Part 1 is  {}'.format(unmarkSum*int(num)))
                stop =True
    n += 1
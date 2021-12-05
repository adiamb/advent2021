def getdepth(input):
    stream=[int(i.strip()) for i in open(input, 'r')]# as inFile:
    n = 0
    for i in range(0, len(stream)-1):
        if stream[i+1] >= stream[i]:
            n +=1
    print(n)
    return(n)

getdepth(input='inputs/d1p1.txt')


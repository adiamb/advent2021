def part1(stream):
    n = 0
    for i in range(0, len(stream)-1):
        if stream[i+1] > stream[i]:
            n +=1
    print(n)
    return(n)

stream=[int(i.strip()) for i in open('inputs/d1p1.txt', 'r')]
part1(stream)

def part2(stream):
    stream2=[]
    for i in range(0, len(stream), 1):
        temp = stream[i:i+3]
        if len(temp) == 3:
            stream2 +=[sum(temp)]
    part1(stream2)

part2(stream)
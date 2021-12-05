class submarine(object):
    def __init__(self, object):
        self.step = object[1]
        self.command = object[0]
        self.horiz = object[2]
        self.depth = object[3]

    def updown(self):
        if self.command == 'up':
            self.depth -= self.step
        elif self.command == 'down':
            self.depth += self.step
        return self.depth
    
    def fwd(self):
        self.horiz += self.step
        return self.horiz
    
    def coord(self):
        return self.horiz, self.depth


def part1():
    with open('inputs/d2.txt', 'r') as dirFile:
        h, d = 0, 0
        for line in dirFile:
            row = line.strip().split(' ')
            dirTup = (row[0], int(row[1]), h, d)
            #init sub
            drive=submarine(dirTup)
            if row[0] == 'forward':
                h = drive.fwd()
            else:
                d = drive.updown()
        print('The Ans to Part1 is {}'.format(h*d))

part1()

class submarineAim(submarine):
    def __init__(self, object):
        super().__init__(object)
        self.aim = object[4]

    def updown(self):
        if self.command == 'up':
            self.aim -= self.step
        else:
            self.aim += self.step
        return self.horiz, self.depth, self.aim

    def fwd(self):
        self.horiz += self.step
        self.depth += (self.aim*self.step)
        return self.horiz, self.depth, self.aim


def part2():
    with open('inputs/d2.txt', 'r') as dirFile:
        h, d, aim = 0, 0, 0
        for line in dirFile:
            row = line.strip().split(' ')
            dirTup = (row[0], int(row[1]), h, d, aim)
            drive=submarineAim(dirTup)
            if row[0] == 'forward':
                h, d, aim = drive.fwd()
            else:
                h, d, aim = drive.updown()
            #print('H {} DEP {} AIM {} line {}'.format(h, d, aim, line))
        print('The Ans to Part2 is {}'.format(h*d))

part2()
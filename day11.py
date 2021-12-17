example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

puzzle = """8577245547
1654333653
5365633785
1333243226
4272385165
5688328432
3175634254
6775142227
6152721415
2678227325"""

max_dim = 10
flashes = 0
adj = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
pod = [[int(c) for c in line] for line in puzzle.split("\n")]
pod


def increaseAdj(x, y, m):
    m[y][x] += 1
    if m[y][x] == 10:
        for (dx, dy) in adj:
            (nx, ny) = (x + dx, y + dy)
            if (nx < 10 and ny < 10 and nx >= 0 and ny >= 0):
                increaseAdj(nx, ny, m)

def countFlashes(m):
    flashes = 0
    for x in range (0, max_dim):
        for y in range (0, max_dim):
            if m[y][x] > 9:
                m[y][x] = 0
                flashes += 1
    return flashes

    
def simulateStep(m):
    for x in range (0, max_dim):
        for y in range (0, max_dim):
            increaseAdj(x, y, m)
    return countFlashes(m)

def printMap(m):
    for line in m:
        row = ""
        for c in line:
            if (c == 0):
                row += "\x1b[31m0\x1b[39m"
            else:
                row += "\x1b[34m"+str(c)+"\x1b[39m"
        print(row)

def isSynchronized(m):
    return all([all(v == 0 for v in line) for line in m])

from os import system

import copy, time
def runSteps(numSteps, m):
    flashes = 0
    for step in range(0, numSteps):
        flashes += simulateStep(m)
    return m
        
def runTillSync(m):
    step = 0
    while not isSynchronized(m):
        runSteps(1, m)
        step += 1
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
        print(f"STEP {step}")
        printMap(m)
        time.sleep(0.125)

    
m = runSteps(100, copy.deepcopy(pod))
print(f"STEP 100")
printMap(m)

runTillSync(copy.deepcopy(pod))

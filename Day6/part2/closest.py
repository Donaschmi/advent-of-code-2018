import os
from collections import defaultdict

def fileToString():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, '../input.txt')
    with open(my_file, "r") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n`
        # at the end of each line
        content = [x.strip() for x in content]
    return content

def sum_dist(i, j, positions):
    dist = 0
    for pos in positions:
        dist += abs(i - pos[0]) + abs(j - pos[1])
    return dist

def _grid(positions):
    left = min(x for (x, _) in positions)
    top = min(y for (_, y) in positions)
    right = max(x for (x, _) in positions)
    bot = max(y for (_, y) in positions)
    
    return left, top, right, bot

def main():
    content = fileToString()
    positions = set()
    for s in content:
        x, y = s.split(', ')
        positions.add((int(x), int(y)))

    left, top, right, bot = _grid(positions)
    result = 0
    for i in range(left, right+1):
        for j in range(top, bot + 1):

            if sum_dist(i, j, positions) < 10000:
                result += 1
    return result
                

if __name__ == "__main__":
    print main()

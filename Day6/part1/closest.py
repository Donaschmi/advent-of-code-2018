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

def closestPos(i, j, positions):
    dist = {}
    for pos in positions:
        dist[pos] = abs(pos[0] - i) + abs(pos[1] - j)
    
    result = set(pos for pos in positions if dist[pos] == min(dist.values()))

    if len(result) > 1:  # more than one pos closest to point -: conflict
        return None
    return list(result)[0]

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

    infinite = set()
    grid = dict()
    data = defaultdict(int)

    for i in range(left, right+1):
        grid[i] = dict()
        for j in range(top, bot + 1):
            grid[i][j] = closestPos(i, j, positions)

            if grid[i][j] is not None:
                data[grid[i][j]] += 1
            
            if i == left or i == right or j == top or j == bot and grid[i][j] is not None:
                infinite.add(grid[i][j])
    
    return max(val for key, val in data.items() if key not in infinite)
                

if __name__ == "__main__":
    print main()

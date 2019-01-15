import os

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def fileToString():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'input.txt')
    with open(my_file, "r") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n`
        # at the end of each line
        content = [x.strip() for x in content]
    return content


def treatLine(line):
    id = line[0][1::]
    pos = line[2].split(',')
    end = len(pos[1])
    pos[1] = pos[1][0:end-1]
    size = line[3].split('x')
    return (id, pos, size)


def parseFile(file):
    result = []
    for line in file:
        line_split = line.split(' ')
        # Remove uneccessary char ex: ' , :
        (id, pos, size) = treatLine(line_split)
        pos = (int(pos[0]), int(pos[1]))
        size = (int(size[0]), int(size[1]))
        result.append([id, pos, size])
    return result

def completeMatrix(treated_data):
    count = 0
    array = [[0] * 1000 for i in range(1000)]
    ok = {}
    for pair in treated_data:
        ok[pair[0]] = True
        for x in range(pair[2][0]):
            for y in range(pair[2][1]):
                new_x = pair[1][0] + x
                new_y = pair[1][1] + y
                elem = array[new_x][new_y]
                if elem == 0:
                    array[new_x][new_y] = pair[0]
                elif elem != 0 and not elem == 'X':
                    ok.pop(pair[0], None)
                    ok.pop(elem, None)
                    array[new_x][new_y] = 'X'
                    count += 1
    return count, ok

def main():
    content = fileToString()
    treated_data = parseFile(content)
    result, ok = completeMatrix(treated_data)
    for d in ok:
        print d
    print result

if __name__ == "__main__":
     main()
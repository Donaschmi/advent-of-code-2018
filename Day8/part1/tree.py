import os
import collections, string

def fileToString():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, '../input.txt')
    with open(my_file, "r") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n`
        # at the end of each line
        content = [x.strip() for x in content]
    return ''.join(content).split()



def main():
    content = fileToString()
    nodes = list(map(int, content))
    stack = []
    i = 0
    while i < len(nodes):
        if len(stack) == 0:
            children = nodes[i]
            meta = nodes[i + 1]
            stack.append([children, meta, children, []])
            i += 2
        elif stack[-1][0] == 0:
            val = 0
            if stack[-1][2] == 0:
                for j in range(stack[-1][1]):
                    val += nodes[i + j]
            else:
                for j in range(stack[-1][1]):
                    index = nodes[i + j] - 1
                    if index >= len(stack[-1][3]):
                        continue
                    val += stack[-1][3][index]
            i += stack[-1][1]
            stack.pop()
            if len(stack) > 0:
                stack[-1][0] -= 1
                stack[-1][3].append(val)
            else:
                return val
        else:
            children = nodes[i]
            meta = nodes[i + 1]
            stack.append([children, meta, children, []])
            i += 2
    return sum_meta

if __name__ == "__main__":
    print main()

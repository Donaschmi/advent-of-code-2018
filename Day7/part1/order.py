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
    return content


def build_dep(file):
    nodes = {}
    letters = []
    for s in file:
        to = s.split()[-3]
        needs = s.split()[1]
        if to not in letters:
            letters.append(to)
        if needs not in letters:
            letters.append(needs)
        if to in nodes:
            nodes[to].append(needs)
        else:
            nodes[to] = [needs]
    on = collections.OrderedDict(sorted(nodes.items()))
    letters = sorted(letters)
    return on, letters

def clear(nodes, letters):
    ordered = []
    while len(nodes) != 0:
        for l in letters:
            if not l in nodes:
                ordered.append(l)
                letters.remove(l)
                for n, a in nodes.items():
                    if l in a:
                        a.remove(l)
                    if len(a) == 0:
                        del nodes[n]
                break
    ordered.append(letters[0])
    return ordered

def main():
    content = fileToString()
    dep, letters = build_dep(content)
    return clear(dep, letters)

if __name__ == "__main__":
    print ''.join(main())

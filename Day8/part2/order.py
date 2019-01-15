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

def processed(letter, workers):
    for w in workers:
        if w is not None and  w[0] == letter:
            return True
    return False

def clear(nodes, letters):
    alphabet = string.ascii_uppercase
    ordered = []
    workers = 5
    worker_task = [None] * workers
    total_time = 0
    while len(letters) > 0:
        for l in letters:
            if not l in nodes:
                for i, w in enumerate(worker_task):
                    if w is None and not processed(l, worker_task):
                        worker_task[i] = (l, alphabet.find(l) + 61)
                        print 'add letter : '+l+' to task'

        for i, task in enumerate(worker_task):
            if task is None:
                continue
            worker_task[i] = (worker_task[i][0], worker_task[i][1] - 1)
            
            if worker_task[i][1] == 0:
                l = worker_task[i][0]
                ordered.append(l)
                letters.remove(l)
                worker_task[i] = None
                for n, a in nodes.items():
                    if l in a:
                        a.remove(l)
                    if len(a) == 0:
                        del nodes[n]
        total_time += 1
    print total_time
    return ordered

def main():
    content = fileToString()
    dep, letters = build_dep(content)
    return clear(dep, letters)

if __name__ == "__main__":
    print ''.join(main())

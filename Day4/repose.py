import os

def fileToString():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'input-S.txt')
    with open(my_file, "r") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n`
        # at the end of each line
        content = [x.strip() for x in content]
    return content

def part1():
    lines = fileToString()
    current_id = None
    guards = {}
    guards_minutes = {}
    start = 0
    end = 59
    for line in lines:
        line_split = line.split()
        if 'Guard' in line_split:
            current_id = int(line_split[3].split('#')[1])
        elif 'falls' in line_split:
            start = int(line_split[1].split(':')[1][:2])
        else:
            end = int(line_split[1].split(':')[1][:2])
            guards[current_id] = guards.get(current_id, 0) + end - start
            if not current_id in guards_minutes:
                guards_minutes[current_id] = {}

            for i in range(start, end):
                guards_minutes[current_id][i] = guards_minutes[current_id].get(i, 0) + 1
    
    max_id = None
    max_i = 0
    for g in guards:
        if max_id is None or guards[g] > max_i:
            max_id = g
            max_i = guards[g]
    
    minute = None
    max_time = 0
    for t in guards_minutes[max_id]:


        if minute is None or guards_minutes[max_id][t] > max_time:
            minute = t
            max_time = guards_minutes[max_id][t]
    return minute * max_id


def part2():
    lines = fileToString()
    current_id = None
    guards = {}
    guards_minutes = {}
    start = 0
    end = 59
    for line in lines:
        line_split = line.split()
        if 'Guard' in line_split:
            current_id = int(line_split[3].split('#')[1])
        elif 'falls' in line_split:
            start = int(line_split[1].split(':')[1][:2])
        else:
            end = int(line_split[1].split(':')[1][:2])
            guards[current_id] = guards.get(current_id, 0) + end - start
            if not current_id in guards_minutes:
                guards_minutes[current_id] = {}

            for i in range(start, end):
                guards_minutes[current_id][i] = guards_minutes[current_id].get(i, 0) + 1

    max_id = None
    max_time = 0
    minute = 0
    for g in guards_minutes:
        for t in guards_minutes[g]:
            if max_id is None or guards_minutes[g][t] > max_time:
                max_id = g
                max_time = guards_minutes[g][t]
                minute = t
    return minute * max_id


def main():
   res1 = part1()
   res2 = part2()
   return (res1, res2)


if __name__ == "__main__":
      print main()
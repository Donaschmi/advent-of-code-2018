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
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    return content

def main():
    sum = 0;
    content = fileToString()
    index = 0
    hashmap = {}
    while True:
        sum += num(content[index])
        if sum in hashmap:
            return sum
        else:
            hashmap[sum] = 1
        index = (index + 1) % len(content)
    print sum

if __name__ == "__main__":
    print main()

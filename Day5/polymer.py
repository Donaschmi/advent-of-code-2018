import os
import string


def fileToString():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'input.txt')
    with open(my_file, "r") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n`
        # at the end of each line
        content = [x.strip() for x in content]
    return content


def number():
    polymer = fileToString()[0]
    
    mini = None
    for cc in string.ascii_lowercase:
        stack = []
        s = polymer.replace(cc, "")
        s = s.replace(cc.upper(), "")
        print 'test'
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1].lower() == c.lower() and stack[-1] != c:
                stack.pop()
            else:
                stack.append(c)
        if mini is None or len(stack) < mini:
            mini = len(stack)
            print mini
    return mini


def main():
    print number()

if __name__ == "__main__":
    main()

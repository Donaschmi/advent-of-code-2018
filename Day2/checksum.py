import os


def fileToString():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'input.txt')
    with open(my_file, "r") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n`
        # at the end of each line
        content = [x.strip() for x in content]
    return content


def inter(content):
    curr = 0
    index = 1
    while curr < len(content) - 1:
        for i in range(index, len(content)):
            diff = 0
            for j in range(0, len(content[curr])):
                diff = diff + 1 if content[curr][j] != content[i][j] else diff
            if diff == 1:
                return (content[curr], content[i])
        curr += 1
        index += 1


def result():
    content = fileToString()
    (s1, s2) = inter(content)
    print(s1, s2)
    sr = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            sr += s1[i]
    return sr


def main():
    content = fileToString()
    hashmap = {}
    for s in content:  # Iterate through each line
        number_of_letter = {}
        for c in s:  # Iterate through each char
            if c in number_of_letter:
                number_of_letter[c] += 1
            else:
                number_of_letter[c] = 1

        changed = {}
        for occ in number_of_letter:  # Iterate through each occurence
            val = number_of_letter[occ]
            if val in changed:
                continue

            if val != 1:
                hashmap[val] = hashmap[val] + 1 if val in hashmap else 1
                changed[val] = 1

    mult = 1
    print hashmap
    for key in hashmap:
        mult *= hashmap[key]
    print mult


if __name__ == "__main__":
    print result()

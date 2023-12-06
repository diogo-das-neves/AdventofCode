import re

numberDict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
              "eight": "8", "nine": "9"}


def easy():
    total = 0
    f = open("easy.txt", "rt")
    for line in f.readlines():
        digits = re.findall("\d", line)
        if len(digits) == 1:
            total += int(digits[0] + digits[0])
        else:
            total = total + int(digits[0] + digits[-1])
    f.close()
    return total


def hard():
    total = 0
    replace = ["", ""]
    f = open("test.txt", "rt")
    for line in f.readlines():
        lowerIndex = 100
        higherIndex = -1
        line.lower()
        for key, value in numberDict.items():
            if key in line:
                if lowerIndex >= line.find(key):
                    lowerIndex = line.find(key)
                    replace[0] = key
                if higherIndex <= line.rfind(key):
                    higherIndex = line.rfind(key)
                    replace[1] = key
        line = line.replace(replace[0], numberDict.get(replace[0]), 1)
        line = line.replace(replace[1], numberDict.get(replace[1]), line.count(replace[1]))
        digits = re.findall("\d", line)
        if len(digits) == 1:
            total += int(digits[0] + digits[0])
        else:
            total = total + int(digits[0] + digits[-1])
    f.close()
    return total

def hardClean():
    sum = 0
    with open('easy.txt') as f:
        for line in f.read().splitlines():
            digits = []
            for index, char in enumerate(line):
                digits.append(char) if char.isdigit() else None
                for pos, number in enumerate(
                        ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')):
                    digits.append(str(pos + 1)) if line[index:].startswith(number) else None
            sum += int(digits[0] + digits[-1])
    return sum





if __name__ == '__main__':
    print("easy: {}".format(easy()))
    print("hard: {}".format(hardClean()))


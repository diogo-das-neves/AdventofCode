import re

numberDict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
              "eight": "8", "nine": "9"}


def easy():
    total = 0
    f = open("input.txt", "rt")
    for line in f.readlines():
        digits = re.findall("\d", line)
        if len(digits) == 1:
            total += int(digits[0] + digits[0])
        else:
            total = total + int(digits[0] + digits[-1])
    f.close()
    return total

def hardClean():
    sum = 0
    with open('input.txt') as f:
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


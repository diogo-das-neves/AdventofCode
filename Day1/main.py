import re


def main():
    total = 0
    f = open("easy.txt", "rt")
    for line in f:
        match = re.findall("\d", line)
        if len(match) == 1:
            total += int(match[0]+match[0])
        else:
            total = total + int(match[0] + match[-1])
    print(total)


if __name__ == '__main__':
    main()

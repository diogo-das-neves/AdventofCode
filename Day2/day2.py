import math
sack = {"red": 12, "green": 13, "blue": 14}


def part1():
    sum = 0
    with open("input.txt") as f:
        for line in f.read().splitlines():
            ID, plays = line.split(":")
            ID = int(ID[5:])
            flag = 1
            for sets in plays.split(";"):
                for move in sets.split(","):
                    move = move.lstrip()
                    number, color = move.split(" ")
                    if int(number) > sack.get(color):
                        flag = 0
                        break
                    else:
                        continue
            if flag == 1:
                sum += ID
        return sum

def part2():
    sum = 0
    power = 0
    with open("input.txt") as f:
        for line in f.read().splitlines():
            sack2 = {"red": 0, "green": 0, "blue": 0}
            ID, plays = line.split(":")
            ID = int(ID[5:])
            for sets in plays.split(";"):
                for move in sets.split(","):
                    move = move.lstrip()
                    number, color = move.split(" ")
                    if int(number) > sack2.get(color):
                        sack2.update({color: int(number)})
            power = math.prod(dict.values(sack2))
            sum += power
        return sum


if __name__ == '__main__':
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')


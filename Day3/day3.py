"""
number_matrix - start and end of number? [number((start)(end))]
                                                 x - char_pos, y - line_number y -  same since number only counts horizontally
[(number, line, start, end) .... ]
symmbox_matrix = [(line, pos)]
"""


def getMatrix() -> tuple[list, list]:
    number_maxtrix = []
    symbol_matrix = []
    start = 0
    flag = False
    with open("example.txt") as f:
        for line_number, line in enumerate(f.read().splitlines()):
            for char_pos, char in enumerate(line):
                if char.isdigit() and not flag:
                    flag = True
                    start = char_pos
                if char.isdigit() and flag:
                    continue
                if flag and not char.isdigit():
                    end = char_pos - 1
                    value = int(line[start:end + 1])
                    number_maxtrix.append((value, line_number, start, end))
                    flag = False
                if char == ".":
                    continue
                else:
                    symbol_matrix.append((line_number, char_pos))

    return number_maxtrix, symbol_matrix


def adjency(positions: tuple) -> bool:
    number_matrix = positions[0]
    symbol_matrix = positions[1]
    for symbol_location in symbol_matrix:
        for number in number_matrix:

            symbol_y = symbol_location[0]
            symbol_x = symbol_location[1]

            number_y = number[1]
            number_xstart = number[2]
            number_xend = number[3]

            if number_y == symbol_y:
                if (symbol_x + 1 == number_xend or symbol_x - 1 == number_xend or
                        symbol_x + 1 == number_xstart or symbol_x - 1 == number_xstart):
                    return True
            elif ( number_xstart <= symbol_x <=number_xend):
                print(number[0])
                return True

    return True


def sum(positions: tuple) -> int:
    total = 0
    for number_index in range(len(positions[0])):
        for symbol_index in range(len(positions[1])):
            break

    return total


if __name__ == '__main__':
    x = getMatrix()
    adjency(x)
    print(f'Symbol Locations: {x[1]} \n Number Locations: {x[0]}')
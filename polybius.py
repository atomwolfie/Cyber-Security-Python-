

SQUARE = [
        ['e', '2', 'r', 'f', 'z', 'm'],
        ['y', 'h', '3', '0', 'b', '7'],
        ['o', 'q', 'a', 'n', 'u', 'k'],
        ['p', 'x', 'j', '4', 'v', 'w'],
        ['d', '1', '8', 'g', 'c', '6'],
        ['9', 'i', 's', '5', 't', 'l']
        ]

def polybius(numbers):
    # takes a string of numbers and runs them through the polybius square
    ret = ''
    for i in range(len(numbers))[::2]:
        ret = ret + SQUARE[int(numbers[i])][int(numbers[i + 1])]

    return ret



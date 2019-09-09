from pip._vendor.distlib.compat import raw_input


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

def get_one_time_pad(numbers):

    numbers_length = len(numbers)
    one_time_pad = int(numbers[numbers_length -2] + numbers[numbers_length - 1])
    return(one_time_pad)


def dec_to_bin(x):
    start = '00'
    return start + str(int(bin(x)[2:]))


if __name__ == '__main__':

   comp_key = raw_input('Enter Composite Key: ')


   print(polybius(comp_key[:-2]))
   print(get_one_time_pad(comp_key))
   print(dec_to_bin(11))
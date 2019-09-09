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
    #takes the last 2 digits for the entry and
    # creates a one time pad key used for encryption
    numbers_length = len(numbers)
    one_time_pad = int(numbers[numbers_length -2] + numbers[numbers_length - 1])
    return(one_time_pad)


def dec_to_bin(x):
    #converts integers to decimal form
    start = '00'
    return start + str(int(bin(x)[2:]))


def get_coordinates(trans_key):
    #takes the transposition key and gets the corrdinate value for each letter,
    # returned in an array
    rows = 6
    columns = 6

    coordinates = []

    for letter in trans_key:
        for i in range(rows):
            for j in range(columns):
                if letter == SQUARE[i][j]:
                    addition = int(str(i) + str(j))
                    coordinates.append(addition)
    return coordinates


def one_pad_crypto_technique(coordinates, one_time_key):

    one_time_binary = dec_to_bin(int(one_time))

    coordinates_in_binary = []

    for item in coordinates:
        new_item = dec_to_bin(item)
        coordinates_in_binary.append(new_item)


    #XOR Operation

    final_ciphertext = ''

    for item in coordinates_in_binary:
        new_binary = ''
        for i in range(len(one_time_binary)):
            if item[i] != one_time_binary[i]:
                new_binary += '1'
            else:
                new_binary += '0'
        final_ciphertext += str(int(new_binary))

    return(final_ciphertext)



if __name__ == '__main__':

   comp_key = raw_input('Enter Composite Key: ')
   one_time = get_one_time_pad(comp_key)

   trans_key = polybius(comp_key[:-2])

   coordinates = get_coordinates(trans_key)

   print('Ciphertext: ', one_pad_crypto_technique(coordinates, one_time))
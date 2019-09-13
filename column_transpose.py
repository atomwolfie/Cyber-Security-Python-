import numpy as np

def sort_key(key):
    sorted_key = list(key)
    sorted_key.sort()
    sorted_key = ''.join(sorted_key)

    sorted_numbers = [key.index(i) for i in sorted_key]
    return sorted_key, sorted_numbers


def encode(key, plain_text):
    first = [[] for i in key]

    for i in range(len(plain_text)):
        first[i % len(key)].append(plain_text[i])
    
    skey, numbers = sort_key(key)
    final = [first[i] for i in numbers]
    print(first)
    return unwrap_matrix(final)

def decode(key, cipher_text):
    first = [[] for i in key]

    for i in range(len(cipher_text)):
        first[i % len(key)].append(cipher_text[i])

    skey, numbers = sort_key(key)

    final = [first[i] for i in numbers]
    
    return unwrap_matrix(final)

def unwrap_matrix(mat):
    zipped = zip(*[i for i in mat])
    return ''.join([''.join([i for i in j]) for j in mat])

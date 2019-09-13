import numpy as np
import itertools

def sort_key(key):
    sorted_key = list(key)
    sorted_key.sort()
    sorted_key = ''.join(sorted_key)

    sorted_numbers = [key.index(i) for i in sorted_key]
    return sorted_key, sorted_numbers


def encode(key, plain_text):
    first = wrap_text(plain_text, key)
    
    skey, numbers = sort_key(key)
    final = [first[i] for i in numbers]
    return unwrap_matrix(final)

def decode(key, cipher_text):
    first = wrap_text(cipher_text, key)

    skey, numbers = sort_key(key)
    
    final = [[] for i in key]
    for i in range(len(numbers)):
        final[numbers[i]] = first[i]
    
    return unwrap_matrix(final)


def test(key, plain):
    decoded = decode(key, encode(key, plain))
    assert plain == decoded

def unwrap_matrix(mat):
    zipped = itertools.zip_longest(*[i for i in mat], fillvalue='')
    return ''.join([''.join([i for i in j]) for j in zipped])

def wrap_text(text, key):
    ret = [[] for i in key]
    for i in range(len(text)):
        ret[i % len(key)].append(text[i])
    return ret

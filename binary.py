
''' 
Assignment 5
Author: Kaiwen Liu

'''

import itertools 

def zbits(n,k):
    """
	takes two arguments n and k and prints all binary strings of length n that contain k zero bits, one per line.
    
    """

    # Create a string with k zeros and another string with (n-k) ones
    zeros = "0" * k
    ones = '1' * (n-k)

    # combine the two strings to form the string
    string = zeros + ones

    # get permutations of the string, and return a set of the permutations
    permutation = itertools.permutations(string)
    return set(''.join(item) for item in permutation)


if __name__ == '__main__':
    print zbits(4,3)
    assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}, "failed first test"
    assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}, 'failed second test'
    assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}, 'failed third'
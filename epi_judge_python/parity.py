from test_framework import generic_test


def parity(x):

    isOdd = 0
    while x:
        x = x & (x - 1) # drops the lowest set bit
        isOdd ^= 1 # XOR with 1 to flip the bool each iteration

    return isOdd 


    


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))

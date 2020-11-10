from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    # check if bits at i and j are different, only then is a swap necessary
    if((x >> i) & 1 != (x >> j) & 1):
        #create bitmask
        bitmask = (1 << i) | (1 <<j)
        x = x ^ bitmask

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))

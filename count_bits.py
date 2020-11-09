from test_framework import generic_test


def count_bits(x: int) -> int:
    # TODO - you fill in here.
    count = 0
    while(x > 0):
        if(x % 2 == 1):
            count = count + 1
        x = x // 2
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))

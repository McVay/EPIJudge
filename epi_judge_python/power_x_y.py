from test_framework import generic_test


def power(x, y):

    # x = 2, y = 2 
    # 2 ^ 2 = 4
    # 10 ^ 10 = 100

    result, power = 1.0, y

    if y < 0:
        power, x = -power, 1.0 / x

    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))

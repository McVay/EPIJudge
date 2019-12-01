from test_framework import generic_test

def has_two_sum(A, t):


    left, right = 0, len(A) - 1
    while left <= right:
        currentSum = A[left] + A[right]
        if currentSum == t:
            return True
        elif currentSum > t:
            right -= 1
        else:
            left += 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))

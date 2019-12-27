# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
#
# Example 2:
#
# Input: -123
# Output: -321
#
# Example 3:
#
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
# range: [−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed
# integer overflows.

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # Method 1

    # signed = 1
    # if x < 0:
    #     signed = -1
    #     x = -1 * x
    # x = signed * int(str(x)[::-1])
    #
    # if x < -2**31 or x > 2**31 - 1:
    #     return 0
    # else:
    #     return x

    # Method 2
    signed = 1
    if x < 0:
        signed = -1
        x = -1 * x
    rev = 0
    while x != 0:
        pop = x % 10
        x = x // 10  # pop operation
        if signed * (rev * 10 + pop) < -2 ** 31 or signed * (rev * 10 + pop) > 2 ** 31 - 1:
            return 0
        rev = rev * 10 + pop  # push operation

    return signed * rev


n = -123
print(reverse(n))

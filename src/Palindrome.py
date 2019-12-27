class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        rev = 0

        # if first and last digit are not same then no need to reverse
        if str(x % 10) != str(x)[0]:
            return False

        while temp != 0:
            pop = temp % 10
            rev = rev * 10 + pop
            temp = temp // 10

        return rev == x


x = 12
o = Solution().isPalindrome(x)
print(o)

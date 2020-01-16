"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if needle == '':
            return 0
        h_len = len(haystack)
        n_len = len(needle)
        index = 0
        while index < h_len + n_len -1:
            print('{} == {}'.format(needle, haystack[index:index+n_len]))
            if needle == haystack[index:index+n_len]:
                return index
            index += 1

        return -1


obj = Solution()
o = obj.strStr("mississippi", "issi")
print(o)

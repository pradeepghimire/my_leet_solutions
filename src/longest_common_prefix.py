# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution(object):
    @classmethod
    def longestCommonPrefix(cls, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # ---------------------- rough solution --------------------------#
        # if len(strs) == 0:
        #     return ''
        # prefix = ''
        # done = False
        # i = 0
        # while not done:
        #     temp = ''
        #     for s in strs:
        #         if i == len(s):
        #             done = True
        #             break
        #         if temp == '':
        #             temp = s[i]
        #             continue
        #         if s[i] != temp:
        #             done = True
        #             break
        #         temp = s[i]
        #     if not done:
        #         prefix += temp
        #     i += 1
        # return prefix

        # ------------------------- horizontal scanning --------------------
        # if len(strs) == 0:
        #     return ''
        # prefix = strs[0]
        # i = 1
        # while i < len(strs):
        #     while strs[i][0:len(prefix)] != prefix:
        #         prefix = prefix[0:len(prefix)-1]
        #         if prefix == '':
        #             return ''
        #     i += 1
        # return prefix

        # --------------------------- vertical scanning ------------------
        if len(strs) == 0:
            return ''
        i = 0
        while i < len(strs[0]):
            j = 1
            while j < len(strs):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][0:i]
                j += 1
            i += 1
        return strs[0]


l = ["aa","ab"]
print (Solution.longestCommonPrefix(l))

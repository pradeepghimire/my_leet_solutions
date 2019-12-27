# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution(object):
    @staticmethod
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # if length == 0:
        #     return True
        # if length % 2 != 0:
        #     return False
        h = {
            '{': '}', '[': ']', '(': ')', '}': False, ']': False, ')': False
             }
        #
        # for i, ch in enumerate(s):
        #     if i == length//2:
        #         break
        #     if not h[ch]:
        #         return False
        #     if h[ch] != s[length - (i+1)]:
        #         return False

        # push pop is the way
        h = {
            '{': '}', '[': ']', '(': ')', '}': False, ']': False, ')': False
             }
        arr = []
        for  ch in s:
            if len(arr) == 0:
                arr.append(ch)
            else:
                pop = arr.pop()
                if not h[pop]:
                    return False
                if ch != h[pop]:
                    arr.append(pop)
                    arr.append(ch)
                else:
                    pass

        if len(arr) == 0:
            return True
        else:
            return False


# print (Solution.isValid('{[({]})]}'))
print (Solution.isValid('([[])[]{}'))

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Brute force solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         indices = []
#         br = False
#         length = len(nums)
#         i = 0
#         while i < length:
#             j = i + 1
#             while j < length:
#                 if nums[i] + nums[j] == target:
#                     indices = [i, j]
#                     br = True
#                     break
#                 j += 1
#             if br:
#                 break
#             i += 1
#         return indices


# hash table implementation

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h_table = {}    # hash table for mapping number with its index
        for index, num in enumerate(nums):
            n = target - num
            if n in h_table:
                return [index, h_table[n]]
            h_table[num] = index
            print(h_table)


obj = Solution()
solutions = obj.twoSum([1, 2, 3, 5, 8], 10)
print(solutions)

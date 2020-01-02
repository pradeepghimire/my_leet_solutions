# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
# the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    head = node = ListNode(0)
    node.next = ListNode(2)
    print(node)
    print

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # arr = []
        # merged_list = ListNode(None)
        # if l1 is None and l2 is None:
        #     # merged_list = ListNode(None)
        #     return merged_list
        #
        # stop = False
        # while not stop:
        #     if l1 is None and l2 is None:
        #         stop = True
        #     if l1.val <= l2.val:
        #         arr.append(l1.val)
        #         arr.append(l2.val)
        #     else:
        #         arr.append(l2.val)
        #         arr.append(l1.val)
        #     l1 = l1.next
        #     l2 = l2.next
        #
        # pop = arr.pop()
        # merged_list.val = pop
        # while len(arr) != 0:
        #     pass

# l1_3 = ListNode(4)
# l1_2 = ListNode(2)
# l1 = ListNode(1)
# l1.next = l1_2
# l1_2.next = l1_3
#
# l2_3 = ListNode(4)
# l2_2 = ListNode(3)
# l2 = ListNode(1)
# l2.next = l2_2
# l2_2.next = l2_3
#
# print(Solution().mergeTwoLists(l1, l2))

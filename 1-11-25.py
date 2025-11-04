# 1 November 2025

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        itr = ListNode(val = -1, next = head)
        head = itr
        prev = itr
        while itr:
            if itr.val in nums:
                prev.next = itr.next
                itr = itr.next
            else:
                prev = itr
                itr = itr.next
        return head.next
        
# just iterating and comparing while maintaining the prev, class linkedlist problem

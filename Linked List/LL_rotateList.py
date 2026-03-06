class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return None
        count = 0
        itr = head
        while itr:
            count = count+1
            itr = itr.next
        k = k%count
        while k > 0:
            itr = head
            while itr.next:
                if itr.next.next is None:
                    a = ListNode(itr.next.val, head)
                    head = a
                    itr.next = None
                    continue
                itr = itr.next
            k = k-1
        return head
            


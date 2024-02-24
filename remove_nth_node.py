class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
  
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
  
        if n <= 0 or n > length:
            return None
  
        if length == n:
            return head.next
  
        current = head
        for _ in range(length - n - 1):
            if current:
                current = current.next
            else:
                return None  
  
        if current and current.next:
            current.next = current.next.next
  
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next #fast = 2nd list tail
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #second = 2nd list pointer
        slow.next = None #slow = 1st list tail

        #reverse second list
        prev = None #head of reversed list
        curr = second

        while curr:
            nxt = curr.next #temporarily store remaining list
            curr.next = prev #change pointer of current
            prev = curr #move prev one step forward
            curr = nxt #move curr one step forward
        
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        
            
        
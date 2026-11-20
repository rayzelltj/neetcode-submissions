# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next
        counter = 1
        l = 0
        r = len(nodes)-1
        current = head
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l == r:
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[l].next = None

        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(next=head)
        p_prev = head
        p = p_prev.next
        while p.next is not None:
            q_prev = sentinel
            q = q_prev.next
            while q.val < p.val:
                q_prev = q_prev.next
                q = q.next
            q_prev.next = p
            p_prev.next = p.next
            p.next = q
            p_prev = p_prev.next
            p = p_prev.next
        return sentinel.next





def toList(arr):
    head = ListNode(arr[0])
    p = head
    for i in range(1, len(arr)):
        p.next = ListNode(arr[i])
        p = p.next
    return head

def printList(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
        print('XD')
    print(arr)

Solution().insertionSortList(toList([4,2,1,3]))
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        if head.next.next is None:
            if head.val < head.next.val:
                return head
            else:
                head.next.next = head
                temp = head.next
                head.next = None
                return temp
        l_last = self.get_middle(head)
        r_head = l_last.next
        l_last.next = None
        head = self.sortList(head)
        r_head = self.sortList(r_head)
        return self.merge(head, r_head)

    def merge(self, q, p):
        dummy = ListNode(next=q)
        q = dummy
        while q.next and p:
            if p.val < q.next.val:
                prev_q_next = q.next
                prev_p_next = p.next
                q.next = p
                p.next = prev_q_next
                q = p
                p = prev_p_next
            else:
                q = q.next
        if p:
            q.next = p
        return dummy.next


    def get_middle(self, p):
        fast = p
        while fast and fast.next:
            fast = fast.next.next
            p = p.next
        return p

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
    print(arr)

Solution().sortList(toList([-1,5,3,4,0]))

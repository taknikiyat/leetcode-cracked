# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(m+n) time | O(max(m,n)) space
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_list = ListNode()
        cur = sum_list
        
        carry = 0
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            # add digits
            result = digit1 + digit2 + carry
            carry = result // 10
            result = result % 10
            cur.next = ListNode(result)
            
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return sum_list.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recAddTwoNumbers(self, l1: ListNode | None, l2: ListNode | None, sum_node: ListNode | None, carry: int):
        if l1 is None and l2 is None:
            if carry:
                sum_node.next = ListNode(carry)
            return

        if l1 is not None:
            val1 = l1.val
        else:
            val1 = 0
        if l2 is not None:
            val2 = l2.val
        else:
            val2 = 0

        total = val1 + val2 + carry
        digit = total%10
        carry = total//10
        sum_node.next = ListNode(digit)
        self.recAddTwoNumbers(
            l1.next if l1 is not None else None,
            l2.next if l2 is not None else None,
            sum_node.next,
            carry,
        )

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        sum_node = ListNode()
        total = l1.val + l2.val
        digit = total%10
        carry = total//10
        sum_node.val = digit
        self.recAddTwoNumbers(l1.next, l2.next, sum_node, carry)
        return sum_node

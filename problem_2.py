# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        # we need to take the first value, add and move to next if extra we carry

        carry = 0

        result = ListNode()

        tail = result

        while (l1 is not None or l2 is not None) or carry > 0:
            # the 1 and 2 in value is a list differentiator and not the value index
            if l1 is not None:
                value_1 = l1.val
            else:
                value_1 = 0

            if l2 is not None:
                value_2 = l2.val
            else:
                value_2 = 0

            answer_state_1 = value_1 + value_2 + carry
            carry = answer_state_1 // 10
            write = answer_state_1 % 10

            l = ListNode(write)
            tail.next = l
            tail = tail.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return result.next

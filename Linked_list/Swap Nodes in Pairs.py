"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
from Linked_list.helper import ListNode, create_linked_list


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        swapped = head

        def swap(head):
            if not head:
                return
            next_head = head.next
            if not next_head:
                return
            head.val, next_head.val = next_head.val, head.val
            head = next_head.next
            swap(head)
        swap(head)
        return swapped


"""
Runtime: O(n/2)
"""
if __name__ == "__main__":
    linked = [1, 2, 3, 4]
    lol = Solution()
    linked_list = create_linked_list(linked)
    print(lol.swapPairs(linked_list))

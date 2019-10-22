"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
from Linked_list.helper import ListNode, create_linked_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        deduped = head
        while head and head.next:
            next_head = head.next
            while head.val == next_head.val:
                next_head = next_head.next
                if not next_head:
                    break
            head.next = next_head
            head = head.next
        return deduped


"""
Runtime: O(n)
"""
if __name__ == "__main__":
    lol = Solution()
    values = [1,1,1,2 , 4]
    nodes = create_linked_list(values)
    print(lol.deleteDuplicates(nodes))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        val_list = [str(self.val)]
        node = self.next
        while node:
            val_list.append(str(node.val))
            node = node.next
        return "->".join(val_list)


def create_linked_list(list):
    tail = ListNode(list[0])
    head = tail
    for index in range(1, len(list)):
        node = ListNode(list[index])
        tail.next = node
        tail = tail.next
    return head

class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def swap_pairs(head):
    if not head or not head.next:
        return head

    next_node = head.next
    head.next = swap_pairs(next_node.next)
    next_node.next = head

    return next_node

def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

head = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
print("Оригінальний список:")
print_list(head)
new_head = swap_pairs(head)
print("\nСписок після заміни пар:")
print_list(new_head)
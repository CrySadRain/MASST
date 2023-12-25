class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_list():
    values = list(map(int, input("Введіть значення вузлів: ").split()))
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def print_list(head):
    current = head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

def reorder_list(head):
    if not head or not head.next:
        return

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow.next
    slow.next = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

    return head

head = create_list()
print("Вхідний список:")
print_list(head)

head = reorder_list(head)

print("Вихідний список:")
print_list(head)
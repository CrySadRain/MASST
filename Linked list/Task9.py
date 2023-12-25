class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def partition(head, x):
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head

    current = head
    while current:
        if current.value < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next

        current = current.next

    before.next = after_head.next
    after.next = None

    return before_head.next

def create_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

input_values = input("Введіть значення списку: ")
values = [int(x) for x in input_values.split()]

x = int(input("Введіть значення x: "))

head = create_list(values)
result_head = partition(head, x)
result_list = list_to_list(result_head)
print(result_list)


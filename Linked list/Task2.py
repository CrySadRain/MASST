class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return head

def sort_list(head):
    values = []
    current = head

    while current:
        values.append(current.value)
        current = current.next

    values.sort()

    sorted_head = ListNode()
    current = sorted_head

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return sorted_head.next

def print_list(head):
    current = head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

def input_list():
    values = input("Введіть відсортований список: ").split()
    values = [int(value) for value in values]
    result_head = ListNode()
    current = result_head

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return result_head.next

head = input_list()

print("Введений список:")
print_list(head)

sorted_head = sort_list(head)
print("Відсортований список:")
print_list(sorted_head)

delete_duplicates(head)

sorted_head = sort_list(head)

print("Список після видалення дублікатів та впорядкування:")
print_list(sorted_head)
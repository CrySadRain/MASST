class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_lists(l1, l2):
    result_head = ListNode()
    current = result_head

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return result_head.next

def merge_k_lists(lists):
    if not lists:
        return None

    merged_list = lists[0]
    for i in range(1, len(lists)):
        merged_list = merge_two_lists(merged_list, lists[i])

    return merged_list

def create_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

lists = []
k = int(input("Введіть кількість відсортованих списків (k): "))

for i in range(k):
    values = input(f"Введіть відсортований список {i + 1}: ").split()
    linked_list = create_list([int(value) for value in values])
    lists.append(linked_list)

result = merge_k_lists(lists)

result_array = []
while result:
    result_array.append(result.value)
    result = result.next

result_array.sort()
print("Відсортований результат об'єднання відсортованих списків:")
print(result_array)

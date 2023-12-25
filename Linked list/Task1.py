class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

def merge_sorted_lists(list1, list2):
    placeholder = ListNode()
    current = placeholder

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next_node = list1
            list1 = list1.next_node
        else:
            current.next_node = list2
            list2 = list2.next_node

        current = current.next_node

    if list1 is not None:
        current.next_node = list1
    elif list2 is not None:
        current.next_node = list2

    return placeholder.next_node

def create_list():
    values = input().split()
    values = [int(value) for value in values]
    nodes = [ListNode(value) for value in values]

    for i in range(len(nodes) - 1):
        nodes[i].next_node = nodes[i + 1]

    return nodes[0] if nodes else None

print("Введіть значення для першого відсортованого списку:")
list1 = create_list()

print("Введіть значення для другого відсортованого списку:")
list2 = create_list()

result = merge_sorted_lists(list1, list2)

result_values = []
while result is not None:
    result_values.append(result.value)
    result = result.next_node

result_values.sort(reverse=True) 

print("Результат об'єднання та сортування відсортованих списків:")
print(result_values)
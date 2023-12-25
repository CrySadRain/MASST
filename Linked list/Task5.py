class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next

def create_list():
    values = list(map(int, input("Введіть елементи списку: ").split()))
    head = ListNode(values[0])
    current_node = head
    for value in values[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return head

def print_list(head):
    current_node = head
    while current_node:
        print(current_node.value, end=" ")
        current_node = current_node.next
    print()

head = create_list()
node_to_delete_value = int(input("Введіть значення вузла, який потрібно видалити: "))
current_node = head
while current_node.next.value != node_to_delete_value:
    current_node = current_node.next
node_to_delete = current_node.next

delete_node(node_to_delete)

print("Результат після видалення вузла:")
print_list(head)

# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def get_node_by_index(node, index):
        while index:
            node = node.next
            index -= 1
        return node

    def insert_node(head, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = head
            return new_node
        previous_node = Node.get_node_by_index(head, index - 1)
        new_node.next = previous_node.next
        previous_node.next = new_node
        return head

    def solution(node, idx):
        while node:
            print(node.value)
            node = node.next_item


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = Node.solution(node0, 1)
    # result is node0 -> node2 -> node3


test()

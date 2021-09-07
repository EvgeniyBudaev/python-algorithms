# Comment it before submitting
# class Node:  
#     def __init__(self, value, next_item=None):  
#         self.value = value  
#         self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        head = node.next_item
        return head
    else:
        head = node
    while idx-1:
        if node.next_item is not None:
            node = node.next_item
        else:
            return head
        idx -= 1
    node.next_item = node.next_item.next_item
    return head

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # result is node0 -> node2 -> node3
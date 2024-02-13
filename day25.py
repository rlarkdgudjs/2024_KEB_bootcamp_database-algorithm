import random

class Node:
    def __init__ (self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
    print()


def count(start):
    global count ,remainder
    current = start
    count = 0
    if current.data % 2 == 0:
        count = count + 1
    while current.link != start:
        current = current.link
        if current.data % 2 == 0:
            count = count + 1
    if count > 7-count:
        remainder = 0
    else:
        remainder = 1

def temp(start):
    global current
    current = start
    if current.data % 2 == remainder:
        current.data = -current.data
    while current.link != start:
        current = current.link
        if current.data % 2 == remainder:
            current.data = -current.data


head, current, pre = None, None, None
data_array = []
for i in range(7):
    data_array.append(random.randint(1, 100))

if __name__ == "__main__":

    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    print_nodes(head)

    count(head)
    temp(head)

    print_nodes(head)
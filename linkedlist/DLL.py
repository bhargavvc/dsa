class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        arry = []
        while temp is not None:
            arry.append(temp.value)
            temp = temp.next
        return arry

    def get_fully_nested_structure(self):
        def node_to_dict(node, visited):
            if node is None or node in visited:
                return None
            visited.add(node)
            return {
                "value": node.value,
                "prev": node_to_dict(node.prev, visited),  # Handle previous node
                "next": node_to_dict(node.next, visited),  # Handle next node
            }

        visited = set() 

        return {
            "head": node_to_dict(self.head, visited),
            "tail": node_to_dict(self.tail, visited),
        }

    def get_index(self, index):

        if index < 0 or index >= self.length:
            return None

        if index < (self.length // 2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1  #
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop(self):

        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None  #
        self.length -= 1
        return temp.value

    def popfirst(self):

        if self.head is None or self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp.value

    def set_value(self, index, value):
        temp = self.get_index(index)
        if temp:
            temp.value = value
        return True

    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)

        temp = self.get_index(index)

        prev = temp.prev
        prev.next = new_node

        new_node.prev = prev
        new_node.next = temp

        temp.prev = new_node

        self.length += 1
        return True


my_dll = DoubleLinkedList(7)

my_dll.append(5)
my_dll.append(6)
my_dll.append(8)
my_dll.append(9)
my_dll.prepend(1)
my_dll.prepend(2)
my_dll.prepend(3)

# my_dll.pop()
# my_dll.popfirst()

# print(my_dll.get_index(0))
# print(my_dll.set_value(1,100))
print("prev Inser", my_dll.print_list())

print(my_dll.insert(1, 100))


print("After Inser", my_dll.print_list())

print(my_dll.get_fully_nested_structure())

print(True)

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        node_value = new_node.value
        while True:
            """
            Why while True.
            when you find a place to insert the new node >as we dont know the location so iterating till best location.
            Loop continue until you find the correct location for insertion.

            2. while temp is not None
            this could also work but we need to set true when we find location or reached end of tree.
            """
            if node_value == temp.value:
                return False
            if node_value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if node_value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return None

        temp = self.root
        while temp is not None:
            '''
            temp is not None:
            This is typically used when you have a clear stopping point
                defined by the iterable itself (like while temp is not None)
            '''
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


bst = BinarySearchTree()

bst.insert(2)
bst.insert(1)
bst.insert(3)

# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
print(bst.contains(3))


'''
### `insert` Method
- **Using `while True`**:
  - The reason for using `while True` in the `insert` method is that you are traversing the tree to find the correct insertion point.
    Since you don't know beforehand where that point will be, the loop continues indefinitely until a return statement is reached.

### `contains` Method
- **Using `while temp is not None`**:
    The stopping condition (`temp is not None`) indicates that
    you will stop traversing when you reach a node that doesn't exist (i.e., when `temp` becomes `None`).

  - **when there are no more nodes to check or loop to continue , when you know the value is not present.

### Summary of Key Points:
- **When to Use `while True`**:
  - Useful for scenarios where multiple paths can lead to an exit, such as finding an insertion point.

- **When to Use `while <condition>`**:
  - When you have a clear stopping point defined by a condition, such as the end of a list or tree.

'''



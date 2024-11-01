class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):

        temp = self.head
        while temp.next:
            yield temp
            temp = temp.next

    def _iterate_from(self, node):
        """Helper method to iterate and collect values from a given node."""
        result = []
        while node:
            result.append(node)
            node = node.next
        return result

    # Pop the last element
    def pop_last(self):
        if self.length == 0:  # If the list is empty
            return None

        temp = self.head
        prev = self.head

        # Loop through to find the last element and its previous one
        while temp.next:
            prev = temp
            temp = temp.next

        # If there's only one element in the list
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.tail = prev  # Set the new tail
            self.tail.next = None  # Remove the reference to the old last node

        self.length -= 1

        # Return the value of the removed node
        return temp.value

    # Prepend a new value to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:  # If the list is empty
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head  # Link new node to the current head
            self.head = new_node  # Set new head

        self.length += 1
        return True

    # Append a new value to the end of the list
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:  # If the list is empty
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node  # Link the old tail to the new node
            self.tail = new_node  # Set the new tail

        self.length += 1
        return True

    # Pop the first element from the list
    def pop_first(self):
        if self.length == 0:  # If the list is empty
            return None

        temp = self.head  # Store the current head to return later
        self.head = self.head.next  # Move head to the next node

        self.length -= 1

        # If the list becomes empty, set tail to None
        if self.length == 0:
            self.tail = None

        return temp.value  # Return the value of the removed node

    def get_index(self, index):
        if index < 0 or index >= self.length:  # Check if index is out of bounds
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next  # Traverse to the node at the given index

        return temp

    def set_index(self, index, value):
        temp = self.get_index(index)  # Fetch the node at the given index

        if temp:  # If the node is found, update its value
            temp.value = value
            return True

        return False  # If the node is not found, return False

    def insert(self, index, value):
        if index < 0 or index > self.length:  # Check if index is out of bounds
            return False

        new_node = Node(value)

        if index == 0:
            return self.prepend(value)  # Insert at the beginning
        if index == self.length:
            return self.append(value)  # Insert at the end

        # Insert in the middle
        temp = self.get_index(index - 1)  # Get the node just before the index
        new_node.next = temp.next  # Link new node to the next node
        temp.next = new_node  # Update previous node to link to new node
        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:  # Correct index bounds check
            return False

        if index == 0:
            return self.pop_first()  # Remove the first node
        if index == self.length - 1:
            return self.pop_last()  # Remove the last node

        # Remove from the middle
        prev = self.get_index(index - 1)  # Get the node before the one to be removed
        temp = prev.next  # Get the node to be removed
        prev.next = temp.next  # Bypass the node to be removed
        temp.next = None # removes the item from the list
        self.length -= 1

        return temp.value  # Return the value of the removed node
    
    #very very important
    def reverse(self):
        import pdb;pdb.set_trace()
        prev = None
        current = self.head
        self.tail = current   # The original head will become the new tail aftyer reversal
        while current is not None:
            print("Current list: ", [node.value for node in self._iterate_from(current)])
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev to the current node
            current = next_node  # Move to the next node
        
        self.head = prev   # The new head is the last node processed

        '''
        for first iteration completes
        current and next_node points to the same Node
        but second iteration before and cuurent points to same node before it reaches to current = next_node
        
        '''
      

# Create an empty linked list
linked_list = SingleLinkedList()

# Append values to the list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)


# Prepend a value to the list

# Pop the first element
# print(linked_list.pop_first())  # Output: 5

# Pop the last element
# print(linked_list.pop_last())  # Output: 30

# print([node.value for node in linked_list])
linked_list.reverse()

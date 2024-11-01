from typing import Any

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Points to the next node in the list


class HashTableWithLinkedList:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key: str) -> int:
        """
        Private method to calculate a hash for the given key.
        """
        my_hash = 0
        len_of_table = len(self.data_map)
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len_of_table
        return my_hash

    def print_table(self):
        """
        Method to print the contents of the hash table.
        """
        for index, value in enumerate(self.data_map):
            chain = []
            current = value
            while current:
                chain.append(f"({current.key}: {current.value})")
                current = current.next
            print(f"{index} : {' -> '.join(chain) if chain else None}")

    def set_item(self, key: str, value: Any):
        """
        Method to add a key-value pair to the hash table.
        """
        index = self.__hash(key)
        new_node = Node(key, value)

        # If no linked list at this index, create one
        if self.data_map[index] is None:
            self.data_map[index] = new_node
        else:
            # Traverse to the end of the linked list and append
            current = self.data_map[index]
            while current.next is not None:
                if current.key == key:  # Overwrite value if key exists
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node  # Add new node at the end

    def get_item(self, key: str) -> Any:
        """
        Method to retrieve a value based on the key from the hash table.
        """
        index = self.__hash(key)
        current = self.data_map[index]

        while current:
            if current.key == key:
                return current.value  # Return the value if key matches
            current = current.next

        return None  # Return None if key not found


# Create a hash table and add key-value pairs
my_ht_linked_list = HashTableWithLinkedList()
my_ht_linked_list.set_item("a", "apple")
my_ht_linked_list.set_item("b", "banana")
my_ht_linked_list.set_item("c", "cat")
my_ht_linked_list.set_item("a", "animal")  # Collision on key "a"
my_ht_linked_list.set_item("d", "dog")

# Print the hash table to see the internal structure (linked lists)
my_ht_linked_list.print_table()

# Retrieve items
print(my_ht_linked_list.get_item("a"))  # Should return "animal"
print(my_ht_linked_list.get_item("b"))  # Should return "banana"
print(my_ht_linked_list.get_item("d"))  # Should return "dog"
print(my_ht_linked_list.get_item("e"))  # Should return None (key not found)

from typing import Any

class HashTableWithLinearProbing:
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
            print(f"{index} : {value}")

    def set_item(self, key: str, value: Any):
        """
        Method to add a key-value pair to the hash table using linear probing.
        """
        index = self.__hash(key)

        # Linear probing: Find the next available slot if a collision occurs
        while self.data_map[index] is not None:
            if self.data_map[index][0] == key:
                # If the key already exists, overwrite the value
                self.data_map[index] = (key, value)
                return
            index = (index + 1) % len(self.data_map)  # Move to the next index

        # Place the key-value pair in the found index
        self.data_map[index] = (key, value)

    def get_item(self, key: str) -> Any:
        """
        Method to retrieve a value based on the key from the hash table using linear probing.
        """
        index = self.__hash(key)

        # Linear probing: Search for the key
        while self.data_map[index] is not None:
            if self.data_map[index][0] == key:
                return self.data_map[index][1]  # Return the value if key matches
            index = (index + 1) % len(self.data_map)  # Move to the next index

        return None  # Return None if key not found


# Create a hash table and add key-value pairs
my_ht_linear_probing = HashTableWithLinearProbing()
my_ht_linear_probing.set_item("a", "apple")
my_ht_linear_probing.set_item("b", "banana")
my_ht_linear_probing.set_item("c", "cat")
my_ht_linear_probing.set_item("a", "animal")  # Overwrite key "a" with new value
my_ht_linear_probing.set_item("d", "dog")

# Print the hash table to see the internal structure
my_ht_linear_probing.print_table()

# Retrieve items
print(my_ht_linear_probing.get_item("a"))  # Should return "animal"
print(my_ht_linear_probing.get_item("b"))  # Should return "banana"
print(my_ht_linear_probing.get_item("d"))  # Should return "dog"
print(my_ht_linear_probing.get_item("e"))  # Should return None (key not found)

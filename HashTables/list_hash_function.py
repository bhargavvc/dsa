from typing import Any, List, Tuple

class HashTable:
    def __init__(self, size: int = 7):
        # Initialize the hash table with 'None' values
        self.data_map: List[List[Tuple[str, Any]]] = [None] * size

    def __hash(self, key: str) -> int:
        """
        Private method to hash the key.
        """
        my_hash = 0
        len_of_table = len(self.data_map)
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len_of_table
        return my_hash

    def print_table(self):
        """
        Method to print the entire hash table.
        """
        for index, value in enumerate(self.data_map):
            print(f"{index} : {value}")

    def set_item(self, key: str, value: Any) -> bool:
        """
        Method to insert a key-value pair into the hash table.
        """
        index = self.__hash(key)

        if self.data_map[index] is None:
            # Initialize a list at the index if it's None
            self.data_map[index] = []
        
        # Check if the key already exists, update if found
        for i, (existing_key, existing_value) in enumerate(self.data_map[index]):
            if existing_key == key:
                self.data_map[index][i] = (key, value)  # Update the value for the existing key
                return True
        
        # Append new key-value pair if key does not exist
        self.data_map[index].append((key, value))
        return True

    def get_item(self, key: str) -> Any:
        """
        Method to retrieve a value based on the key.
        """
        index = self.__hash(key)

        if self.data_map[index] is None:
            return None  # Key not found

        # Iterate through the list at the index to find the key
        for existing_key, value in self.data_map[index]:
            if existing_key == key:
                return value  # Return the value if the key matches

        return None  # Return None if the key is not found at the index



# Create an instance of HashTable
my_ht = HashTable()

# Intentionally adding keys that will likely cause collisions
my_ht.set_item("apple", "fruit")
my_ht.set_item("elppa", "reversed fruit")
my_ht.set_item("pplea", "anagram fruit")

# Add more items to cause further collisions
my_ht.set_item("bottle", "container")
my_ht.set_item("otbel", "reversed container")

# Print the hash table to observe collisions
my_ht.print_table()

# Retrieve values to ensure collision handling works
print("\nRetrieving items:")
print(my_ht.get_item("apple"))   # Should return "fruit"
print(my_ht.get_item("elppa"))   # Should return "reversed fruit"
print(my_ht.get_item("pplea"))   # Should return "anagram fruit"
print(my_ht.get_item("bottle"))  # Should return "container"
print(my_ht.get_item("otbel"))   # Should return "reversed container"
print(my_ht.get_item("non_existent"))  # Should return None
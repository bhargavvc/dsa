from typing import Any

class HashTableWithDict:
    def __init__(self, size=7):
        # Initialize the hash table with None entries of specified size
        self.data_map = [None] * size

    def __hash(self, key: str) -> int:
        """
        Private method to calculate a hash for the given key
        """
        my_hash = 0
        len_of_table = len(self.data_map)
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len_of_table
        return my_hash

    def print_table(self):
        """
        Method to print the contents of the hash table
        """
        for index, value in enumerate(self.data_map):
            print(f"{index} : {value}")

    def set_item(self, key: str, value: Any) -> bool:
        """
        Method to add a key-value pair to the hash table
        """
        index = self.__hash(key)
        if self.data_map[index] is None:
            # Instead of a list, we now initialize an empty dictionary for each index
            self.data_map[index] = {}
        # Store the key-value pair in the dictionary at the hashed index
        self.data_map[index][key] = value
        return True
    
    def get_item(self, key: str) -> Any:
        """
        Method to retrieve a value based on the key from the hash table
        """
        index = self.__hash(key)
        if self.data_map[index] is not None:
            # Retrieve the value directly from the dictionary
            return self.data_map[index].get(key, None)
        return None  # Return None if the key or index doesn't exist

# Create a hash table and add key-value pairs
my_ht_dict = HashTableWithDict()
my_ht_dict.set_item("a", "apple")
my_ht_dict.set_item("b", "banana")
my_ht_dict.set_item("c", "cat")
my_ht_dict.set_item("a", "animal")  # This will overwrite "apple" for the key 'a'

# Print the hash table to see the internal structure
my_ht_dict.print_table()

# Retrieve items
print(my_ht_dict.get_item("a"))  # Should return "animal"
print(my_ht_dict.get_item("b"))  # Should return "banana"
print(my_ht_dict.get_item("c"))  # Should return "cat"
print(my_ht_dict.get_item("d"))  # Should return None (key not found)

from typing import Any
class HashTableWithDictCollision:
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
        
        # If there's no dictionary at this index, initialize a list to handle collisions
        if self.data_map[index] is None:
            self.data_map[index] = []
        
        # Check if the key already exists in the dictionary (to prevent duplicate keys)
        for item in self.data_map[index]:
            if key in item:
                # If key already exists, update the value
                item[key] = value
                return True
        
        # If the key doesn't exist, append a new dictionary containing the key-value pair
        self.data_map[index].append({key: value})
        return True
    
    def get_item(self, key: str) -> Any:
        """
        Method to retrieve a value based on the key from the hash table
        """
        index = self.__hash(key)
        # Ensure the index is not empty
        if self.data_map[index] is not None:
            # Search through the list of dictionaries for the matching key
            for item in self.data_map[index]:
                if key in item:
                    return item[key]  # Return the value if key matches
        return None  # Return None if key not found

# Create a hash table and add key-value pairs
my_ht_dict_collision = HashTableWithDictCollision()
my_ht_dict_collision.set_item("a", "apple")
my_ht_dict_collision.set_item("b", "banana")
my_ht_dict_collision.set_item("c", "cat")
my_ht_dict_collision.set_item("a", "animal")  # Collision: overwrites "apple" for the key 'a'
my_ht_dict_collision.set_item("d", "dog")  # Another key at the same hashed index

# Print the hash table to see the internal structure
my_ht_dict_collision.print_table()

# Retrieve items
print(my_ht_dict_collision.get_item("a"))  # Should return "animal"
print(my_ht_dict_collision.get_item("b"))  # Should return "banana"
print(my_ht_dict_collision.get_item("c"))  # Should return "cat"
print(my_ht_dict_collision.get_item("d"))  # Should return "dog"
print(my_ht_dict_collision.get_item("e"))  # Should return None (key not found)

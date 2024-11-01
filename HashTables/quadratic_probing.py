from typing import Any

class HashTableWithQuadraticProbingDict:
    def __init__(self, size=7):
        self.data_map = [None] * size
        self.size = size

    def __hash(self, key: str) -> int:
        """
        Private method to calculate a hash for the given key.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % self.size
        return my_hash

    def print_table(self):
        """
        Method to print the contents of the hash table.
        """
        for index, value in enumerate(self.data_map):
            print(f"{index} : {value}")

    def set_item(self, key: str, value: Any):
        """
        Method to add a key-value pair to the hash table using quadratic probing.
        """
        index = self.__hash(key)
        original_index = index  # Keep track of the original hashed index
        i = 0

        # Quadratic probing: Find the next available slot if a collision occurs
        while self.data_map[index] is not None:
            existing_key, _ = self.data_map[index]
            if existing_key == key:
                # If the key already exists, overwrite the value
                self.data_map[index] = (key, value)
                return
            i += 1
            index = (original_index + i**2) % self.size  # Quadratic probing step
            if index == original_index:
                raise Exception("Hash table is full")

        # Place the key-value pair in the found index
        self.data_map[index] = (key, value)

    def get_item(self, key: str) -> Any:
        """
        Method to retrieve a value based on the key from the hash table using quadratic probing.
        """
        index = self.__hash(key)
        original_index = index
        i = 0

        # Quadratic probing: Search for the key
        while self.data_map[index] is not None:
            existing_key, value = self.data_map[index]
            if existing_key == key:
                return value  # Return the value if key matches
            i += 1
            index = (original_index + i**2) % self.size
            if index == original_index:
                break

        return None  # Return None if key not found


# Create a hash table with quadratic probing
my_ht_quadratic_probing_dict = HashTableWithQuadraticProbingDict()
my_ht_quadratic_probing_dict.set_item("a", "apple")
my_ht_quadratic_probing_dict.set_item("b", "banana")
my_ht_quadratic_probing_dict.set_item("c", "cat")
my_ht_quadratic_probing_dict.set_item("a", "animal")  # Overwrite key "a"
my_ht_quadratic_probing_dict.set_item("d", "dog")

# Print the hash table to see the internal structure
my_ht_quadratic_probing_dict.print_table()

# Retrieve items
print(my_ht_quadratic_probing_dict.get_item("a"))  # Should return "animal"
print(my_ht_quadratic_probing_dict.get_item("b"))  # Should return "banana"
print(my_ht_quadratic_probing_dict.get_item("d"))  # Should return "dog"
print(my_ht_quadratic_probing_dict.get_item("e"))  # Should return None (key not found)


dict()
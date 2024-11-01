
### Why Use a Prime Number for Hash Table Size?

**Clustering** occurs when multiple keys hash to the same index, leading to a situation where certain areas of the hash table are filled while others remain empty. This can degrade performance during operations like insertion, search, and deletion.

1. **Fewer Divisors**:
   - Prime numbers have only two divisors: 1 and themselves. This property minimizes the chances of multiple keys hashing to the same index.

2. **Even Distribution**:
   - Using a prime number in the hash table size can help achieve a more uniform distribution of hashed values, especially when keys exhibit patterns that could lead to clustering.


- Using a prime number for the hash table size improves the randomness and even distribution of hashed keys.


### Why Use Modulo?

- **Modulo Operation**: The modulo operator (%) returns the remainder of the division. It effectively restricts values to a specified range.

#### Examples of Modulo Output
- `print(132432124 % 334)` gives a result between `0` and `333` (since you're dividing by `334`).
- `print(132432124 % 10)` gives a result between `0` and `9`.
- `print(132432124 % 5)` gives a result between `0` and `4`.

### Use in  Hash Function
if take 7 (lenght of hash table size)

- The modulo operation restricts hash values to a specific range(here in case 0-7), which helps ensure that all keys map to indices within the hash table.


### Examples
two scenarios: one using a prime number and one using a composite number.

#### Example 1: Using a Prime Number

**Hash Table Size**: 7 (a prime number)

- **Keys to Insert**: `"apple"`, `"banana"`, `"grape"`, `"kiwi"`, `"orange"`

Assume a simple hash function like:

```python
hash_value = sum(ord(char) for char in key) % 7
```

- **Hash Values**:
  - `"apple"` → 5
  - `"banana"` → 0
  - `"grape"` → 4
  - `"kiwi"` → 2
  - `"orange"` → 6

**Hash Table**:
```
Index: 0   1   2   3   4   5   6
       [b] None [k] None [g] [a] [o]
```

In this case, the keys are spread out fairly evenly across the table.

#### Example 2: Using a Composite Number

**Hash Table Size**: 8 (a composite number)

- **Keys to Insert**: `"apple"`, `"banana"`, `"grape"`, `"kiwi"`, `"orange"`

Using the same hash function:

- **Hash Values**:
  - `"apple"` → 5
  - `"banana"` → 0
  - `"grape"` → 4
  - `"kiwi"` → 2
  - `"orange"` → 0 (collision with `"banana"`)

**Hash Table**:
```
Index: 0   1   2   3   4   5   6   7
       [b] None [k] None [g] [a] None None
       [o] (collision)
```

In this case, you see a collision at index 0, which means that both `"banana"` and `"orange"` hash to the same index. This can lead to clustering if more keys collide at the same index.


### Best DataStructure to Handle collisions in hash tables
### which one to use ?
- **Use Lists (or Linked Lists)**:
  - If you prefer a simpler implementation and your use case can tolerate O(n) lookups.
  - If maintaining the order of entries is important.

- **Use Dictionaries**:
  - If you want faster lookups and can afford the additional memory overhead.
  - If you're dealing with scenarios where keys may collide frequently.

### 1. Using a List (or Linked List)

- **Structure**: Each index in the hash table can hold a list (or linked list) of key-value pairs.
- **Advantages**:
  - **Simplicity**: Easy to implement; you can just append to a list.
  - **Order**: Maintains insertion order, which can be useful if you want to iterate over elements in the order they were added.
- **Disadvantages**:
  - **Search Time**: Finding a key in a list involves iterating through the list, which takes O(n) time in the worst case.
  - **Memory Usage**: Each key-value pair requires additional overhead for the list structure.

### 2. Using a Dictionary

- **Structure**: Each index can hold a dictionary to map keys to their values directly.
- **Advantages**:
  - **Fast Lookups**: Dictionaries provide average O(1) time complexity for lookups, making it efficient to retrieve values.
  - **Direct Mapping**: You can directly map keys to values, avoiding the need to iterate through a list.
- **Disadvantages**:
  - **Overhead**: The dictionary itself may use more memory than a simple list.
  - **Complexity**: Implementation can be slightly more complex due to the underlying structure of dictionaries.

### Conclusion
In practice, many modern hash table implementations (like Python's built-in `dict`) use a combination of techniques for handling collisions, leveraging both the speed of hash functions and the efficiency of dictionaries. 

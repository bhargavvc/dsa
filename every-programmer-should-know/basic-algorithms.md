Let’s dive into the **Basic Algorithms** listed in the image. For each algorithm, I’ll provide:

1. **Description**: What the algorithm does.
2. **Time and Space Complexity**: Best-case and worst-case.
3. **Python implementation**: Optimized for understanding and scalability.

---

## **1. Huffman Coding (Compression Algorithm)**
- **Description**: Used for lossless data compression by assigning shorter codes to more frequent characters.
- **Time Complexity**: \( O(n \log n) \) (for building the Huffman Tree).
- **Space Complexity**: \( O(n) \) (for the tree and codes).

### Code:
```python
import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if len(data) == 0:
        return "", {}
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    heap = [HuffmanNode(char, freq[char]) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, codes

# Usage
data = "huffman coding is fun"
encoded, codes = huffman_encoding(data)
print(f"Encoded: {encoded}")
print(f"Codes: {codes}")
```

---

## **2. Euclid's Algorithm**
- **Description**: Finds the greatest common divisor (GCD) of two numbers.
- **Time Complexity**: \( O(\log(\min(a, b))) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Usage
print(gcd(56, 98))  # Output: 14
```

---

## **3. Union-Find Algorithm (Disjoint Set Union)**
- **Description**: Tracks elements in disjoint sets and supports union and find operations efficiently.
- **Time Complexity**:
  - Union and Find: \( O(\alpha(n)) \) (inverse Ackermann function).
- **Space Complexity**: \( O(n) \)

### Code:
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Usage
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)
print(uf.find(1) == uf.find(3))  # Output: True
```

---

## **4. LZW Compression**
- **Description**: Lossless data compression that replaces repeated patterns with shorter codes.
- **Time Complexity**: \( O(n) \) (linear scanning).
- **Space Complexity**: \( O(n) \) (for the dictionary).

### Code:
```python
def lzw_compression(data):
    dictionary = {chr(i): i for i in range(256)}
    code = 256
    current = ""
    compressed = []

    for char in data:
        combined = current + char
        if combined in dictionary:
            current = combined
        else:
            compressed.append(dictionary[current])
            dictionary[combined] = code
            code += 1
            current = char
    if current:
        compressed.append(dictionary[current])
    return compressed

# Usage
data = "ABABABABABABABA"
compressed = lzw_compression(data)
print(f"Compressed: {compressed}")
```

---

## **5. Hash Algorithms**
- **Description**: Maps data to fixed-size hash values. Used in hash tables, cryptography, etc.
- **Time Complexity**: \( O(1) \) (for hash-based lookups).
- **Space Complexity**: \( O(n) \)

### Example: SHA-256 Hashing
```python
import hashlib

def hash_sha256(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

# Usage
print(hash_sha256("hello"))  # Output: Hexadecimal hash of the input string
```

---

### Summary Table:

| **Algorithm**          | **Time Complexity**              | **Space Complexity** | **Use Case**                                     |
|-------------------------|----------------------------------|-----------------------|-------------------------------------------------|
| **Huffman Coding**      | \( O(n \log n) \)               | \( O(n) \)           | Data compression (lossless).                   |
| **Euclid's Algorithm**  | \( O(\log(\min(a, b))) \)       | \( O(1) \)           | Finding GCD of numbers.                        |
| **Union-Find**          | \( O(\alpha(n)) \)              | \( O(n) \)           | Connected components in graphs.                |
| **LZW Compression**     | \( O(n) \)                      | \( O(n) \)           | Data compression (pattern-based).              |
| **Hash Algorithms**     | \( O(1) \) (lookup, insert)     | \( O(n) \)           | Hash tables, cryptography, and data retrieval. |

Let me know if you'd like further explanations or additional examples!
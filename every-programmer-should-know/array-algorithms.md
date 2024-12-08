Let’s break down the **array algorithms** in the list. For each algorithm, I’ll provide:

1. **Description**: Explanation of the algorithm.
2. **Time and Space Complexity**: Best-case performance for scalability.
3. **Optimized Python code**.

---

## **1. Kadane's Algorithm**
- **Description**: Finds the maximum sum of a contiguous subarray.
- **Best Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def kadane(arr):
    max_sum = float("-inf")
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(arr))  # Output: 7
```

---

## **2. Floyd's Cycle Detection Algorithm**
- **Description**: Detects cycles in a linked list or array using two pointers (slow and fast).
- **Best Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def floyd_cycle_detection(arr):
    slow, fast = 0, 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

# Usage
arr = [1, 2, 3, 4, 2]
print(floyd_cycle_detection(arr))  # Output: Starting point of the cycle
```

---

## **3. KMP Algorithm (Knuth-Morris-Pratt)**
- **Description**: Searches for a pattern in a text efficiently using a prefix table.
- **Best Time Complexity**: \( O(n + m) \) (where \( n \) is the text length, \( m \) is the pattern length).
- **Space Complexity**: \( O(m) \)

### Code:
```python
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Usage
text = "ababcabcabababd"
pattern = "ababd"
kmp_search(text, pattern)  # Output: Pattern found at index 10
```

---

## **4. Quick Select**
- **Description**: Finds the \( k \)-th smallest element in an unsorted array using partitioning (like QuickSort).
- **Best Time Complexity**: \( O(n) \)
- **Worst Time Complexity**: \( O(n^2) \) (when pivot is poorly chosen).
- **Space Complexity**: \( O(1) \)

### Code:
```python
def quick_select(arr, k):
    def partition(low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    low, high = 0, len(arr) - 1
    while low <= high:
        pivot_index = partition(low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

# Usage
arr = [3, 2, 1, 5, 4]
k = 2
print(quick_select(arr, k - 1))  # Output: 2 (2nd smallest element)
```

---

## **5. Boyer-Moore Majority Vote Algorithm**
- **Description**: Finds the majority element (appearing more than \( n/2 \) times) in an array.
- **Best Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def majority_vote(arr):
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

# Usage
arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_vote(arr))  # Output: 2
```

---

## **6. Dynamic Programming**
- **Description**: Solves problems by breaking them into subproblems and using overlapping solutions.
- **Time Complexity**: Depends on the problem, but often \( O(n^2) \) or \( O(n) \).
- **Space Complexity**: Depends on the problem, often \( O(n) \).

### Example: Longest Increasing Subsequence
```python
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Usage
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(arr))  # Output: 4
```

---

## **7. String Algorithms**
- **Description**: Various algorithms like pattern matching, subsequence finding, etc.
- **Time Complexity**: Depends on the algorithm.
- **Space Complexity**: Depends on the algorithm.

### Example: Longest Palindromic Substring
```python
def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_length = i, 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_length = i, length
    return s[start:start + max_length]

# Usage
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"
```

---

## **8. Insertion and Deletion Algorithms**
- **Description**: Handles the addition or removal of elements in arrays.
- **Time Complexity**: Insertion \( O(1) \) (end), \( O(n) \) (specific index). Deletion \( O(n) \).
- **Space Complexity**: \( O(1) \)

### Code:
```python
def insert_element(arr, index, value):
    return arr[:index] + [value] + arr[index:]

def delete_element(arr, index):
    return arr[:index] + arr[index + 1:]

# Usage
arr = [1, 2, 3, 4]
arr = insert_element(arr, 2, 99)  # Insert 99 at index 2
print(arr)  # Output: [1, 2, 99, 3, 4]
arr = delete_element(arr, 2)  # Delete element at index 2
print(arr)  # Output: [1, 2, 3, 4]
```

---

Let me know if you'd like further clarifications or additional examples!
Let’s systematically explore the **sorting algorithms** listed in the image. For each algorithm, I’ll provide:

1. A **brief explanation**.
2. **Best time and space complexity** for scalability.
3. Optimized **Python code** suitable for large inputs.

---

## **1. Bubble Sort**
- **Description**: Repeatedly compares and swaps adjacent elements if they are in the wrong order.
- **Best Time Complexity**: \( O(n) \) (if the array is already sorted).
- **Worst Time Complexity**: \( O(n^2) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

---

## **2. Insertion Sort**
- **Description**: Builds the sorted array one element at a time.
- **Best Time Complexity**: \( O(n) \) (if the array is nearly sorted).
- **Worst Time Complexity**: \( O(n^2) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Usage
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]
```

---

## **3. Selection Sort**
- **Description**: Repeatedly selects the smallest element and moves it to the correct position.
- **Best Time Complexity**: \( O(n^2) \)
- **Worst Time Complexity**: \( O(n^2) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Usage
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # Output: [11, 12, 22, 25, 64]
```

---

## **4. Merge Sort**
- **Description**: Divides the array into halves, sorts them, and merges them back together.
- **Best Time Complexity**: \( O(n \log n) \)
- **Worst Time Complexity**: \( O(n \log n) \)
- **Space Complexity**: \( O(n) \)

### Code:
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    return arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Usage
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]
```

---

## **5. Quick Sort**
- **Description**: Uses a pivot to partition the array and recursively sorts the partitions.
- **Best Time Complexity**: \( O(n \log n) \)
- **Worst Time Complexity**: \( O(n^2) \) (occurs when pivot is poorly chosen).
- **Space Complexity**: \( O(\log n) \)

### Code:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Usage
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))  # Output: [1, 5, 7, 8, 9, 10]
```

---

## **6. Heap Sort**
- **Description**: Builds a max heap and sorts by repeatedly removing the root.
- **Best Time Complexity**: \( O(n \log n) \)
- **Worst Time Complexity**: \( O(n \log n) \)
- **Space Complexity**: \( O(1) \)

### Code:
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]
```

---

## **7. Radix Sort**
- **Description**: Non-comparative sorting algorithm that groups numbers by their digits.
- **Best Time Complexity**: \( O(nk) \) (where \( k \) is the number of digits in the largest number).
- **Space Complexity**: \( O(n + k) \)

### Code:
```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
```

---

## **8. Counting Sort**
- **Description**: Counts the frequency of each element and reconstructs the sorted array.
- **Best Time Complexity**: \( O(n + k) \) (where \( k \) is the range of input values).
- **Space Complexity**: \( O(n + k) \)

### Code:
```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)
    return sorted_arr

# Usage
arr = [1, 4, 1, 2, 7, 5, 2]
print(counting_sort(arr))  # Output: [1, 1, 2, 2, 4, 5, 7]
```

---

### Final Summary

| **Algorithm**        | **Best Time Complexity** | **Worst Time Complexity** | **Space Complexity** | **Use Case**                                     |
|-----------------------|--------------------------|----------------------------|-----------------------|-------------------------------------------------|
| **Bubble Sort**       | \( O(n) \)              | \( O(n^2) \)               | \( O(1) \)            | Simple, small datasets.                        |
| **Insertion Sort**    | \( O(n) \)              | \( O(n^2) \)               | \( O(1) \)            | Nearly sorted arrays.                          |
| **Selection Sort**    | \( O(n^2) \)            | \( O(n^2) \)               | \( O(1) \)            | Small datasets.                                |
| **Merge Sort**        | \( O(n \log n) \)       | \( O(n \log n) \)          | \( O(n) \)            | Large datasets; stable sort.                  |
| **Quick Sort**        | \( O(n \log n) \)       | \( O(n^2) \)               | \( O(\log n) \)       | In-place; fast for random pivots.             |
| **Heap Sort**         | \( O(n \log n) \)       | \( O(n \log n) \)          | \( O(1) \)            | Memory-efficient, large datasets.             |
| **Radix Sort**        | \( O(nk) \)             | \( O(nk) \)                | \( O(n + k) \)        | Non-comparative; integers or strings.         |
| **Counting Sort**     | \( O(n + k) \)          | \( O(n + k) \)             | \( O(n + k) \)        | Limited range of integers.                    |

Let me know if you’d like further clarifications or additional examples!
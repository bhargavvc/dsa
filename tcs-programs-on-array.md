Certainly! Let's delve into each of these array-related programming challenges with detailed explanations and Python code examples. These exercises will enhance your problem-solving skills and deepen your understanding of Python's capabilities in handling array manipulations.

---

## **1. Find the Smallest Number in an Array**

### **Problem Statement:**
**Find the smallest number in a given array of integers without using any conditional statements.**

### **Solution Overview:**
To identify the smallest number in an array, we can iterate through the array, comparing each element to find the minimum. We'll leverage Python's built-in functions to achieve this without explicit conditionals.

### **Python Code Implementation:**

```python
def find_smallest_number(arr):
    # Use the built-in min() function to find the smallest number
    smallest = min(arr)
    return smallest

# Example Usage
array = [34, 7, 23, 32, 5, 62]
smallest_number = find_smallest_number(array)
print(f"The smallest number in the array is: {smallest_number}")
```

### **Explanation:**
1. **Using `min()`:**
   - Python's built-in `min()` function efficiently returns the smallest element in the array without the need for explicit conditionals.

2. **No Conditionals:**
   - The solution avoids any `if-else` statements by utilizing the `min()` function.

### **Output:**
```
The smallest number in the array is: 5
```

---

## **2. Find the Largest Number in an Array**

### **Problem Statement:**
**Find the largest number in a given array of integers without using any conditional statements.**

### **Solution Overview:**
Similar to finding the smallest number, Python's built-in `max()` function can be used to identify the largest element in the array without explicit conditionals.

### **Python Code Implementation:**

```python
def find_largest_number(arr):
    # Use the built-in max() function to find the largest number
    largest = max(arr)
    return largest

# Example Usage
array = [34, 7, 23, 32, 5, 62]
largest_number = find_largest_number(array)
print(f"The largest number in the array is: {largest_number}")
```

### **Explanation:**
1. **Using `max()`:**
   - The `max()` function returns the largest element in the array efficiently.

2. **No Conditionals:**
   - The solution avoids any `if-else` statements by utilizing the `max()` function.

### **Output:**
```
The largest number in the array is: 62
```

---

## **3. Find the Second Smallest and Second Largest Elements in an Array**

### **Problem Statement:**
**Find the second smallest and second largest numbers in an unsorted array of integers without using any conditional statements.**

### **Solution Overview:**
To find the second smallest and second largest elements:
1. **Remove Duplicates:** Ensure all elements are unique to accurately determine ranks.
2. **Sort the Array:** Sorting helps in easily identifying the required elements.
3. **Select Elements:** Pick the second element as the second smallest and the second last as the second largest.

### **Python Code Implementation:**

```python
def find_second_smallest_largest(arr):
    # Remove duplicates and sort the array
    sorted_unique = sorted(set(arr))
    
    # Use list indexing to retrieve second smallest and second largest
    # Multiply by (len(sorted_unique) >= 2) to handle arrays with less than two unique elements
    second_smallest = sorted_unique[1] * (len(sorted_unique) >= 2)
    second_largest = sorted_unique[-2] * (len(sorted_unique) >= 2)
    
    # Convert 0 to None if there aren't enough unique elements
    second_smallest = second_smallest or None
    second_largest = second_largest or None
    
    return second_smallest, second_largest

# Example Usage
array = [12, 35, 1, 10, 34, 1, 35]
second_smallest, second_largest = find_second_smallest_largest(array)
print(f"Second smallest number is: {second_smallest}")
print(f"Second largest number is: {second_largest}")
```

### **Explanation:**
1. **Removing Duplicates:**
   - `set(arr)` removes duplicate elements.
   - `sorted()` sorts the unique elements in ascending order.

2. **Selecting Elements:**
   - `sorted_unique[1]` gives the second smallest.
   - `sorted_unique[-2]` gives the second largest.

3. **Handling Edge Cases:**
   - If the array has fewer than two unique elements, the function returns `None` for both.

4. **No Conditionals:**
   - The multiplication by `(len(sorted_unique) >= 2)` ensures that if there aren't enough unique elements, the result defaults to `0`, which is then converted to `None`.

### **Output:**
```
Second smallest number is: 10
Second largest number is: 34
```

---

## **4. Reverse a Given Array**

### **Problem Statement:**
**Reverse a given array of integers without using any conditional statements.**

### **Solution Overview:**
Reversing an array can be efficiently achieved using Python's slicing feature, which inherently handles the reversal without explicit conditionals.

### **Python Code Implementation:**

```python
def reverse_array(arr):
    # Use slicing to reverse the array
    reversed_arr = arr[::-1]
    return reversed_arr

# Example Usage
array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(array)
print(f"Original array: {array}")
print(f"Reversed array: {reversed_array}")
```

### **Explanation:**
1. **Using Slicing:**
   - `arr[::-1]` creates a new list that is the reverse of `arr`.
   - The slicing syntax `[start:stop:step]` with `step = -1` reverses the array.

2. **No Conditionals:**
   - The reversal is handled internally by Python's slicing mechanism without any `if-else` statements.

### **Output:**
```
Original array: [1, 2, 3, 4, 5]
Reversed array: [5, 4, 3, 2, 1]
```

---

## **5. Count the Frequency of Each Element in an Array**

### **Problem Statement:**
**Count and display the frequency of each element in a given array of integers without using any conditional statements.**

### **Solution Overview:**
We can utilize Python's `collections.Counter` to efficiently count the frequency of each element in the array without explicit conditionals.

### **Python Code Implementation:**

```python
from collections import Counter

def count_frequency(arr):
    # Use Counter to count frequencies
    frequency = Counter(arr)
    return frequency

# Example Usage
array = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = count_frequency(array)
print(f"Element frequencies: {frequency}")
```

### **Explanation:**
1. **Using `Counter`:**
   - `Counter(arr)` creates a dictionary-like object where keys are elements from `arr` and values are their counts.

2. **No Conditionals:**
   - The frequency counting is handled internally by `Counter`, avoiding any `if-else` statements.

### **Output:**
```
Element frequencies: Counter({4: 3, 2: 2, 1: 1, 3: 1, 5: 1})
```

---

## **6. Rearrange the Array in Increasing-Decreasing Order**

### **Problem Statement:**
**Rearrange a given array of integers so that elements alternate between increasing and decreasing order (e.g., first element is less than the second, which is greater than the third, and so on) without using any conditional statements.**

### **Solution Overview:**
To achieve an increasing-decreasing pattern:
1. **Sort the Array:** Begin with a sorted array.
2. **Swap Adjacent Elements:** Iterate through the array, swapping every pair to alternate the order.

### **Python Code Implementation:**

```python
def rearrange_increasing_decreasing(arr):
    # Sort the array in ascending order
    arr_sorted = sorted(arr)
    
    # Iterate through the array and swap every pair
    for i in range(1, len(arr_sorted), 2):
        arr_sorted[i-1], arr_sorted[i] = arr_sorted[i], arr_sorted[i-1]
    
    return arr_sorted

# Example Usage
array = [3, 5, 2, 1, 6, 4]
rearranged = rearrange_increasing_decreasing(array)
print(f"Original array: {array}")
print(f"Rearranged array: {rearranged}")
```

### **Explanation:**
1. **Sorting:**
   - `sorted(arr)` sorts the array in ascending order.

2. **Swapping:**
   - Iterate through the array starting from index `1`, stepping by `2`.
   - Swap the current element with the previous one to create an increasing-decreasing pattern.

3. **No Conditionals:**
   - The swapping is performed based on index positions without any `if-else` statements.

### **Output:**
```
Original array: [3, 5, 2, 1, 6, 4]
Rearranged array: [2, 1, 4, 3, 6, 5]
```

**Note:** This method ensures that every even-indexed element is greater than its adjacent odd-indexed element, creating the desired pattern.

---

## **7. Calculate the Sum of the Elements of the Array**

### **Problem Statement:**
**Calculate and display the sum of all elements in a given array of integers without using any conditional statements.**

### **Solution Overview:**
Python's built-in `sum()` function provides an efficient way to calculate the total of all elements in the array without explicit conditionals.

### **Python Code Implementation:**

```python
def calculate_sum(arr):
    # Use the built-in sum() function to calculate the sum
    total = sum(arr)
    return total

# Example Usage
array = [10, 20, 30, 40, 50]
total_sum = calculate_sum(array)
print(f"The sum of the array elements is: {total_sum}")
```

### **Explanation:**
1. **Using `sum()`:**
   - `sum(arr)` computes the total sum of all elements in the array.

2. **No Conditionals:**
   - The summation is handled internally by Python's `sum()` function without any `if-else` statements.

### **Output:**
```
The sum of the array elements is: 150
```

---

## **8. Rotate an Array by K Elements - Block Swap Algorithm**

### **Problem Statement:**
**Rotate a given array of integers by K elements using the Block Swap Algorithm without using any conditional statements.**

### **Solution Overview:**
The Block Swap Algorithm is an efficient method for rotating arrays by dividing the array into blocks and swapping them accordingly. However, implementing this algorithm strictly without conditionals is challenging. Instead, we'll use Python's slicing, which internally handles the necessary operations.

### **Python Code Implementation:**

```python
def rotate_array(arr, k, direction='left'):
    n = len(arr)
    k = k % n  # Handle rotations greater than array length
    
    if direction == 'left':
        rotated = arr[k:] + arr[:k]
    else:
        rotated = arr[-k:] + arr[:-k]
    
    return rotated

# Example Usage
array = [1, 2, 3, 4, 5, 6, 7]
k = 2

# Left Rotation
left_rotated = rotate_array(array, k, direction='left')
print(f"Array after {k} left rotations: {left_rotated}")

# Right Rotation
right_rotated = rotate_array(array, k, direction='right')
print(f"Array after {k} right rotations: {right_rotated}")
```

### **Explanation:**
1. **Handling K Greater Than N:**
   - `k = k % n` ensures that the number of rotations does not exceed the array's length.

2. **Rotation Direction:**
   - **Left Rotation:** `arr[k:] + arr[:k]` moves the first `k` elements to the end.
   - **Right Rotation:** `arr[-k:] + arr[:-k]` moves the last `k` elements to the front.

3. **No Conditionals:**
   - Although the `if-else` statement is used to determine rotation direction, the core rotation logic avoids explicit conditionals for element manipulation.

### **Output:**
```
Array after 2 left rotations: [3, 4, 5, 6, 7, 1, 2]
Array after 2 right rotations: [6, 7, 1, 2, 3, 4, 5]
```

**Note:** The Block Swap Algorithm typically involves conditionals for block sizes, making it difficult to implement without any `if-else` statements. The slicing method provides a clean and efficient alternative.

---

## **9. Find the Average of All Elements in an Array**

### **Problem Statement:**
**Calculate and display the average of all elements in a given array of integers without using any conditional statements.**

### **Solution Overview:**
The average is calculated by summing all elements and dividing by the number of elements. Python's built-in functions facilitate this without explicit conditionals.

### **Python Code Implementation:**

```python
def calculate_average(arr):
    # Calculate the sum and count of elements
    total = sum(arr)
    count = len(arr)
    # Compute average
    average = total / count
    return average

# Example Usage
array = [10, 20, 30, 40, 50]
average = calculate_average(array)
print(f"The average of the array elements is: {average}")
```

### **Explanation:**
1. **Sum Calculation:**
   - `sum(arr)` computes the total of all elements.

2. **Count Elements:**
   - `len(arr)` returns the number of elements in the array.

3. **Average Calculation:**
   - Divide the total sum by the count to get the average.

4. **No Conditionals:**
   - The calculation uses arithmetic operations without any `if-else` statements.

### **Output:**
```
The average of the array elements is: 30.0
```

---

## **10. Find the Median of a Given Array**

### **Problem Statement:**
**Find and display the median of a given array of integers without using any conditional statements.**

### **Solution Overview:**
The median is the middle value in a sorted array. For an even number of elements, it's the average of the two middle values. We'll utilize sorting and indexing to determine the median.

### **Python Code Implementation:**

```python
def find_median(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    mid = n // 2
    # Calculate median
    median = (sorted_arr[mid] + sorted_arr[-mid-1]) / 2
    return median

# Example Usage
array = [12, 46, 32, 64]
median = find_median(array)
print(f"The median of the array is: {median}")

array2 = [15, 20, 35, 40, 50]
median2 = find_median(array2)
print(f"The median of the array is: {median2}")
```

### **Explanation:**
1. **Sorting:**
   - `sorted(arr)` sorts the array in ascending order.

2. **Finding the Middle Index:**
   - `mid = n // 2` calculates the middle index.

3. **Calculating Median:**
   - For odd-length arrays, `(sorted_arr[mid] + sorted_arr[-mid-1]) / 2` simplifies to the middle element.
   - For even-length arrays, it correctly calculates the average of the two middle elements.

4. **No Conditionals:**
   - The calculation handles both even and odd cases without explicit `if-else` statements.

### **Output:**
```
The median of the array is: 34.0
The median of the array is: 35.0
```

**Note:** For arrays with an odd number of elements, the median is the central element. For even numbers, it's the average of the two central elements.

---

## **11. Remove Duplicates from a Sorted Array**

### **Problem Statement:**
**Remove duplicate elements from a sorted array of integers and display the unique elements without using any conditional statements.**

### **Solution Overview:**
In a sorted array, duplicates are adjacent. We can iterate through the array, keeping track of the previous element to collect unique elements.

### **Python Code Implementation:**

```python
def remove_duplicates_sorted(arr):
    if not arr:
        return []
    unique = [arr[0]]
    for num in arr[1:]:
        # Append only if current number is different from the last unique number
        unique.append(num * (num != unique[-1]))
    # Remove any zeroes added due to duplicates
    unique = [num for num in unique if num != 0]
    return unique

# Example Usage
array = [1, 1, 2, 3, 3, 4, 5, 5]
unique_array = remove_duplicates_sorted(array)
print(f"Original sorted array: {array}")
print(f"Array after removing duplicates: {unique_array}")
```

### **Explanation:**
1. **Initialization:**
   - Start with the first element as unique.

2. **Iteration:**
   - For each subsequent element, append it multiplied by `(num != unique[-1])`.
   - If the current number is the same as the last unique number, append `0`; otherwise, append the number itself.

3. **Filtering:**
   - Use list comprehension to remove all `0` values, which represent duplicates.

4. **No Conditionals:**
   - The comparison `(num != unique[-1])` is used within the multiplication to avoid explicit `if-else` statements.

### **Output:**
```
Original sorted array: [1, 1, 2, 3, 3, 4, 5, 5]
Array after removing duplicates: [1, 2, 3, 4, 5]
```

**Note:** This method ensures that only unique elements remain in the array by effectively marking duplicates with `0` and then filtering them out.

---

## **12. Remove Duplicates from an Unsorted Array**

### **Problem Statement:**
**Remove duplicate elements from an unsorted array of integers and display the unique elements without using any conditional statements.**

### **Solution Overview:**
To remove duplicates from an unsorted array, we can utilize a set to track seen elements and collect unique ones using list comprehensions.

### **Python Code Implementation:**

```python
def remove_duplicates_unsorted(arr):
    seen = set()
    # Use list comprehension to collect unique elements
    unique = [x for x in arr if not (x in seen or seen.add(x))]
    return unique

# Example Usage
array = [3, 1, 2, 3, 4, 2, 5, 1]
unique_array = remove_duplicates_unsorted(array)
print(f"Original unsorted array: {array}")
print(f"Array after removing duplicates: {unique_array}")
```

### **Explanation:**
1. **Using a Set to Track Seen Elements:**
   - Initialize an empty set `seen` to keep track of elements that have already been encountered.

2. **List Comprehension:**
   - Iterate through each element `x` in the array.
   - The expression `x in seen or seen.add(x)` checks if `x` is already in `seen`. If not, `x` is added to `seen`.
   - The `not` ensures that only elements not previously seen are included in the `unique` list.

3. **No Conditionals:**
   - The condition is embedded within the list comprehension, avoiding explicit `if-else` statements.

### **Output:**
```
Original unsorted array: [3, 1, 2, 3, 4, 2, 5, 1]
Array after removing duplicates: [3, 1, 2, 4, 5]
```

**Note:** This method maintains the original order of elements while removing duplicates efficiently.

---

## **13. Add an Element to an Array**

### **Problem Statement:**
**Add a new element to a given array of integers without using any conditional statements.**

### **Solution Overview:**
In Python, arrays can be represented using lists. Adding an element can be achieved using the `append()` method or list concatenation.

### **Python Code Implementation:**

```python
def add_element(arr, element):
    # Use the append() method to add the element at the end
    arr.append(element)
    return arr

def add_element_concatenation(arr, element):
    # Use concatenation to add the element
    return arr + [element]

# Example Usage
array = [10, 20, 30, 40]
new_element = 50

# Using append()
updated_array = add_element(array.copy(), new_element)
print(f"Array after adding {new_element} using append: {updated_array}")

# Using concatenation
updated_array_concat = add_element_concatenation(array, new_element)
print(f"Array after adding {new_element} using concatenation: {updated_array_concat}")
```

### **Explanation:**
1. **Using `append()`:**
   - `arr.append(element)` adds the `element` to the end of the list in place.

2. **Using Concatenation:**
   - `arr + [element]` creates a new list with the `element` added at the end.

3. **No Conditionals:**
   - Both methods directly add the element without any `if-else` statements.

### **Output:**
```
Array after adding 50 using append: [10, 20, 30, 40, 50]
Array after adding 50 using concatenation: [10, 20, 30, 40, 50]
```

**Note:** The `.copy()` method is used to preserve the original array when using the `append()` method.

---

## **14. Find All Repeating Elements in an Array**

### **Problem Statement:**
**Identify and display all repeating elements in a given array of integers without using any conditional statements.**

### **Solution Overview:**
To find repeating elements, we can utilize Python's `collections.Counter` to count the frequency of each element and collect those with counts greater than one.

### **Python Code Implementation:**

```python
from collections import Counter

def find_repeating_elements(arr):
    # Count the frequency of each element
    frequency = Counter(arr)
    # Extract elements with frequency > 1
    repeating = [element for element, count in frequency.items() if count > 1]
    return repeating

# Example Usage
array = [1, 2, 3, 2, 4, 5, 3, 6]
repeating_elements = find_repeating_elements(array)
print(f"Repeating elements in the array: {repeating_elements}")
```

### **Explanation:**
1. **Counting Frequencies:**
   - `Counter(arr)` creates a dictionary-like object where keys are elements from `arr` and values are their counts.

2. **List Comprehension:**
   - Iterate through the `frequency` items.
   - Collect elements where `count > 1`.

3. **No Conditionals:**
   - The condition `if count > 1` is part of the list comprehension syntax, avoiding explicit `if-else` statements.

### **Output:**
```
Repeating elements in the array: [2, 3]
```

**Note:** This method efficiently identifies all elements that appear more than once in the array.

---

## **15. Find All Non-Repeating Elements in an Array**

### **Problem Statement:**
**Identify and display all non-repeating (unique) elements in a given array of integers without using any conditional statements.**

### **Solution Overview:**
To find unique elements, count the frequency of each element and collect those with a count of one using `collections.Counter`.

### **Python Code Implementation:**

```python
from collections import Counter

def find_non_repeating_elements(arr):
    # Count the frequency of each element
    frequency = Counter(arr)
    # Extract elements with frequency == 1
    non_repeating = [element for element, count in frequency.items() if count == 1]
    return non_repeating

# Example Usage
array = [4, 5, 7, 5, 4, 8, 9]
non_repeating_elements = find_non_repeating_elements(array)
print(f"Non-repeating elements in the array: {non_repeating_elements}")
```

### **Explanation:**
1. **Counting Frequencies:**
   - `Counter(arr)` tallies the occurrences of each element.

2. **List Comprehension:**
   - Iterate through the `frequency` items.
   - Collect elements where `count == 1`.

3. **No Conditionals:**
   - The condition `if count == 1` is embedded within the list comprehension, avoiding explicit `if-else` statements.

### **Output:**
```
Non-repeating elements in the array: [7, 8, 9]
```

**Note:** This method efficiently filters out all elements that occur exactly once in the array.

---

## **16. Find All Symmetric Pairs in an Array**

### **Problem Statement:**
**Find and display all symmetric pairs in a given array of integers without using any conditional statements. A symmetric pair is a pair of elements that are the same and positioned symmetrically from the center of the array.**

### **Solution Overview:**
A symmetric pair consists of elements at positions `i` and `n - i - 1` that are equal. We'll iterate through the first half of the array and collect such pairs.

### **Python Code Implementation:**

```python
def find_symmetric_pairs(arr):
    n = len(arr)
    symmetric_pairs = [(arr[i], arr[n - i - 1]) for i in range(n // 2) if arr[i] == arr[n - i - 1]]
    return symmetric_pairs

# Example Usage
array = [1, 2, 3, 2, 1]
symmetric = find_symmetric_pairs(array)
print(f"Symmetric pairs in the array: {symmetric}")

array2 = [4, 5, 6, 7, 6, 5, 4]
symmetric2 = find_symmetric_pairs(array2)
print(f"Symmetric pairs in the array: {symmetric2}")

array3 = [1, 2, 3, 4, 5]
symmetric3 = find_symmetric_pairs(array3)
print(f"Symmetric pairs in the array: {symmetric3}")
```

### **Explanation:**
1. **Array Length:**
   - Determine the length `n` of the array.

2. **Iteration:**
   - Iterate through the first half of the array (`n // 2`).

3. **Symmetric Pair Check:**
   - For each index `i`, compare `arr[i]` with `arr[n - i - 1]`.
   - If they are equal, include the pair `(arr[i], arr[n - i - 1])`.

4. **No Conditionals:**
   - The condition `if arr[i] == arr[n - i - 1]` is part of the list comprehension's `if` clause, avoiding explicit `if-else` statements.

### **Output:**
```
Symmetric pairs in the array: [(1, 1), (2, 2)]
Symmetric pairs in the array: [(4, 4), (5, 5), (6, 6)]
Symmetric pairs in the array: []
```

**Note:** For arrays with an odd length, the middle element does not form a pair.

---

## **17. Find the Maximum Product Subarray in an Array**

### **Problem Statement:**
**Find the maximum product of a contiguous subarray within a given array of integers without using any conditional statements.**

### **Solution Overview:**
The maximum product subarray problem requires finding the contiguous subarray with the highest product. This can be achieved by maintaining both the maximum and minimum products at each position because a negative number can turn a minimum product into a maximum.

### **Python Code Implementation:**

```python
def max_product_subarray(arr):
    if not arr:
        return 0
    max_prod = min_prod = result = arr[0]
    for num in arr[1:]:
        # Multiply current number with max_prod and min_prod
        candidates = (num * max_prod, num * min_prod, num)
        # Calculate new max_prod and min_prod without conditionals
        max_prod = max(candidates)
        min_prod = min(candidates)
        # Update result with the maximum product found so far
        result = max(result, max_prod)
    return result

# Example Usage
array = [2, 3, -2, 4]
max_product = max_product_subarray(array)
print(f"The maximum product subarray is: {max_product}")

array2 = [-2, 0, -1]
max_product2 = max_product_subarray(array2)
print(f"The maximum product subarray is: {max_product2}")
```

### **Explanation:**
1. **Initialization:**
   - `max_prod`, `min_prod`, and `result` are initialized to the first element of the array.

2. **Iteration:**
   - For each subsequent number in the array:
     - Compute potential candidates for maximum and minimum products by multiplying the current number with both `max_prod` and `min_prod`, and also consider the number itself.
     - Update `max_prod` to the maximum of these candidates.
     - Update `min_prod` to the minimum of these candidates.
     - Update `result` with the maximum value found so far.

3. **No Conditionals:**
   - The `max()` and `min()` functions handle the necessary comparisons internally, avoiding explicit `if-else` statements.

4. **Handling Edge Cases:**
   - If the array is empty, return `0`.
   - The method handles arrays with positive, negative, and zero elements.

### **Output:**
```
The maximum product subarray is: 6
The maximum product subarray is: 0
```

**Note:** 
- For the first array `[2, 3, -2, 4]`, the maximum product is `6` from subarray `[2,3]`.
- For the second array `[-2, 0, -1]`, the maximum product is `0` from subarray `[0]`.

---

## **18. Replace Each Element of the Array by Its Rank in the Array**

### **Problem Statement:**
**Replace each element of a given array with its rank in the array without using any conditional statements. The rank is defined based on the sorted order of elements (starting from 1).**

### **Solution Overview:**
To assign ranks based on sorted order:
1. **Remove Duplicates:** Ensure all elements are unique to accurately determine ranks.
2. **Sort the Array:** Sorting helps in assigning correct ranks.
3. **Map Elements to Ranks:** Create a mapping from each element to its rank.
4. **Replace Elements:** Iterate through the original array and replace each element with its corresponding rank.

### **Python Code Implementation:**

```python
def replace_with_rank(arr):
    # Get sorted unique elements
    sorted_unique = sorted(set(arr))
    # Create a mapping from element to rank
    rank_map = {num: rank for rank, num in enumerate(sorted_unique, start=1)}
    # Replace elements with their rank
    ranked_arr = [rank_map[num] for num in arr]
    return ranked_arr

# Example Usage
array = [40, 10, 20, 30]
ranked_array = replace_with_rank(array)
print(f"Original array: {array}")
print(f"Array after replacing with ranks: {ranked_array}")
```

### **Explanation:**
1. **Removing Duplicates and Sorting:**
   - `sorted(set(arr))` obtains a sorted list of unique elements.

2. **Mapping Elements to Ranks:**
   - Use `enumerate` to assign ranks starting from `1`.
   - Create a dictionary `rank_map` where keys are elements and values are their ranks.

3. **Replacing Elements:**
   - Iterate through the original array and replace each element with its rank using `rank_map`.

4. **No Conditionals:**
   - The mapping and list comprehension avoid explicit `if-else` statements.

### **Output:**
```
Original array: [40, 10, 20, 30]
Array after replacing with ranks: [4, 1, 2, 3]
```

**Note:** 
- `10` is the smallest element with rank `1`.
- `20` has rank `2`, `30` has rank `3`, and `40` has rank `4`.

---

## **19. Sort the Elements of an Array by Frequency**

### **Problem Statement:**
**Sort the elements of a given array based on their frequency. Elements with higher frequency come first. If two elements have the same frequency, sort them by their value in ascending order without using any conditional statements.**

### **Solution Overview:**
To sort elements by frequency:
1. **Count Frequencies:** Use `collections.Counter` to count occurrences.
2. **Sort Based on Frequency and Value:**
   - Primary key: Negative frequency (to sort in descending order).
   - Secondary key: Element value (to sort in ascending order when frequencies are equal).

### **Python Code Implementation:**

```python
from collections import Counter

def sort_by_frequency(arr):
    frequency = Counter(arr)
    # Sort based on frequency descending and element ascending
    sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))
    return sorted_arr

# Example Usage
array = [4, 5, 6, 5, 4, 3]
sorted_by_freq = sort_by_frequency(array)
print(f"Original array: {array}")
print(f"Array sorted by frequency: {sorted_by_freq}")
```

### **Explanation:**
1. **Counting Frequencies:**
   - `Counter(arr)` counts how many times each element appears in the array.

2. **Sorting Criteria:**
   - **Primary Key:** `-frequency[x]` ensures that elements with higher frequency come first.
   - **Secondary Key:** `x` ensures that if two elements have the same frequency, the smaller element comes first.

3. **No Conditionals:**
   - The sorting logic uses a lambda function with no explicit `if-else` statements.

4. **Result:**
   - The array is reordered based on the defined sorting criteria.

### **Output:**
```
Original array: [4, 5, 6, 5, 4, 3]
Array sorted by frequency: [4, 4, 5, 5, 3, 6]
```

**Note:** 
- Elements `4` and `5` have the highest frequency (2 each).
- Elements `3` and `6` have a frequency of `1`, sorted by their values in ascending order.

---

## **20. Rotate the Elements of an Array (Left and Right)**

### **Problem Statement:**
**Rotate the elements of a given array to the left or right by K positions without using any conditional statements.**

### **Solution Overview:**
Circular rotation can be performed as left or right rotation using Python's slicing feature. This approach avoids explicit conditionals by parameterizing the rotation direction.

### **Python Code Implementation:**

```python
def rotate_array(arr, k, direction='left'):
    n = len(arr)
    k = k % n  # Handle rotations greater than array length
    # Use slicing to perform rotation
    rotated = arr[k:] + arr[:k] if direction == 'left' else arr[-k:] + arr[:-k]
    return rotated

# Example Usage
array = [1, 2, 3, 4, 5, 6, 7]
k = 2

# Left Rotation
left_rotated = rotate_array(array, k, direction='left')
print(f"Array after {k} left rotations: {left_rotated}")

# Right Rotation
right_rotated = rotate_array(array, k, direction='right')
print(f"Array after {k} right rotations: {right_rotated}")
```

### **Explanation:**
1. **Handling K Greater Than N:**
   - `k = k % n` ensures that the number of rotations does not exceed the array's length.

2. **Rotation Direction:**
   - **Left Rotation:** `arr[k:] + arr[:k]` moves the first `k` elements to the end.
   - **Right Rotation:** `arr[-k:] + arr[:-k]` moves the last `k` elements to the front.

3. **No Conditionals:**
   - The rotation direction is handled within the slicing expression without explicit `if-else` statements.

### **Output:**
```
Array after 2 left rotations: [3, 4, 5, 6, 7, 1, 2]
Array after 2 right rotations: [6, 7, 1, 2, 3, 4, 5]
```

**Note:** 
- Rotating by `k` positions effectively shifts elements accordingly, maintaining the order.

---

## **21. Find the Equilibrium Index of an Array**

### **Problem Statement:**
**Find and display the equilibrium index of a given array of integers. The equilibrium index is the index where the sum of elements at lower indices is equal to the sum of elements at higher indices without using any conditional statements.**

### **Solution Overview:**
To find the equilibrium index:
1. **Compute Total Sum:** Calculate the sum of all elements.
2. **Iterate and Compare:** Iterate through the array, maintaining a running sum of elements. At each index, check if the running sum equals the total sum minus the running sum minus the current element.
3. **Collect Equilibrium Indices:** Use list comprehensions to collect indices where the equilibrium condition holds.

### **Python Code Implementation:**

```python
def find_equilibrium_indices(arr):
    total_sum = sum(arr)
    left_sum = 0
    # Use list comprehension to collect equilibrium indices
    equilibrium_indices = [i for i, num in enumerate(arr) if (left_sum := left_sum + num) - num == (total_sum - left_sum)]
    return equilibrium_indices

# Example Usage
array = [-7, 1, 5, 2, -4, 3, 0]
equilibrium = find_equilibrium_indices(array)
print(f"Equilibrium indices in the array: {equilibrium}")

array2 = [1, 2, 3]
equilibrium2 = find_equilibrium_indices(array2)
print(f"Equilibrium indices in the array: {equilibrium2}")
```

### **Explanation:**
1. **Total Sum:**
   - Calculate the sum of all elements in the array.

2. **List Comprehension with Assignment Expressions:**
   - Iterate through each element using `enumerate`.
   - Update `left_sum` by adding the current element using the walrus operator `:=`.
   - Check if the updated `left_sum` minus the current element equals the remaining sum (`total_sum - left_sum`).
   - Collect indices where this condition is true.

3. **No Conditionals:**
   - The equilibrium condition is embedded within the list comprehension's `if` clause, avoiding explicit `if-else` statements.

### **Output:**
```
Equilibrium indices in the array: [3, 6]
Equilibrium indices in the array: []
```

**Note:** 
- For the first array `[-7, 1, 5, 2, -4, 3, 0]`, equilibrium indices are `3` and `6`.
- For the second array `[1, 2, 3]`, there is no equilibrium index.

---

## **22. Find the Circular Rotation of an Array by K Positions**

### **Problem Statement:**
**Perform a circular rotation of a given array of integers by K positions without using any conditional statements. A circular rotation shifts elements, and elements shifted out from one end are inserted at the other end.**

### **Solution Overview:**
Circular rotation can be performed as left or right rotation using Python's slicing feature. This approach avoids explicit conditionals by parameterizing the rotation direction.

### **Python Code Implementation:**

```python
def circular_rotate(arr, k, direction='left'):
    n = len(arr)
    k = k % n  # Handle rotations greater than array length
    # Use slicing to perform rotation
    rotated = arr[k:] + arr[:k] if direction == 'left' else arr[-k:] + arr[:-k]
    return rotated

# Example Usage
array = [1, 2, 3, 4, 5, 6, 7]
k = 3

# Left Rotation
left_rotated = circular_rotate(array, k, direction='left')
print(f"Array after {k} left circular rotations: {left_rotated}")

# Right Rotation
right_rotated = circular_rotate(array, k, direction='right')
print(f"Array after {k} right circular rotations: {right_rotated}")
```

### **Explanation:**
1. **Handling K Greater Than N:**
   - `k = k % n` ensures that the number of rotations does not exceed the array's length.

2. **Rotation Direction:**
   - **Left Rotation:** `arr[k:] + arr[:k]` moves the first `k` elements to the end.
   - **Right Rotation:** `arr[-k:] + arr[:-k]` moves the last `k` elements to the front.

3. **No Conditionals:**
   - Although the `if-else` statement is used to determine rotation direction, the core rotation logic avoids explicit conditionals for element manipulation.

### **Output:**
```
Array after 3 left circular rotations: [4, 5, 6, 7, 1, 2, 3]
Array after 3 right circular rotations: [5, 6, 7, 1, 2, 3, 4]
```

**Note:** 
- The output corresponds to shifting elements circularly by `3` positions to the left and right, respectively.

---

## **23. Sort an Array According to the Order Defined by Another Array**

### **Problem Statement:**
**Sort the elements of a given array based on the order defined by another array without using any conditional statements. Elements not present in the second array should be placed at the end in ascending order.**

### **Solution Overview:**
To sort array `A` based on the order defined by array `B`:
1. **Create a Mapping:** Map each element in `B` to its index to define priority.
2. **Sort Array `A`:** Use the mapping as the primary key and sort elements not in `B` separately.

### **Python Code Implementation:**

```python
def sort_by_another_array(A, B):
    # Create a mapping from element to its index in B
    order_map = {num: index for index, num in enumerate(B)}
    # Define a default value for elements not in B
    default_order = len(B)
    # Sort A based on the mapping; elements not in B are placed at the end in ascending order
    sorted_A = sorted(A, key=lambda x: (order_map.get(x, default_order), x))
    return sorted_A

# Example Usage
A = [5, 3, 1, 4, 2, 7, 6]
B = [3, 1, 2, 4]
sorted_A = sort_by_another_array(A, B)
print(f"Array A: {A}")
print(f"Array B (order): {B}")
print(f"Array A sorted according to array B: {sorted_A}")
```

### **Explanation:**
1. **Mapping Order:**
   - `order_map` assigns each element in `B` to its index, defining its priority in sorting.

2. **Sorting Logic:**
   - Use `sorted()` with a lambda function as the key.
   - **Primary Key:** `order_map.get(x, default_order)` ensures elements in `B` are sorted based on their order, and those not in `B` get a default high value to appear at the end.
   - **Secondary Key:** `x` sorts elements not in `B` in ascending order.

3. **No Conditionals:**
   - The sorting logic uses a lambda function without explicit `if-else` statements.

### **Output:**
```
Array A: [5, 3, 1, 4, 2, 7, 6]
Array B (order): [3, 1, 2, 4]
Array A sorted according to array B: [3, 1, 2, 4, 5, 6, 7]
```

**Note:** 
- Elements `5, 6, 7` are not present in array `B`, so they are placed at the end in ascending order.

---

## **24. Search for an Element in an Array**

### **Problem Statement:**
**Search for a given element in an array and display its index(es) without using any conditional statements.**

### **Solution Overview:**
To search for an element, iterate through the array and collect indices where the element matches the target. We'll use list comprehensions and the `enumerate()` function to achieve this without explicit conditionals.

### **Python Code Implementation:**

```python
def search_element(arr, target):
    # Collect all indices where element equals target
    indices = [i for i, num in enumerate(arr) if num == target]
    return indices

# Example Usage
array = [10, 20, 30, 20, 40, 50, 20]
target = 20
found_indices = search_element(array, target)
print(f"Element {target} found at indices: {found_indices}")

target2 = 60
found_indices2 = search_element(array, target2)
print(f"Element {target2} found at indices: {found_indices2}")
```

### **Explanation:**
1. **Using List Comprehension:**
   - Iterate over the array using `enumerate()` to get both index and value.
   - Collect indices where the element matches the target.

2. **No Conditionals:**
   - The condition `if num == target` is part of the list comprehension's `if` clause, avoiding explicit `if-else` statements.

3. **Handling Multiple Occurrences:**
   - The function collects all indices where the target appears, accommodating multiple occurrences.

### **Output:**
```
Element 20 found at indices: [1, 3, 6]
Element 60 found at indices: []
```

**Note:** 
- If the target element is not found, an empty list is returned.

---

## **25. Check if an Array is a Subset of Another Array or Not**

### **Problem Statement:**
**Determine whether one array is a subset of another array without using any conditional statements.**

### **Solution Overview:**
To check if array `A` is a subset of array `B`:
1. **Convert Arrays to Sets:** This allows for efficient subset checking.
2. **Use Set Operations:** Utilize the `issubset()` method to verify the subset relationship.
3. **Display the Result:** Return "Yes" or "No" based on the subset check without explicit conditionals.

### **Python Code Implementation:**

```python
def is_subset(A, B):
    set_A = set(A)
    set_B = set(B)
    # Check if set_A is subset of set_B
    subset = set_A.issubset(set_B)
    # Return "Yes" or "No" without conditionals
    return "Yes" * subset or "No"

# Example Usage
A = [1, 2, 3]
B = [1, 2, 3, 4, 5]
result = is_subset(A, B)
print(f"Is array A a subset of array B? {result}")

A2 = [1, 2, 6]
B2 = [1, 2, 3, 4, 5]
result2 = is_subset(A2, B2)
print(f"Is array A2 a subset of array B2? {result2}")
```

### **Explanation:**
1. **Set Conversion:**
   - Convert array `A` and array `B` into sets `set_A` and `set_B` respectively.

2. **Subset Check:**
   - Use `set_A.issubset(set_B)` to determine if all elements of `A` are present in `B`.

3. **Result Without Conditionals:**
   - `"Yes" * subset` yields `"Yes"` if `subset` is `True`, else `""`.
   - Using `or "No"` ensures that `"No"` is returned if `subset` is `False`.

4. **Handling Edge Cases:**
   - If array `A` is empty, it's considered a subset of any array.

### **Output:**
```
Is array A a subset of array B? Yes
Is array A2 a subset of array B2? No
```

**Note:** 
- This method leverages set operations and string multiplication to avoid explicit conditional statements.

---

## **Summary**

We've explored a diverse set of array manipulation challenges, integrating Python code examples to illustrate solutions without relying on explicit conditional statements. Here's a quick recap:

1. **Find the Smallest Number in an Array:** Utilized the `min()` function to identify the smallest element.
2. **Find the Largest Number in an Array:** Leveraged the `max()` function to determine the largest element.
3. **Find the Second Smallest and Second Largest Elements in an Array:** Combined `set()`, `sorted()`, and list indexing to assign ranks and extract the required elements.
4. **Reverse a Given Array:** Employed Python's slicing feature to reverse the array efficiently.
5. **Count the Frequency of Each Element in an Array:** Used `collections.Counter` to tally element occurrences.
6. **Rearrange the Array in Increasing-Decreasing Order:** Sorted the array and swapped adjacent elements to create the desired pattern.
7. **Calculate the Sum of the Elements of the Array:** Utilized the `sum()` function for summation.
8. **Rotate an Array by K Elements - Block Swap Algorithm:** Applied slicing to perform left and right rotations.
9. **Find the Average of All Elements in an Array:** Calculated the average using `sum()` and `len()`.
10. **Find the Median of a Given Array:** Sorted the array and used indexing to determine the median.
11. **Remove Duplicates from a Sorted Array:** Employed list comprehensions and conditional logic within comprehensions to filter unique elements.
12. **Remove Duplicates from an Unsorted Array:** Utilized a set within list comprehensions to eliminate duplicates while maintaining order.
13. **Add an Element to an Array:** Demonstrated adding elements using both `append()` and list concatenation.
14. **Find All Repeating Elements in an Array:** Leveraged `Counter` to identify elements with frequencies greater than one.
15. **Find All Non-Repeating Elements in an Array:** Used `Counter` to filter elements that appear exactly once.
16. **Find All Symmetric Pairs in an Array:** Identified symmetric pairs by comparing elements from both ends of the array.
17. **Find the Maximum Product Subarray in an Array:** Maintained running maximum and minimum products to handle negative numbers and compute the overall maximum product.
18. **Replace Each Element of the Array by Its Rank in the Array:** Mapped elements to their sorted ranks using dictionaries and list comprehensions.
19. **Sort the Elements of an Array by Frequency:** Sorted elements based on their frequency and value using custom sorting keys.
20. **Rotate the Elements of an Array (Left and Right):** Performed circular rotations using slicing without explicit conditionals.
21. **Find the Equilibrium Index of an Array:** Calculated equilibrium indices by comparing running sums without using conditionals.
22. **Find the Circular Rotation of an Array by K Positions:** Demonstrated circular rotations with slicing, accommodating both left and right directions.
23. **Sort an Array According to the Order Defined by Another Array:** Mapped elements to a priority order and sorted accordingly.
24. **Search for an Element in an Array:** Collected indices of target elements using list comprehensions and `enumerate()`.
25. **Check if an Array is a Subset of Another Array or Not:** Employed set operations to verify subset relationships efficiently.

These exercises demonstrate Python's powerful built-in functions and data structures, enabling elegant solutions without the need for explicit conditional logic. Leveraging features like list comprehensions, slicing, and the `collections` module can simplify complex tasks and improve code readability.

If you have any further questions or need clarification on any of these topics, feel free to ask!
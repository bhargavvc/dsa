'''
Time Complexity 
breaking the list takes  O( Log N)
combining them to back take O(N)

so its O(N Log N)
'''

#this works only two lists are sorted
# array1 = [1,2, 3, 6]
# array2 = [10,32,65,87]

def mergeSort(array1, array2):

    combined = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):

        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1

    while i < len(array1):
        combined.append(array1[i])
        i += 1
    while j < len(array2):
        combined.append(array2[j])
        j += 1
    print(combined)

array1 = [1,2, 3, 6]
array2 = [10,32,65,87]
mergeSort(array1, array2)


#actual Merge sort code 
def merge_sort(array):
    if len(array) <= 1:  # Base case: arrays with 0 or 1 element are already sorted
        return array

    mid = len(array) // 2  # Find the midpoint to divide the array
    left_half = merge_sort(array[:mid])  # Recursively sort the left half
    right_half = merge_sort(array[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    combined = []
    i = j = 0

    # Merging the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1

    # Append remaining elements
    while i < len(left):
        combined.append(left[i])
        i += 1
    while j < len(right):
        combined.append(right[j])
        j += 1

    return combined

# Example usage
array = [3, 1, 4, 2, 5]
sorted_array = merge_sort(array)
print("Sorted Array:", sorted_array)

'''
sample iteration behind the logic
Sure! Let’s walk through the recursive process of **Merge Sort** step-by-step using the specific array `[3, 1, 4, 2, 5]`. We’ll show how the algorithm divides the array and then merges it back together without focusing on the specific values, just the process.

### Initial Array
```
[3, 1, 4, 2, 5]
```

### Step-by-Step Recursive Process

1. **Initial Call**:
   - **Input**: `[3, 1, 4, 2, 5]`
   - **Divide**: Split into two halves.
   - **Left Half**: `[3, 1]`
   - **Right Half**: `[4, 2, 5]`

---

### Sorting the Left Half: `[3, 1]`

2. **Call**: `merge_sort([3, 1])`
   - **Divide**: Split into `[3]` and `[1]`.
   - Both `[3]` and `[1]` are single-element arrays and are thus sorted.

3. **Merge**: Combine `[3]` and `[1]`:
   - Compare `3` and `1`. 
   - Result: `[1, 3]`

---

### Sorting the Right Half: `[4, 2, 5]`

4. **Call**: `merge_sort([4, 2, 5])`
   - **Divide**: Split into `[4]` and `[2, 5]`.

5. **Sorting the Right Half**: Now sort `[2, 5]`:
   - **Call**: `merge_sort([2, 5])`
   - **Divide**: Split into `[2]` and `[5]`.
   - Both are single-element arrays and are thus sorted.

6. **Merge**: Combine `[2]` and `[5]`:
   - Compare `2` and `5`. 
   - Result: `[2, 5]`

---

### Merging the Right Half: Combine `[4]` and `[2, 5]`

7. **Merge**: Combine `[4]` and `[2, 5]`:
   - Compare `4` with `2` and `5`.
   - Result: `[2, 4, 5]`

---

### Final Merge: Combine `[1, 3]` and `[2, 4, 5]`

8. **Merge**: Combine `[1, 3]` and `[2, 4, 5]`:
   - Compare elements:
     - `1` < `2` ➜ Add `1`
     - `3` < `2` ➜ Add `2`
     - `3` < `4` ➜ Add `3`
     - Add remaining `4` and `5`.
   - Result: `[1, 2, 3, 4, 5]`

---

### Final Sorted Array
The sorted array is:
```
[1, 2, 3, 4, 5]
```

### Summary of the Process
- **Dividing**: The array is recursively divided into smaller sub-arrays until only single elements remain.
- **Merging**: Each level of recursion merges the sorted sub-arrays back together in order, leading to the final sorted array.

This example illustrates the recursive nature of Merge Sort while sorting the specific array `[3, 1, 4, 2, 5]`.
'''
## **Find Minimum in Rotated Sorted Array (LeetCode #153)**

   - Modified binary search

### **Problem Statement:**

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]` if it was rotated `4` times. Given the rotated sorted array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in \( O(\log N) \) time complexity.

**Example:**
- **Input:** `[3, 4, 5, 1, 2]`
- **Output:** `1`
- **Explanation:** The minimum value in the rotated array is `1`.

- **Input:** `[4, 5, 6, 7, 0, 1, 2]`
- **Output:** `0`
- **Explanation:** The minimum value in the rotated array is `0`.

### **Key Insight for Optimal Solution:**

#### **1. Understanding the Rotated Array:**

When a sorted array is rotated, the leftmost and rightmost values no longer provide direct information about whether the array is sorted. However, the key property of a rotated sorted array is that there is a "pivot point" where the rotation occurs. The minimum value lies at or immediately after this pivot point.

#### **2. Goal:**
We aim to find the minimum value using **binary search** to achieve \( O(\log N) \) time complexity. The idea is to leverage the properties of a sorted and rotated array.

### **Approach Using Binary Search:**

The binary search approach works by identifying which part of the array is sorted and narrowing down the search range accordingly:

1. **Identify Middle Element:**
   - Calculate the mid-point of the current search range (`left` to `right`).

2. **Compare the Middle Element with the Rightmost Element:**
   - If `nums[mid] > nums[right]`, it means that the smallest element must lie in the right half of the array (the pivot point is in the right half). Therefore, move `left` to `mid + 1`.
   - If `nums[mid] <= nums[right]`, it means the smallest element is either the mid element itself or lies in the left half. Therefore, move `right` to `mid`.

3. **Repeat until the left and right pointers converge**.

### **Optimal Approach Explanation:**

1. **Why This Works:**
   - The binary search leverages the sorted and rotated property of the array. By comparing `nums[mid]` with `nums[right]`, we can determine which half of the array contains the smallest element.

2. **Time Complexity:** \( O(\log N) \) — We are dividing the search range in half at each step.
3. **Space Complexity:** \( O(1) \) — Only a few extra variables are used.

---

### **Binary Search Code:**

```python
def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        # Check if mid element is greater than the rightmost element
        if nums[mid] > nums[right]:
            # The minimum must be in the right half
            left = mid + 1
        else:
            # The minimum could be the mid element or in the left half
            right = mid

    return nums[left]
```

### **Explanation of the Code:**

1. **Initialization:**
   - Set `left` to the start of the array and `right` to the end.

2. **Loop Condition:**
   - The loop continues while `left` is less than `right`. This ensures that we only stop when the minimum element is identified.

3. **Calculate the Middle Point:**
   - `mid = (left + right) // 2` — This finds the middle index of the current range.

4. **Determine Which Half to Search:**
   - If `nums[mid] > nums[right]`, it means the smallest element must lie in the right half. So, set `left` to `mid + 1`.
   - Otherwise, the smallest element could be at `mid` or in the left half, so set `right` to `mid`.

5. **Return the Result:**
   - When `left` equals `right`, the minimum element is at `left`.

---

### **Conceptual Visualization:**

**Example:** `[4, 5, 6, 7, 0, 1, 2]`

- **Step 1:** `left = 0, right = 6, mid = 3` → `nums[mid] = 7`, `nums[right] = 2`. Since `nums[mid] > nums[right]`, the minimum is in the right half. Update `left` to `4`.
- **Step 2:** `left = 4, right = 6, mid = 5` → `nums[mid] = 1`, `nums[right] = 2`. Since `nums[mid] <= nums[right]`, the minimum could be at `mid` or in the left half. Update `right` to `5`.
- **Step 3:** `left = 4, right = 5, mid = 4` → `nums[mid] = 0`, `nums[right] = 1`. Since `nums[mid] <= nums[right]`, the minimum is at `mid` or in the left half. Update `right` to `4`.
- **Step 4:** `left = 4, right = 4` — Loop ends. The minimum element is `0`.

---

### **Final Takeaway:**

- **Binary Search** efficiently finds the minimum element in a rotated sorted array by leveraging the properties of sorted and rotated subarrays.
- The key is to compare the middle element with the rightmost element to determine the half where the minimum resides.

### **Time and Space Complexity Analysis:**

- **Time Complexity:** \( O(\log N) \) — Each iteration halves the search range.
- **Space Complexity:** \( O(1) \) — Only a few extra pointers are used.

By understanding the problem and implementing the solution using binary search, we efficiently locate the minimum element in a rotated sorted array.

---
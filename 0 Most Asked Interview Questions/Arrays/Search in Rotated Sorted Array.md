

   - Two-pass binary search

## **Search in Rotated Sorted Array (LeetCode #33)**

### **Problem Statement:**

Given an integer array `nums` sorted in ascending order, and rotated at some pivot unknown to you beforehand (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`), and a target value `target`, write a function to search `target` in `nums`. If `target` exists in the array, return its index, otherwise, return `-1`.

You must write an algorithm with \( O(\log N) \) time complexity.

**Example 1:**
- **Input:** nums = `[4,5,6,7,0,1,2]`, target = `0`
- **Output:** `4`

**Example 2:**
- **Input:** nums = `[4,5,6,7,0,1,2]`, target = `3`
- **Output:** `-1`

### **Key Insight for Solution:**

The array is rotated, but crucially, one half of the array (either the left or right side) will always remain sorted after the rotation. This property allows us to effectively use binary search.

### **Approach Using Modified Binary Search:**

1. **Identify the Sorted Half:**
   - During each iteration of binary search, identify which half of the array is sorted.

2. **Determine the Search Range:**
   - If the target is within the range of the sorted half, narrow the search to that half.
   - Otherwise, search in the other half.

3. **Repeat Until the Target is Found or the Search Space is Exhausted.**

### **Binary Search Implementation:**

```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the mid element is the target
        if nums[mid] == target:
            return mid

        # Determine which half is properly sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            # Check if the target lies in the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            # Check if the target lies in the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

### **Explanation of the Code:**

1. **Binary Search Initialization:**
   - Begin with pointers `left` and `right` at the start and end of the array, respectively.

2. **Loop Until `left` Exceeds `right`:**
   - Compute the middle index, `mid`, of the current search range.
   - If `nums[mid]` is the target, return the index `mid`.

3. **Identify the Sorted Segment:**
   - If the left half is sorted (`nums[left] <= nums[mid]`):
     - Check if the target lies within this sorted range. If yes, adjust `right` to search this half. If no, adjust `left` to search the right half.
   - If the right half is sorted:
     - Check if the target lies within this sorted range. If yes, adjust `left` to search this half. If no, adjust `right` to search the left half.

### **Conceptual Visualization:**

The decision-making process is guided by the position of the `mid` relative to the `left` and `right` and by comparing the target value with the boundaries of the current sorted segment. This strategy effectively narrows down the search to the segment that must contain the target, leveraging the sorted property of that segment.

### **Time and Space Complexity:**

- **Time Complexity:** \( O(\log N) \) — Each step of the binary search halves the size of the search space.
- **Space Complexity:** \( O(1) \) — The space usage is constant since only a few variables are used for index tracking.

### **Final Thoughts:**

This approach efficiently searches for an element in a rotated sorted array by dynamically adjusting the search space based on the sorted segment of the array. This ensures that the algorithm consistently performs in logarithmic time, making it well-suited for large datasets.

By understanding and implementing this modified binary search technique, you can effectively handle variations of the binary search problem, especially those involving searches in rotated or otherwise modified arrays.

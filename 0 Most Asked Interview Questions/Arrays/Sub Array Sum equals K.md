## **Subarray Sum Equals K (LeetCode #560)**

   - Cumulative sum with hash map

### **Problem Statement:**

You are given an integer array `nums` and an integer `k`. You need to find the total number of **continuous subarrays** whose sum equals `k`.

**Key Points:**
- A **subarray** is a contiguous part of the array.
- The elements of the subarray must sum up to the target value `k`.

### **Example 1:**

**Input:** `nums = [1, 1, 1]`, `k = 2`

**Output:** `2`

**Explanation:** 
- The subarrays that sum up to `2` are `[1, 1]` and `[1, 1]`. 

### **Example 2:**

**Input:** `nums = [1, 2, 3]`, `k = 3`

**Output:** `2`

**Explanation:** 
- The subarrays that sum up to `3` are `[1, 2]` and `[3]`.

### **Constraints:**

- The length of the array can be between 1 and \(2 \times 10^4\).
- The values in the array can be both positive and negative.

### **Goal:**
Find the number of contiguous subarrays in the given array `nums` whose sum equals `k`.

---

### **Approach to Solving the Problem:**

The problem can be solved using various methods. Let’s discuss an optimal solution that uses the concept of prefix sums with a hash map (dictionary in Python) for efficient lookup.

### **Optimal Solution Using Prefix Sum and Hash Map:**

**Why this works:**

The main idea is to keep track of the cumulative sum of the elements (`prefix_sum`) as we iterate through the array. As we progress, we want to know if there exists a prefix sum (earlier in the array) such that:

\[
\text{prefix\_sum} - k = \text{some earlier prefix sum}
\]

This indicates that there is a subarray with a sum of `k` between those two prefix sums.

### **Algorithm:**

1. **Initialize Variables:**
   - A hash map `prefix_sum_count` to store the count of occurrences of each prefix sum.
   - A variable `prefix_sum` to store the running cumulative sum of elements.
   - A variable `count` to store the total number of subarrays whose sum equals `k`.

2. **Iterate Through the Array:**
   - For each element `num` in `nums`:
     - Add the current element to the running `prefix_sum`.
     - Check if `(prefix_sum - k)` exists in `prefix_sum_count`. If it does, it means there exists a subarray ending at the current index that sums up to `k`. Add the number of occurrences of `(prefix_sum - k)` to `count`.
     - Update `prefix_sum_count` to include the current `prefix_sum`.

3. **Return the Count:** This gives the total number of subarrays whose sum equals `k`.

### **Time Complexity:** \( O(N) \), where \( N \) is the length of the array. We are iterating through the array once and performing \( O(1) \) operations for each element using the hash map.

### **Space Complexity:** \( O(N) \), where \( N \) is the length of the array. In the worst case, we might store all prefix sums in the hash map.

---

### **Optimal Solution Code:**

```python
def subarray_sum(nums, k):
    # Hash map to store the frequency of each prefix sum
    prefix_sum_count = {0: 1}
    prefix_sum = 0
    count = 0

    for num in nums:
        # Update the running sum
        prefix_sum += num

        # Check if (prefix_sum - k) exists in the hash map
        if prefix_sum - k in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k]

       prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum,1)+1

      #   # Update the hash map with the current prefix sum
      #   if prefix_sum in prefix_sum_count:
      #       prefix_sum_count[prefix_sum] += 1
      #   else:
      #       prefix_sum_count[prefix_sum] = 1

    return count
```

### **Explanation of the Code:**

1. **Initialization:**
   - We initialize a hash map `prefix_sum_count` with a key of `0` and value of `1` to handle the case when a subarray starting from the first element itself equals `k`.
   - We also initialize `prefix_sum` to `0` to track the running sum of elements and `count` to store the number of subarrays that sum up to `k`.

2. **Iterate Through Each Element in the Array:**
   - Update the `prefix_sum` by adding the current element.
   - Check if `(prefix_sum - k)` exists in `prefix_sum_count`. If it does, add the count of occurrences of `(prefix_sum - k)` to the `count`. This step indicates that there are subarrays ending at the current index whose sum equals `k`.
   - Update the count of `prefix_sum` in the hash map.

3. **Return the Count:** Finally, return the total count of subarrays whose sum equals `k`.

---

### **Visual Example:**

Let’s use an example to visualize the algorithm:

**Example:** `nums = [1, 2, 3]`, `k = 3`

- **Iteration 1:** 
  - Current number: `1`
  - `prefix_sum = 0 + 1 = 1`
  - `(prefix_sum - k) = 1 - 3 = -2` → Not in hash map.
  - Update `prefix_sum_count = {0: 1, 1: 1}`
- **Iteration 2:** 
  - Current number: `2`
  - `prefix_sum = 1 + 2 = 3`
  - `(prefix_sum - k) = 3 - 3 = 0` → Found in hash map (with value `1`).
  - Increase count by `1` → `count = 1`
  - Update `prefix_sum_count = {0: 1, 1: 1, 3: 1}`
- **Iteration 3:** 
  - Current number: `3`
  - `prefix_sum = 3 + 3 = 6`
  - `(prefix_sum - k) = 6 - 3 = 3` → Found in hash map (with value `1`).
  - Increase count by `1` → `count = 2`
  - Update `prefix_sum_count = {0: 1, 1: 1, 3: 1, 6: 1}`

**Result:** `count = 2`

### **Final Takeaway:**

The hash map-based solution effectively tracks the prefix sums and counts occurrences of each prefix sum. By checking if `(prefix_sum - k)` exists in the hash map, we efficiently determine if there are subarrays whose sum equals `k`.

### **Key Points to Remember:**

1. **Prefix Sum Concept:** The solution relies on computing a running sum of elements and using the difference between the current prefix sum and `k` to identify subarrays.
2. **Hash Map for Efficient Lookup:** The hash map stores the frequency of each prefix sum, allowing for efficient lookups in constant time.
3. **Handling Edge Cases:** The initialization of the hash map with `{0: 1}` handles the case where a subarray starting from the first element sums to `k`.

By understanding the prefix sum technique and the use of hash maps, you can solve similar problems involving sums and subarrays efficiently.
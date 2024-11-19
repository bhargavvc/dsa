

Here’s a detailed 7-step explanation for solving LeetCode Problem 136: **Single Number**.

---

### **1. Problem Statement**

- **Objective**: Given a non-empty array of integers `nums`, every element appears **twice** except for one. Find that single one.
- **Constraints**:
  - `1 <= nums.length <= 3 * 10^4`
  - `-3 * 10^4 <= nums[i] <= 3 * 10^4`
  - Every element appears twice except for one.

---

### **2. Understanding the Problem**

- **Duplicate Elements**: All elements except one appear exactly twice.
- **Unique Element**: One element appears only once.
- **Goal**: Identify the unique element.
- **Requirements**:
  - **Time Complexity**: Must be linear, i.e., O(n).
  - **Space Complexity**: Must use constant extra space, i.e., O(1).

---

### **3. Algorithm Explanation**

- **Bitwise XOR Operation**:
  - **Property 1**: `a ^ a = 0` (XOR of a number with itself is 0).
  - **Property 2**: `a ^ 0 = a` (XOR of a number with 0 is the number itself).
  - **Property 3**: XOR is **commutative** and **associative**.
- **Approach**:
  - Initialize a variable `result` to 0.
  - Iterate through each number in the array and perform XOR with `result`.
  - After the iteration, `result` will hold the unique number.

---

### **4. Implementation**

```python
def singleNumber(nums):
    result = 0  # Step 1: Initialize result to 0
    for num in nums:
        result ^= num  # Step 2: XOR current number with result
    return result  # Step 3: Return the unique number
```

---

### **5. Complexity Analysis**

- **Time Complexity**: O(n)
  - We traverse the list once.
- **Space Complexity**: O(1)
  - Only a single variable `result` is used regardless of input size.

---

### **6. Test Cases**

1. **Example 1**:
   - **Input**: `[2, 2, 1]`
   - **Process**:
     - `result = 0 ^ 2 = 2`
     - `result = 2 ^ 2 = 0`
     - `result = 0 ^ 1 = 1`
   - **Output**: `1`

2. **Example 2**:
   - **Input**: `[4, 1, 2, 1, 2]`
   - **Process**:
     - `result = 0 ^ 4 = 4`
     - `result = 4 ^ 1 = 5`
     - `result = 5 ^ 2 = 7`
     - `result = 7 ^ 1 = 6`
     - `result = 6 ^ 2 = 4`
   - **Output**: `4`

3. **Example 3**:
   - **Input**: `[1]`
   - **Process**:
     - `result = 0 ^ 1 = 1`
   - **Output**: `1`

---

### **7. Detailed Explanation**

- **Why XOR Works in This Scenario**:
  - Since XOR of two identical numbers is 0, all numbers appearing twice will cancel each other out.
  - The XOR operation accumulates the unique number because `0 ^ unique_number = unique_number`.
- **Step-by-Step Execution**:
  - **Initialization**:
    - Set `result` to 0.
  - **Iteration**:
    - For each element `num` in `nums`, update `result` using `result ^= num`.
  - **Final Result**:
    - After processing all elements, `result` contains the single number.

---

**Note**: This solution satisfies the constraints by achieving O(n) time complexity and O(1) space complexity, using bit manipulation to find the unique element efficiently.
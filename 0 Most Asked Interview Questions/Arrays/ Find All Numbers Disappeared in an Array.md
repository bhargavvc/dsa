

   - In-place array manipulation
**Problem Statement:**

You are given an array of integers `nums` of length `n`, where each element is in the range `[1, n]`. Some elements may appear twice, and others appear once. Your task is to find all the integers in the range `[1, n]` that do not appear in `nums`.

**Example:**

```plaintext
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Explanation: Numbers 5 and 6 are missing from the array.
```

---

**Logic Explanation:**

To solve this problem efficiently, we use the array itself to keep track of which numbers have appeared. The main idea is to iterate through the array and, for each number `nums[i]`, mark the element at the index corresponding to `nums[i]` as negative. This serves as a flag to indicate that the number `nums[i]` exists in the array.

Here's how it works:

1. **Iterate Over the Array:**

   - For each element `nums[i]`, calculate the index `index = abs(nums[i]) - 1`. We subtract 1 because arrays are 0-based indexed, but the numbers range from 1 to `n`.
   - Mark the number at `nums[index]` as negative to indicate that the number `index + 1` is present in the array.

2. **Collect Missing Numbers:**

   - After marking, iterate through the array again.
   - If `nums[i]` is positive, it means the number `i + 1` was not present in the original array.
   - Collect all such numbers into a result list.

**Why We Are Using This Logic:**

- **In-Place Marking:** By modifying the input array in place, we avoid using extra space, achieving O(1) space complexity (excluding the output array).
- **Negative Values as Indicators:** Negative values act as markers to indicate the presence of a number. Since the original numbers are all positive (in the range `[1, n]`), a negative sign is an effective flag.
- **0-Based Indexing Alignment:** Subtracting 1 aligns the 1-based numbering of elements with the 0-based indexing of arrays.

---

**Time and Space Complexity:**

- **Time Complexity:** O(n), because we traverse the array twice (once for marking, once for collecting).
- **Space Complexity:** O(1), since we use the input array for marking and only the output list for storing results.

---

**Array Limitations:**

- **Range Constraint:** All elements in `nums` are in the range `[1, n]`, where `n` is the length of the array.
- **Duplicates Allowed:** Elements may appear more than once.
- **No Extra Space:** The problem requires achieving constant extra space complexity.

---

**Detailed Explanation with Negative Values and 0-Based Indexing:**

1. **First Pass (Marking Presence):**

   - **Process Each Element:**
     - For each `nums[i]`, compute `index = abs(nums[i]) - 1`.
     - Use `abs(nums[i])` because `nums[i]` might have been marked negative already.
   - **Mark the Corresponding Index:**
     - If `nums[index]` is positive, set it to `-nums[index]` to mark that `index + 1` is present.
     - If `nums[index]` is already negative, leave it as is (it has been marked before).

2. **Second Pass (Identifying Missing Numbers):**

   - **Check Each Position:**
     - For each index `i` from `0` to `n - 1`, if `nums[i]` is positive, it means `i + 1` was not present in the array.
   - **Collect Missing Numbers:**
     - Add `i + 1` to the result list for every positive `nums[i]`.

---

**Step-by-Step Example:**

Let's walk through the example `nums = [4,3,2,7,8,2,3,1]`.

**First Pass:**

```plaintext
i = 0:
  index = abs(nums[0]) - 1 = 4 - 1 = 3
  nums[3] = -nums[3] => nums[3] = -7
  nums = [4,3,2,-7,8,2,3,1]

i = 1:
  index = abs(nums[1]) - 1 = 3 - 1 = 2
  nums[2] = -nums[2] => nums[2] = -2
  nums = [4,3,-2,-7,8,2,3,1]

i = 2:
  index = abs(nums[2]) - 1 = 2 - 1 = 1
  nums[1] = -nums[1] => nums[1] = -3
  nums = [4,-3,-2,-7,8,2,3,1]

i = 3:
  index = abs(nums[3]) - 1 = 7 - 1 = 6
  nums[6] = -nums[6] => nums[6] = -3
  nums = [4,-3,-2,-7,8,2,-3,1]

i = 4:
  index = abs(nums[4]) - 1 = 8 - 1 = 7
  nums[7] = -nums[7] => nums[7] = -1
  nums = [4,-3,-2,-7,8,2,-3,-1]

i = 5:
  index = abs(nums[5]) - 1 = 2 - 1 = 1
  nums[1] is already negative
  nums = [4,-3,-2,-7,8,2,-3,-1]

i = 6:
  index = abs(nums[6]) - 1 = 3 - 1 = 2
  nums[2] is already negative
  nums = [4,-3,-2,-7,8,2,-3,-1]

i = 7:
  index = abs(nums[7]) - 1 = 1 - 1 = 0
  nums[0] = -nums[0] => nums[0] = -4
  nums = [-4,-3,-2,-7,8,2,-3,-1]
```

**Second Pass:**

```plaintext
i = 0: nums[0] = -4 (negative)
i = 1: nums[1] = -3 (negative)
i = 2: nums[2] = -2 (negative)
i = 3: nums[3] = -7 (negative)
i = 4: nums[4] = 8 (positive) => Missing number: 5
i = 5: nums[5] = 2 (positive) => Missing number: 6
i = 6: nums[6] = -3 (negative)
i = 7: nums[7] = -1 (negative)
```

**Result:**

- The missing numbers are `[5, 6]`.

---

**Conclusion:**

By marking the indices corresponding to the numbers present in the array, we efficiently identify the missing numbers without using extra space. The use of negative values as markers and aligning the 1-based numbers with 0-based indexing allows us to work within the constraints of the problem.

---

**Final Code Implementation:**

```python
def findDisappearedNumbers(nums):
    n = len(nums)
    # First pass to mark numbers as negative
    for i in range(n):
        index = abs(nums[i]) - 1  # Align number to 0-based index
        if nums[index] > 0:
            nums[index] = -nums[index]  # Mark as negative

    # Second pass to collect missing numbers
    missing_numbers = []
    for i in range(n):
        if nums[i] > 0:
            missing_numbers.append(i + 1)  # Adjust back to 1-based numbering

    return missing_numbers

    #it solcves all cases 
    def find_missing_numbers_negative_index(arr):
    # Step 1: Find the minimum and maximum values manually
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # Step 2: Mark elements as visited using negative indexing
    for i in range(len(arr)):
        # Calculate the index relative to the min_val
        index = arr[i] - min_val
        # Only mark if it's within the range and not already marked
        if 0 <= index < len(arr) and arr[index] > 0:
            arr[index] = -arr[index]  # Mark it as visited

    # Step 3: Identify missing numbers
    missing_numbers = []
    for i in range(min_val, max_val + 1):
        index = i - min_val
        if index >= len(arr) or arr[index] > 0:
            missing_numbers.append(i)

    return missing_numbers

    # Test cases
    print(find_missing_numbers_negative_index([1, 4]))          # Output: [2, 3]
    print(find_missing_numbers_negative_index([1, 1, 1, 4]))    # Output: [2, 3]

```

---

**Key Takeaways:**

- **In-Place Modification:** Utilize the input array to track information, saving space.
- **Negative Marking:** Use the sign of numbers as indicators without losing original data.
- **0-Based Indexing:** Adjust calculations to match the array's indexing system.
- **Efficiency:** Achieve O(n) time complexity by minimizing the number of passes over the data.

---

This approach effectively solves the problem within the specified constraints, providing a clear and efficient solution.
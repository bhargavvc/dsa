**Problem Statement:**

Given the head of a singly linked list, determine if the linked list has a cycle in it.

- **Input:** `head` (the head node of a singly linked list)
- **Output:** `True` if there is a cycle, `False` otherwise

A cycle occurs when a node's `next` pointer points back to a previous node in the list, creating a loop. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

---

**Solution Code:**

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head):
    # Initialize slow and fast pointers
    slow = head
    fast = head

    # Traverse the list
    while fast and fast.next:
        slow = slow.next          # Move slow pointer by 1
        fast = fast.next.next     # Move fast pointer by 2

        # Check if the two pointers meet
        if slow == fast:
            return True  # Cycle detected

    # If we reach here, no cycle exists
    return False
```

---

**Time and Space Complexity:**

- **Time Complexity:** O(n), where **n** is the number of nodes in the linked list.
  - Each node is visited at most once by each pointer.
  - The fast pointer moves twice as fast, but both pointers together cover at most `2n` steps.
  - Therefore, the algorithm runs in linear time relative to the size of the list.

- **Space Complexity:** O(1) (constant space)
  - Only a fixed number of variables (`slow` and `fast`) are used, regardless of the input size.
  - No additional data structures that scale with the input size are used.

**Explanation:**


---

## **Example Walkthrough:**

Consider a linked list with nodes A → B → C → D → E → C (cycle starting at node C).

1. **Initialization:**
   - `slow` at A
   - `fast` at A

2. **First Iteration:**
   - `slow` moves to B
   - `fast` moves to C

3. **Second Iteration:**
   - `slow` moves to C
   - `fast` moves to E

4. **Third Iteration:**
   - `slow` moves to D
   - `fast` moves to D (since E → C → D) (E.next(i.e c).next--> D)

5. **Meeting Point:**
   - `slow` and `fast` both at node D
   - Cycle detected.

---

## **Edge Cases to Consider:**

1. **Empty List (`head` is `None`):**
   - The function should return `False`.
   - **Explanation:** There are no nodes, so no cycle can exist.

2. **Single Node without Cycle:**
   - A single node pointing to `None` should return `False`.
   - **Explanation:** The node does not loop back to itself.

3. **Single Node with Cycle (node pointing to itself):**
   - Should return `True`.
   - **Explanation:** The node's `next` pointer references itself, forming a cycle.

---
---

Let's solve the problem **"141. Linked List Cycle"** step by step, explaining the logic and reasoning behind the chosen approach.

---

## **Understanding the Problem:**

- A **cycle** in a linked list occurs when a node's `next` pointer points back to a previous node in the list, creating a loop.
- We need to detect if such a cycle exists without modifying the linked list.

---

## **Approach:**

To detect a cycle in a linked list efficiently, we can use **Floyd's Tortoise and Hare Algorithm** (also known as the **Two-Pointer Technique**).

### **Why Choose This Approach?**

- **Time Efficiency:** It operates in O(n) time, where n is the number of nodes.
- **Space Efficiency:** It uses O(1) extra space (constant space).
- **Effectiveness:** It reliably detects cycles in a linked list.

### **Logic Behind the Algorithm:**

- **Two Pointers:**
  - **Slow Pointer (Tortoise):** Moves one step at a time.
  - **Fast Pointer (Hare):** Moves two steps at a time.
- **Cycle Detection:**
  - If there is **no cycle**, the fast pointer will reach the end (`null`) before the slow pointer.
  - If there **is a cycle**, the fast pointer will eventually meet the slow pointer within the cycle.

### **Step-by-Step Explanation:**

1. **Traverse the List:**
   - Move `slow` one step forward: `slow = slow.next`.
   - Move `fast` two steps forward: `fast = fast.next.next`.


2. **Loop Until Conclusion:**
   - Continue the traversal until `fast` is `null` or `fast.next` is `null` (meaning the end of the list is reached).
   - If the loop exits without `slow` meeting `fast`, return `False`.

---

## **Detailed Explanation of the Code:**

1. **Node Definition:**

   ```python
   class ListNode:
       def __init__(self, val=0):
           self.val = val
           self.next = None
   ```

   - Defines a node in the singly linked list with a value `val` and a pointer `next`.


2. **Traverse the List Using a Loop:**

   ```python
   while fast and fast.next:
   ```

   - Continues as long as `fast` and `fast.next` are not `None`.
   - Ensures that `fast.next.next` in the next step does not raise an exception.

3. **Move Pointers Forward:**

   ```python
   slow = slow.next
   fast = fast.next.next
   ```

   - `slow` moves one node ahead.
   - `fast` moves two nodes ahead.

4. **No Cycle Detected:**

   ```python
   return False
   ```

   - If the loop ends without `slow` meeting `fast`, it means `fast` reached the end (`null`).
   - The function returns `False`.

---

## **Why This Logic Works:**

- **Intuition:**
  - In a cyclic linked list, the fast pointer will eventually loop around and meet the slow pointer.
- **Mathematical Proof:**
  - They are moving at different speeds, so in a cyclic path, the distance between them decreases by one node each iteration, eventually leading to a meeting point.
- **Efficiency:**
  - Only requires constant extra space.
  - Traverses the list at most twice.


## **Alternative Approaches:**

### **1. Using a Hash Set:**

- **Logic:**
  - Traverse the list and store each visited node in a set.
  - If a node is revisited (found in the set), a cycle exists.

- **Implementation:**

  ```python
  def hasCycle(head):
      visited = set()
      current = head
      while current:
          if current in visited:
              return True
          visited.add(current)
          current = current.next
      return False
  ```

- **Time Complexity:** O(n)
  - Each node is visited once.
- **Space Complexity:** O(n)
  - In the worst case (no cycle), all nodes are stored in the `visited` set.

### **Why Not Use This Approach?**

- **Higher Space Usage:**
  - Requires O(n) extra space to store visited nodes.
- **Less Efficient:**
  - For large lists, the space consumption can be significant.
- **Preferred Approach:**
  - Floyd's algorithm is more space-efficient, using only constant extra space.

---

## **Final Thoughts:**

- **Floyd's Tortoise and Hare Algorithm** is preferred for its space efficiency.
- It's important to handle edge cases to ensure the function is robust.
- Understanding the underlying principles helps in applying similar techniques to other problems.

---

**Remember:** When dealing with linked lists and cycles, the two-pointer technique is a powerful tool for cycle detection with optimal time and space complexity.
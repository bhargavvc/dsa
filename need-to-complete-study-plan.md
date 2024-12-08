### **Week 4: Trees & Binary Search Trees**

#### **Concepts to Learn**
1. **Tree Traversal Methods:**
   - **Inorder Traversal (Left-Root-Right):** Visits the left subtree, then the root, and finally the right subtree. For a binary search tree (BST), this gives elements in sorted order.
   - **Preorder Traversal (Root-Left-Right):** Visits the root first, then the left subtree, and finally the right subtree. Useful for creating a copy of the tree.
   - **Postorder Traversal (Left-Right-Root):** Visits the left and right subtrees before visiting the root. Commonly used for deleting a tree or evaluating expressions.

2. **Binary Search Tree (BST) Properties:**
   - The left child of a node contains a value smaller than the node.
   - The right child of a node contains a value greater than the node.
   - Inorder traversal of a BST gives values in ascending order.

3. **Balanced Tree:** A tree where the height difference between left and right subtrees for any node is not more than 1.

#### **Practice Problems**
1. **Inorder Traversal:** Write a recursive and iterative solution to traverse a binary tree in inorder.
2. **Check if a Tree is Balanced:** Implement a function that calculates the height of left and right subtrees and ensures the height difference is ≤1 at every node.

---

### **Week 5: Graphs & Graph Algorithms**

#### **Concepts to Learn**
1. **Graphs Representation:**
   - **Adjacency Matrix:** A 2D matrix where `matrix[i][j] = 1` if there's an edge from vertex `i` to vertex `j`.
   - **Adjacency List:** A list where each index represents a vertex, and the values are the vertices it's connected to.

2. **Graph Traversal Algorithms:**
   - **BFS (Breadth-First Search):**
     - Traverses the graph level by level.
     - Uses a queue for implementation.
     - Suitable for finding the shortest path in an unweighted graph.
   - **DFS (Depth-First Search):**
     - Traverses as far as possible along one branch before backtracking.
     - Uses a stack (or recursion).

3. **Shortest Path Algorithms:**
   - **Dijkstra’s Algorithm:** Finds the shortest path in a weighted graph.
   - **Bellman-Ford Algorithm:** Similar to Dijkstra but handles negative weights.
   - **Floyd-Warshall Algorithm:** Finds shortest paths between all pairs of nodes.

#### **Practice Problems**
1. **Implement BFS and DFS:** Write iterative and recursive solutions for both.
2. **Find the Shortest Path:** Solve using BFS for unweighted graphs and Dijkstra for weighted graphs.

---

### **Week 6: Sorting & Searching Algorithms**

#### **Concepts to Learn**
1. **Sorting Algorithms:**
   - **Merge Sort:**
     - A divide-and-conquer algorithm.
     - Divides the array into halves, recursively sorts each half, and merges the sorted halves.
     - **Time Complexity:** O(n log n).
   - **Quick Sort:**
     - Selects a pivot and partitions the array such that elements smaller than the pivot are on the left, and larger ones are on the right.
     - **Time Complexity:** O(n log n) on average, O(n²) in the worst case.

2. **Binary Search:**
   - Efficient search algorithm for sorted arrays.
   - **Time Complexity:** O(log n).

3. **Binary Search in Rotated Array:**
   - A modified binary search to handle sorted arrays that have been rotated at an unknown pivot.
   - Identify the sorted half of the array and decide where to search.

#### **Practice Problems**
1. **Merge Sort:** Implement merge sort for an array and explain each step.
2. **Quick Sort:** Solve a problem requiring partitioning logic.
3. **Binary Search in Rotated Array:** Find an element in a rotated sorted array.

---

### **Week 7: Dynamic Programming (DP)**

#### **Concepts to Learn**
1. **Principles of Dynamic Programming:**
   - Break the problem into smaller subproblems.
   - Solve each subproblem only once and store its result (memoization or tabulation).
   - Common patterns include:
     - **Overlapping Subproblems:** Problems can be broken into smaller, repeating problems.
     - **Optimal Substructure:** An optimal solution can be constructed from the optimal solutions of its subproblems.

2. **Common DP Problems:**
   - **Fibonacci Sequence:**
     - Compute the nth Fibonacci number using recursion + memoization or bottom-up tabulation.
     - **Time Complexity:** O(n).
   - **Longest Common Subsequence (LCS):**
     - Find the longest sequence present in both strings in the same order but not necessarily contiguous.
     - **Time Complexity:** O(n × m), where n and m are the lengths of the strings.

#### **Practice Problems**
1. **Fibonacci Sequence:**
   - Write both recursive and iterative solutions with memoization and tabulation.
2. **Longest Common Subsequence:**
   - Implement a DP table to solve LCS.
   - Backtrack through the table to reconstruct the sequence.

---

### **Detailed Explanation of Each Practice Problem**

#### **1. Inorder Traversal:**
- Traverse the tree using the pattern: Left → Root → Right.
- Example: For a tree with nodes `[3, 2, 5, 1, 4]`, the inorder traversal gives `[1, 2, 3, 4, 5]`.

#### **2. Check if a Tree is Balanced:**
- Recursively calculate the height of left and right subtrees for each node.
- Verify if the difference in heights is ≤1 for all nodes.

#### **3. Implement BFS and DFS:**
- BFS: Use a queue to explore all neighbors of a node before moving to the next level.
- DFS: Use a stack (or recursion) to explore one path fully before backtracking.

#### **4. Merge Sort:**
- Example: Split `[38, 27, 43, 3, 9]` into `[38, 27]` and `[43, 3, 9]`. Recursively sort and merge back to get `[3, 9, 27, 38, 43]`.

#### **5. Binary Search in Rotated Array:**
- Find the pivot point where the rotation occurs.
- Perform binary search in the appropriate half of the array.

#### **6. Fibonacci Sequence:**
- Use memoization:
  - Base cases: `fib(0) = 0`, `fib(1) = 1`.
  - Recurrence relation: `fib(n) = fib(n-1) + fib(n-2)`.

#### **7. Longest Common Subsequence:**
- Example: For `ABCD` and `ACBAD`, the LCS is `ABD`.
- Use a DP table where `dp[i][j]` represents the LCS of the first `i` characters of one string and `j` characters of the other.

---

This progression helps you master each topic systematically, with theoretical and practical exposure to problems!
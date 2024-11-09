Let me explain the logic behind the implementation of your `is_valid_brackets` function in detail, including why the approach you used is appropriate for matching brackets:

### Code Breakdown

```python
def is_valid_brackets(string):
    stack = []  # Initialize an empty stack to store the opening brackets
    
    # Define the symbols for open and closed brackets
    open_symbols = "{[("
    closed_symbols = "})]"
    
    # Define the matched symbols, i.e., what each closing bracket should match with
    matched_symbols = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    
    for sym in string:  # Loop through each character in the string
        if sym in open_symbols:  # If the character is an open symbol
            stack.append(sym)  # Push the open bracket onto the stack
        elif sym in closed_symbols:  # If the character is a close symbol
            if stack and stack[-1] == matched_symbols[sym]:  # Check if the top of the stack matches
                stack.pop()  # If it matches, pop the open bracket from the stack
            else:
                return False  # If it doesn't match, return False (unbalanced)
    
    # After iterating through the string, check if the stack is empty
    return True if not stack else False
```

### Step-by-Step Explanation of the Logic

1. **Use of Stack**:
   - A **stack** is used to solve the problem because stacks follow a **Last In, First Out (LIFO)** principle. This works perfectly for matching brackets, because:
     - The most recent opening bracket should be matched by the nearest closing bracket.
     - By using a stack, we ensure that brackets are closed in the correct order, respecting the **nesting** of brackets.

2. **Checking for Open and Close Symbols**:
   - We define two sets of symbols:
     - **Open symbols**: `{[(` for `{`, `[`, and `(`.
     - **Closed symbols**: `})]` for `}`, `]`, and `)`.
   - As we iterate through the string, we check each character to determine if it is an opening bracket (to be pushed onto the stack) or a closing bracket (to be matched).

3. **Matching Closing Brackets**:
   - The dictionary `matched_symbols` helps to quickly look up what each closing bracket should match with:
     - `"}": "{"`, meaning `}` should match with `{`.
     - `"]": "["`, meaning `]` should match with `[`.
     - `")": "("`, meaning `)` should match with `(`.
   - When a closing bracket is encountered, we check if the stack is not empty and if the bracket at the top of the stack matches the expected opening bracket (using `stack[-1]` to access the top of the stack).
     - If it matches, we pop the opening bracket from the stack (since the pair is now complete).
     - If it doesn't match or if the stack is empty (indicating there is no corresponding opening bracket), we return `False` immediately (since the brackets are unbalanced).

4. **Final Check**:
   - After processing the entire string, if the stack is empty, it means that all opening brackets had corresponding closing brackets, and the brackets are properly matched.
   - If the stack is not empty, it means there are unmatched opening brackets left, so we return `False`.

### Why This Logic Works

- **Order of Operations**: The LIFO nature of the stack ensures that the most recent opening bracket gets matched with the nearest closing bracket, making sure that brackets are properly nested.
- **Efficient Matching**: By using a dictionary for `matched_symbols`, we can quickly look up the corresponding opening bracket for each closing bracket, making the matching process fast and clear.
- **Early Termination**: If we encounter an unmatched closing bracket, the function returns `False` immediately, saving time by not having to process the rest of the string unnecessarily.
- **Final Check**: The condition `return True if not stack else False` ensures that we return `True` only if all brackets have been properly matched and no unmatched opening brackets remain.

### Why the Logic Is Chosen:
This approach is based on the following observations:
- **Brackets must be matched in pairs**: The first open bracket must be matched by the last closed bracket (respecting the LIFO structure).
- **Efficient handling with a stack**: A stack provides an efficient way to "remember" the most recent opening bracket and match it with a closing bracket.
- **Early Exit**: By immediately returning `False` when a mismatch is found, we avoid unnecessary operations and make the solution more efficient.

### Example Walkthrough:
Let’s walk through the example string `"([)]{}"`:

1. **`(`**: It’s an opening bracket, so we push it onto the stack: `stack = ["("]`.
2. **`[`**: Another opening bracket, so we push it onto the stack: `stack = ["(", "["]`.
3. **`)`**: A closing bracket. We check if it matches the top of the stack (`[`), but it doesn’t (it matches `(` instead). So, the function returns `False` because the brackets are unbalanced.

This logic works for any valid or invalid combination of brackets, ensuring correct matching and nesting.

### Final Thought
The stack-based approach is optimal for solving the problem of bracket matching because it ensures correct nesting and matching in an efficient manner. It’s widely used in problems involving balanced parentheses or similar nested structures.
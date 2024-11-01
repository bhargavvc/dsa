
## Function `stock_option` with Time and Space Complexity Annotations
- Track minimum price and maximum profit

```python
def stock_option(prices):
    # Initialize min_price to infinity to ensure any price in the list will be lower
    min_price = float('inf')  
    max_profit = 0             

    for price in prices:       
        if price < min_price:
            min_price = price  

        profit = price - min_price  

        if profit > max_profit:
            max_profit = profit    
            print(f"New max_profit found: {max_profit}") 


    return max_profit  

# Example usage:
array = [7, 1, 5, 3, 6, 4]
profit = stock_option(array)  
print(f"Maximum Profit: {profit}")  
```

#### 1. **Initialization:**
   - **`min_price = float('inf')`**
     - **Purpose:** Sets `min_price` to the highest possible value initially.
     - **Reasoning:** Ensures that any actual stock price in the `prices` list will be lower, allowing `min_price` to be updated on the first iteration.
     - **Implication:** Avoids handling the first element separately and provides a clean starting point for comparisons.
   - **`max_profit = 0`**
     - **Purpose:** Initializes the maximum profit to zero.
     - **Reasoning:** Since no transactions have been made yet, the initial profit is zero. This variable will store the highest profit found during iteration.

### Summary of Time and Space Complexity

| **Aspect**           | **Complexity** | **Explanation**                                                                                                                                                           |
|----------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Time Complexity**  | **O(n)**        | The function processes each element in the `prices` list exactly once within a single loop. All operations inside the loop are constant time (`O(1)`), leading to a linear time complexity relative to the input size `n`. |
| **Space Complexity** | **O(1)**        | The function uses a fixed amount of additional space regardless of the input size. Variables like `min_price`, `max_profit`, and `profit` consume constant space. No additional data structures that scale with input size are used.      |

#### **Implications of Complexities**

- **Time Efficiency:** With a linear time complexity (**O(n)**), the function scales efficiently even as the number of stock prices increases. This makes it suitable for large datasets where performance is critical.
  
- **Space Efficiency:** Constant space complexity (**O(1)**) ensures that the memory usage remains minimal and does not grow with the input size. This is particularly advantageous in environments with limited memory resources.

#### **Logic Behind the Two `if` Conditions:**
1. **First `if` Condition (`if price < min_price`):**
   - **Purpose:** Identifies and updates the lowest price to buy the stock.
   - **Outcome:** Ensures that all future profit calculations are based on the lowest possible buy price up to the current point in the list.

2. **Second `if` Condition (`if profit > max_profit`):**
   - **Purpose:** Determines whether selling at the current price yields a better profit than any previously recorded.
   - **Outcome:** Updates `max_profit` to the highest profit found during the iteration.

**Key Takeaways:**
- **Single Pass Efficiency:** By iterating through the list once and maintaining only necessary variables (`min_price` and `max_profit`), the function achieves optimal performance.
- **Dynamic Tracking:** Continuously updating `min_price` and `max_profit` ensures that the best possible transaction is identified without redundant computations.
- **Scalability:** The linear time complexity allows the function to handle extensive datasets gracefully, making it suitable for real-world applications where stock prices lists can be large.


### 1. **Example Walkthrough with `array = [7, 1, 5, 3, 6, 4]`**

Let's step through the function using the provided example to see how `min_price` and `max_profit` evolve:

1. **Initial State:**
   - `min_price = inf`
   - `max_profit = 0`

2. **First Price (7):**
   - **Check `if price < min_price`:** `7 < inf` → **True**
     - **Update `min_price`:** `min_price = 7`
   - **Calculate `profit`:** `7 - 7 = 0`
   - **Check `if profit > max_profit`:** `0 > 0` → **False**
     - **No update to `max_profit`.**
   - **State After Iteration:**
     - `min_price = 7`
     - `max_profit = 0`

3. **Second Price (1):**
   - **Check `if price < min_price`:** `1 < 7` → **True**
     - **Update `min_price`:** `min_price = 1`
   - **Calculate `profit`:** `1 - 1 = 0`
   - **Check `if profit > max_profit`:** `0 > 0` → **False**
     - **No update to `max_profit`.**
   - **State After Iteration:**
     - `min_price = 1`
     - `max_profit = 0`

   - ...
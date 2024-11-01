
# Understanding `while True` and Loop Control

- **`while loop`**: 
  - This loop continues to execute indefinitely because the condition is always `True`.
  - The loop will run until it encounters a `break` statement or a `return` statement that exits the function.

### When to Use `while True` vs. `while <condition>`

#### When to Use `while True`:
    - Where you have multiple exit points or complex conditions, 
    - such as searching for an insertion point in a data structure.
    **USE**:
        - when the loop execution madatory untill u satisify the condtion(inserting node in Tree)
  
#### When to Use `while <condition>`:
    - Best when you have a clear stopping condition(i.e., when `temp` becomes `None`), 
    - like traversing a list or tree, where you know the loop should terminate based on the structure being iterated over.
    - this is straight forward beacuse no need of True here. loop stops if it founds Value in any iteraiton.

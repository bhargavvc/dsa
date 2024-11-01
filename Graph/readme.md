
# Handling Runtime Errors in Mutable Collections

## Overview

When modifying mutable collections such as lists and dictionaries while iterating over them, you may encounter `RuntimeError`. This occurs because the structure of the collection changes during iteration, which can lead to unexpected behavior.

## Example: Modifying a List While Iterating

Here's an example demonstrating a `RuntimeError` when attempting to remove elements from a list:

```python
my_list = [1, 2, 3, 4, 5]

try:
    for item in my_list:
        if item % 2 == 0:  # If the item is even
            my_list.remove(item)  # Attempting to remove the item
except RuntimeError as e:
    print(f"RuntimeError: {e}")  # This may not be triggered directly
finally:
    print("Final list:", my_list)
```

### Output
```
Final list: [1, 3, 5]
```

### Solution
To avoid this issue, create a separate copy of the collection you are iterating over:

```python
for item in my_list[:]:  # Using a slice to create a copy of the list
    if item % 2 == 0:
        my_list.remove(item)
```

## Example: Modifying a Dictionary While Iterating

Here's an example that demonstrates modifying a dictionary while iterating over it:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    for key in my_dict:
        if my_dict[key] % 2 == 0:  # If the value is even
            del my_dict[key]  # Attempting to remove the key
except RuntimeError as e:
    print(f"RuntimeError: {e}")  # This will raise an error in Python 3
finally:
    print("Final dictionary:", my_dict)
```

### Output
```
Final dictionary: {'a': 1, 'b': 2, 'c': 3}
```

### Collect Keys First
For dictionaries, collect the keys you want to modify in a separate list first:

```python
keys_to_remove = [key for key in my_dict if my_dict[key] % 2 == 0]
for key in keys_to_remove:
    del my_dict[key]
```

## Conclusion
By following these best practices—using copies of collections when iterating or collecting keys first for dictionaries—you can avoid `RuntimeError` and ensure your code behaves as expected.
```

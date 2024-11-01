
- Left and right product arrays

```python
def product_array_elements_except_self(nums):
    length = len(nums)
    output = [1] * length
    prefix = 1 
    for i in range(length):  
        # Prefix value is the product of all elements before the current index
        output[i] = prefix  
        prefix *= nums[i]  

    suffix = 1
    for i in range(length - 1, -1, -1):  
        # Multiply the suffix with the value at output index and update the suffix for the next iteration
        output[i] *= suffix 
        suffix *= nums[i]  
    
    return output 

# Example usage:
array = [1, 2, 3]
output = product_array_elements_except_self(array) 
print(output)  # Output: [6, 3, 2] 
```
## Time and Space Complexity

### Time Complexity

- **O(n)**: The function makes two separate passes through the array, each in linear time. Thus, the total time complexity remains linear relative to the size of the input array.

### Space Complexity

- **O(n)**: Space is used for the `output` array which stores the results. The additional space used for the `prefix` and `suffix` variables is constant, O(1), but the overall space complexity is O(n) due to the output array.


```plaintext

#my analogy 

#product of array elements except self requires both passes 
----->
<-----

#doing fwd pass
[1, 2, 3]

This array now tells us that:
At index 0, the product of all numbers to the left is 1.
At index 1, it’s also 1.
At index 2, it’s 2.

1,2,3
1 --> 2*3
2 --> 1*3
3 --> 2*1

forward pass product  [ 1, 1, 2]

suffix producs (backwardpass)
index 2 -> 3 ==> 1*2
index 1 -> 2 ==> 1*3
index 0 -> 1 ==> 3*2

suffix pass product [ 6, 3, 1]
final output --> [6,3, 2]

#brute force approach 
for inedx, ele in enumerate(prefix):
     output.append(ele of prefix * suffxi(index))

but this approach already optimised in suffix for loop at a time
    
```


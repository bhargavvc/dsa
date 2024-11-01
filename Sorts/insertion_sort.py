def insertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]  # Taking the current value to be inserted
        j = i - 1  # Start comparing with the previous element
        
        # Shift elements of the sorted segment to the right
        while j >= 0 and array[j] > temp:  # Correct order check
            array[j + 1] = array[j]  # Shift the larger element to the right
            j -= 1
        
        # Place temp(min sort value) in its correct position
        array[j + 1] = temp

    print(array)

array = [3, 1, 4, 2]
insertionSort(array)

# 
'''
[1,3,4,2]
[1,3,2,4]
[1,2,3,4]
 how while should interchange the value 

'''

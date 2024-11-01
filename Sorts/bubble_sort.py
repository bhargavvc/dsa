

#how its internally working

def bubble_sort_list(array):
    '''
     

    loop has to run n-1 comparison 
    for first time if length is 4 it would take 3 comparison
    for first time if length is 3 it would take 2 comparison
    for first time if length is 2 it would take 1 comparison
    '''

    '''
    that for loop logic should run len array - 1 times
    '''

    for ele in range(len(array)-1):
        if array[ele] > array[ele+1]:
            array[ele], array[ele+1] = array[ele+1], array[ele]
    
    for ele in range(len(array)-1):
        if array[ele] > array[ele+1]:
            array[ele], array[ele+1] = array[ele+1], array[ele]
    
    for ele in range(len(array)-1):
        if array[ele] > array[ele+1]:
            array[ele], array[ele+1] = array[ele+1], array[ele]
     

def bubble_sort(array):
    n = len(array)

    # Loop for n passes
    for i in range(n):
        swapped = False 

        # Inner Loop: The inner loop runs up to n - 1 - i 
        #  The largest unsorted element "bubbles" up to its correct position in each pass.
        for j in range(n-1-i):#range(n - 1 - i): #range(i, n-1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
            
        if not swapped:
            print(array)
            break


    

# array = [1, 2, 3, 4, 5, 7] #[1, 5, 2, 4, 3, 7]
array =[1, 5, 2, 4, 3, 7]

# Example usage
bubble_sort(array)

#Bonus
'''
Revered Sorted Order
array[j] < array[j+1]

The swapped flag is a clever optimization in the bubble sort algorithm 
that can significantly reduce unnecessary iterations, 
especially when the array is already sorted or nearly sorted
'''
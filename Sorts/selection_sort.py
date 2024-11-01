

def ssort(array):
    
    n = len(array)
    for i in range(n): # range(n-1)   ==> 0,1,2,3,4 vs 0,1,2,3
        min_index = i 
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        if i != min_index:
            array[min_index], array[i] = array[i],array[min_index]

    print(array)
            


array = [1,4,3,2]
ssort(array)

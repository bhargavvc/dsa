


# def find_max_num(array, n):

#     if n==1:
#         return array[0]
#     return max(array[n-1], find_max_num(array, n-1))

# array = [1,3,4,2,5,8]
# n= len(array)
# print(find_max_num(array, n))


"""
   Here  main thing comparing the first value with all the values using max fucntion
   that function we ran till it reaches first index
"""
'''
 Appraoch here is find max requores n times loop run so 
 we are doing negative indexing by taking the lenght of array - 1 in each recursive call
 we will do this until it reaches the first element

 if it reaches first element we are doing max comparision between the first element and negitive index elment 
'''
 
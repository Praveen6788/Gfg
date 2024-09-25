
from collections import Counter

# FIND INDEX
# def findIndex (arr, key ):
#         x=Counter(arr)
#         if key not in arr:
#             return [-1,-1]
#         a= arr.index(key)
#         for i in range(0,len(arr)):
#             if arr[i] == key:
#                 x[arr[i]] -=1
#                 if x[arr[i]] == 0:
#                     return [a,i]
                
    
# arr = [6, 5, 4, 3,2] 
# key = 1

# c = findIndex(arr,key)
# print(c)


# MISSING NUMBER
# n=4
# a = list(range(1,n+1))
# print(a)
# b =[1,  4,  3]
# x =set(a) - set(b)
# print(x)



# first repeting Number
def firstRepeated( arr):
    x = Counter(arr)  # Count occurrences of each element
    min_index = float("inf")  # Set initial min_index to a large value
    
    for i in range(len(arr)):
        if x[arr[i]] >= 2:  # Check if the element is repeated
            min_index = min(i, min_index)
    return min_index+1 if min_index != float("inf") else -1
             
arr = [1,2,3,4]
a =firstRepeated(arr)
print(a)
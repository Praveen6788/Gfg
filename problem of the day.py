# Palindrome Linked List

def isPalindrome(self, head):
        res =[]
        temp = head
        while temp:
            res.append(temp.data)
            temp = temp.next
        if res == res[::-1]:
            return True
        return False



# Roof Top

# Difficulty: Easy
# You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the next adjacent building. You need to find the maximum number of consecutive steps you can put forward such that you gain an increase in altitude with each step.



def max_step(arr):
    max_count = 0
    count = 0
    for i in range(len(arr)-1):
        if arr[i] <arr[i+1]:
            count +=1
            max_count = max(max_count,count)
        else:
            count = 0
    return max_count

a = max_step([20, 6 ,5, 10, 7 ,17, 19, 4, 17, 2, 18, 12, 16, 11])
# print(a)







# K Sized Subarray Maximum

# Difficulty: Medium
# Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.










def max_of_subarrays(k,arr):
        n = len(arr)
        output = []
        maxele = max(arr[:k]) 
        output.append(maxele)
        
        for i in range(1, n - k + 1):
            if arr[i - 1] == maxele:
               
                maxele = max(arr[i:i + k])
            else:
                maxele = max(maxele, arr[i + k - 1])
            output.append(maxele)
        
        return output 
ab= max_of_subarrays(3,[1, 2, 3, 1, 4, 5, 2, 3, 6])
# print(ab)









def minimizeCost(k, arr):
    n = len(arr)
    mincost = float('inf')

    dp = [float('inf')] * n
    dp[0] = 0  
    for i in range(n):
        for j in range(1, k + 1):  
            if i + j < n:  
                cost = dp[i] + abs(arr[i] - arr[i + j])
                dp[i + j] = min(dp[i + j], cost)  
    
   
    return dp[-1]

k = 2
arr = [35, 1, 70, 25, 79, 59, 63, 65]
mincost = minimizeCost(k, arr)
# print("mincost", mincost)












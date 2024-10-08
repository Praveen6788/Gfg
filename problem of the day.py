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






# Total Count
def totalCount (k, arr):
    total_count = 0

    for num in arr:
        
        parts = (num + k - 1) // k
        print(num+k-1) 
        
        print(parts)
        total_count += parts
    
    return total_count

k = 3
arr = [5, 8, 10, 13]
# print(totalCount(k,arr))



# Multiply two linked lists
# Difficulty: Easy
# Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.


def multiply_two_lists(self, first, second):
    MOD = 1000000007 

    num1 = 0
    while first:
        num1 = (num1 * 10 + first.data) % MOD
        first = first.next


    num2 = 0
    while second:
        num2 = (num2 * 10 + second.data) % MOD
        second = second.next


    return(num1 * num2) % MOD


def findMajority(self, nums):
    
        if not nums:
            return [-1]
        
        # Step 1: Find potential candidates using Boyer-Moore Voting Algorithm
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Validate the candidates by counting their actual occurrences
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 3: Collect results that appear more than n//3 times
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        
        if not result:
            return [-1]
        return sorted(result)
    


def findSmallest(self, arr):
        res = 1

    # Traverse the array and increment the result if the current element
    # is less than or equal to the result
        for i in range(len(arr)):
            # If arr[i] is greater than res, then we cannot form 'res' as a sum
            if arr[i] > res:
                break
            res += arr[i]
    
        return res
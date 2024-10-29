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
    
    
    
# Find the Sum of Last N nodes of the Linked List


def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        temp =head
        sum1=0
        # for i in range(1,n+1):
        #     sum1+=temp.data
        #     temp =temp.next
        # return sum1
        array=[]
        while temp:
            array.append(temp.data)
            temp= temp.next
        array.reverse()
        return sum(array[:n])


# Remove dupilicates in array
def removeDuplicates(self, arr):
        s =[]
        for i in arr:
            if i in s:
                continue
            else:
                s.append(i)
        return s
    
    
# Quick Sort on Linked List
# Difficulty: Medium
# You are given a Linked List. Sort the given Linked List using quicksort. 

# Examples:

# Input: Linked list: 1->6->2
# Output: 1->2->6

def quickSort(head):
    if head is None or head.next is None:
        return head

    # Partition the list around the pivot (first element)
    pivot = head.data
    less_head = less_tail = None
    greater_head = greater_tail = None
    current = head.next

    while current:
        if current.data < pivot:
            if less_head is None:
                less_head = less_tail = current
            else:
                less_tail.next = current
                less_tail = less_tail.next
        else:
            if greater_head is None:
                greater_head = greater_tail = current
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
        current = current.next


    if less_tail:
        less_tail.next = None
    if greater_tail:
        greater_tail.next = None

    less_sorted = quickSort(less_head)
    greater_sorted = quickSort(greater_head)

   
    if less_sorted:
        
        temp = less_sorted
        while temp.next:
            temp = temp.next
        temp.next = head  
    else:
        less_sorted = head

    head.next = greater_sorted  

    return less_sorted
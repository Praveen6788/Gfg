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
print(a)
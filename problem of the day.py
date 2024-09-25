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
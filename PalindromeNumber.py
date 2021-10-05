# URL : https://leetcode.com/problems/palindrome-number/submissions/
class Solution:

    # Optimized
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10 ==0 and x!=0): return False
        rev=0
        while x>rev:
            rev = rev*10 + x%10
            x //= 10
        return x==rev or x==rev//10
       
    def isPalindrome(self, x: int) -> bool:
        rev=0
        while x!=0:
            rev = rev*10 + x%10
            x //= 10
        return x==rev x=str(x)
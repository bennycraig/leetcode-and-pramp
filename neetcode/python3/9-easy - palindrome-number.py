#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
""" 
PALINDROME NUMBER
GIVEN: integer x

RETURN: True/False if number is palindrome

EXAMPLE:
121
l r

BRUTE FORCE:
1. Convert to string
2. Treat as string palindrome problem
    1. Use pointers to left and right side
    2. while (l <= r), the left value should equal the right value

    Even-length: 
    Odd-length:

FOLLOW UP (NO STRING CASTING):


"""

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Convert to string
        str_x = str(x) #! What's the best way to convert between data types in Python?

        # Create pointers to beginning and end
        l = 0
        r = len(str_x) - 1

        while (l <= r):
            print("str_x[l]: ", str_x[l])
            print("str_x[r]: ", str_x[r])
            if str_x[l] != str_x[r]:
                return False
            l += 1
            r -= 1
        
        return True
        
# @lc code=end


# palindrome is a number that reads the same on both sides ie. 121 that when flipped reads 121

# version 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # we are given the number x that is an int and we need to return a bool
        # we are going to slice in reverse and check

        x = str(x)
        reverse = x[::-1]

        return (reverse == x)
    
test = Solution()
print(test.isPalindrome(1023456))

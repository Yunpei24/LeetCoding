"""
* leetcode.py Contains the solution to LeetCode problems.
"""

class LeetCode:
    """
    A class to represent a solution to LeetCode problems.
    """

    def isPalindrome(self, x: int) -> bool:
        """Check if a number is palindrome or not.
        Examples:
            121 is palindrome: is the same when we read from right to left and vice versa
            321 is not palindrome
        
        Args:
            x: The number that we want to check if it is palindrome or not
        
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0 # Initialize the reversed half that will help us to check if the number is palindrome
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10 # Add the last digit of x to the reversed half
            x = x // 10 # Remove the last digit of x
        return x == reversed_half or x == reversed_half // 10

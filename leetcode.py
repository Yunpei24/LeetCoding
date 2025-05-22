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
        x_copy = x # Copy the number that will be using to check
        r = 0 # Follow the rest of the division by 10

        while x_copy > 0:
            modulo10_rest = x_copy % 10 # The rest of the division by 10
            r = 10 * r + modulo10_rest
            x_copy = x_copy // 10 # the result of integer division by 10

        if r == x:
            print(x, "is palindrome")
        else:
            print(x, "is not palindrome")

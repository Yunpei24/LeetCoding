"""
* leetcode.py Contains the solution to LeetCode problems.
"""

from typing import List

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
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find two numbers in the list that add up to the target number.
        Examples:
            nums = [2, 7, 11, 15], target = 9
            The two numbers that add up to 9 are at indices: [0, 1]
            nums = [3, 2, 4], target = 6
            The two numbers that add up to 6 are at indices: [1, 2]
        
        Args:
            nums: The list of numbers that we want to check if there are two numbers that add up to the target number
            target: The target number that we want to check if there are two numbers that add up to it
        
        Returns:
            A list of two indices of the numbers that add up to the target number
        """
        n = len(nums)
        if n == 0: # Be sure the list of numbers is not empty
            return False
        
        for i in range(n): # browse list of numbers
            k = n - 1 - i # The index to do the reverse parcours of the list of numbers
            for j in range(i + 1, n): # browse the list of numbers after the index i
                l = n - 1 - j # browse the reverse parcours of j
                if nums[i] + nums[j] == target:
                    return [i, j]
                if nums[k] + nums[l] == target:
                    return [l, k]
                
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """"Find the median of two sorted arrays.
        Examples:
            nums1 = [1, 3], nums2 = [2]
            The median is 2.0
            nums1 = [1, 2], nums2 = [3, 4]
            The median is (2 + 3) / 2 = 2.5
        Args:
            nums1: The first sorted array
            nums2: The second sorted array
        Returns:
            The median of the two sorted arrays (float)
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 and n2 == 0: return "First and second List are empty"

        nums1.extend(nums2) # Merge the two sorted arrays
        nums1.sort() # Be sure the list of numbers is sorted
        idx = len(nums1)//2 # The index of the median

        if len(nums1) % 2 != 0: # If the length of the list of numbers is odd
            return nums1[idx]
        else:
            return (nums1[idx -1] + nums1[idx]) / 2
        
    def isHappy(self, n: int) -> bool:
        """Check if a number is a happy number.
        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits,
        and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
        Examples:
            19 is a happy number: 1^2 + 9^2 = 82,
                                  8^2 + 2^2 = 68,
                                  6^2 + 8^2 = 100,
                                  1^2 + 0^2 + 0^2 = 1
            2 is not a happy number: 2^2 = 4,
                                     4^2 = 16,
                                     1^2 + 6^2 = 37,
                                     3^2 + 7^2 = 58,
                                     5^2 + 8^2 = 89,
                                     8^2 + 9^2 = 145,
                                     1^2 + 4^2 + 5^2 = 42,
                                     4^2 + 2^2 = 20,
                                     2^2 + 0^2 = 4 (cycle)
        Args:
            n: The number that we want to check if it is a happy number or not
        Returns:
            True if the number is a happy number, False otherwise
    """
        if n < 0 : # Be sure the number is not negative
            return False
        if n == 1:
            return True 
        check = [] # List to check if we have already seen the number
        while n != 1:
            digits = [int(i) for i in str(n)] # Convert the number to a list of digits
            n = sum(map(lambda x: x ** 2, digits)) # Sum the square of the digits
            # Check if the number is already in the list or if the number is greater than 2^31 - 1
            if (n in check) or n >= (2 ** 31 - 1):
                return False
            check.append(n)
        return True
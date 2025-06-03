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
        
        Args:
            nums: The list of numbers that we want to check if there are two numbers that add up to the target number
            target: The target number that we want to check if there are two numbers that add up to it
        
        Returns:
            A list of two indices of the numbers that add up to the target number
        """
        n = len(nums)
        if n == 0: # Be sure the list of numbers is not empty
            return False
        
        for i in range(n):
            k = n - 1 - i # The index to do the reverse parcours of the list of numbers
            for j in range(i + 1, n): # browse the list of numbers after the index i
                l = n - 1 - j # browse the reverse parcours of j
                if nums[i] + nums[j] == target:
                    return [i, j]
                if nums[k] + nums[l] == target:
                    return [l, k]
                
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """"Find the median of two sorted arrays.
        Args:
            nums1: The first sorted array
            nums2: The second sorted array
        Returns:
            The median of the two sorted arrays (float)
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 and n2 == 0: return "First and second List are empty"

        nums1.extend(nums2) 
        nums1.sort()
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
        
        Args:
            n: The number that we want to check if it is a happy number or not
        Returns:
            True if the number is a happy number, False otherwise
    """
        if n < 0 : 
            return False
        if n == 1:
            return True 
        check = [] # List to check if we have already seen the number
        while n != 1:
            digits = [int(i) for i in str(n)]
            n = sum(map(lambda x: x ** 2, digits)) # Sum the square of the digits
            if (n in check) or n >= (2 ** 31 - 1):
                return False
            check.append(n)
        return True
    
    def romanToInt(self, s: str) -> int:
        """Convert a Roman numeral to an integer.
        Args:
            s: The Roman numeral that we want to convert to an integer
        Returns:
            The integer value of the Roman numeral
        """
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0 # this variable will hold the total value of the Roman numeral
        prev_value = 0 # this variable will hold the value of the previous character
        
        for char in reversed(s): 
            value = roman_to_int_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
    
    def strStr(self, haystack: str, needle: str) -> int:
        """Find the index of the first occurrence of needle in haystack.
        
        Args:
            haystack: The string in which we want to find the needle
            needle: The string that we want to find in the haystack
        Returns:
            The index of the first occurrence of needle in haystack, or -1 if needle is not found
        """
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Find the longest common prefix string amongst an array of strings.
        
        Args:
            strs: The array of strings that we want to find the longest common prefix
        Returns:
            The longest common prefix string amongst the input strings
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
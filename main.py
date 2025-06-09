from leetcode import LeetCode

if __name__ == "__main__":
    leet_obj = LeetCode()

    # Problem of Palindrome number Testing
    n1 = 12121
    print(n1, "is palindrome?: ",leet_obj.isPalindrome(n1))

    n2 = 321
    print(n2, "is palindrome?: ",leet_obj.isPalindrome(n2))

    # Problem of Two Sum Testing
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("The two numbers that add up to", target1, "are at indices:", leet_obj.twoSum(nums1, target1))

    nums2 = [3, 2, 4]
    target2 = 6
    print("The two numbers that add up to", target2, "are at indices:", leet_obj.twoSum(nums2, target2))

    nums3 = [3, 3]
    target3 = 6
    print("The two numbers that add up to", target3, "are at indices:", leet_obj.twoSum(nums3, target3))
    
    nums4 = [3, 2, 3]
    target4 = 6
    print("The two numbers that add up to", target4, "are at indices:", leet_obj.twoSum(nums4, target4))

    # Problem of Median of Two Sorted Arrays Testing
    nums5 = [1, 3]
    nums6 = [2]
    print("The median of the two sorted arrays is:", leet_obj.findMedianSortedArrays(nums5, nums6))
    nums7 = [1, 2]
    nums8 = [3, 4]
    print("The median of the two sorted arrays is:", leet_obj.findMedianSortedArrays(nums7, nums8))
    nums9 = []
    nums10 = [1]
    print("The median of the two sorted arrays is:", leet_obj.findMedianSortedArrays(nums9, nums10))

    # Problem of Happy Number Testing
    n3 = 19
    print(n3, "is happy number?: ", leet_obj.isHappy(n3)) # Output should be True
    n4 = 2
    print(n4, "is happy number?: ", leet_obj.isHappy(n4)) # Output should be False
    n5 = 7
    print(n5, "is happy number?: ", leet_obj.isHappy(n5)) # Output should be True
    n6 = 4
    print(n6, "is happy number?: ", leet_obj.isHappy(n6)) # Output should be False
    n7 = 1
    print(n7, "is happy number?: ", leet_obj.isHappy(n7)) # Output should be True

    # Problem of romanToInt Testing
    roman1 = "III"
    print(f"The integer value of the roman numeral '{roman1}' is: {leet_obj.romanToInt(roman1)}")  # Output should be 3
    roman2 = "IV"
    print(f"The integer value of the roman numeral '{roman2}' is: {leet_obj.romanToInt(roman2)}")  # Output should be 4
    roman3 = "IX"
    print(f"The integer value of the roman numeral '{roman3}' is: {leet_obj.romanToInt(roman3)}")  # Output should be 9
    roman4 = "LVIII"
    print(f"The integer value of the roman numeral '{roman4}' is: {leet_obj.romanToInt(roman4)}")  # Output should be 58
    roman5 = "MCMXCIV"
    print(f"The integer value of the roman numeral '{roman5}' is: {leet_obj.romanToInt(roman5)}")  # Output should be 1994

    # Find the index of the first occurrence of needle in haystack
    haystack1 = "sadbutsad"
    needle1 = "sad"
    print(f"The index of the first occurrence of '{needle1}' in '{haystack1}' is: {leet_obj.strStr(haystack1, needle1)}")  # Output should be 0
    haystack2 = "leetcode"
    needle2 = "leeto"
    print(f"The index of the first occurrence of '{needle2}' in '{haystack2}' is: {leet_obj.strStr(haystack2, needle2)}")  # Output should be -1

    # Problem of Longest Common Prefix Testing
    strs1 = ["flower", "flow", "flight"]
    print(f"The longest common prefix of {strs1} is: '{leet_obj.longestCommonPrefix(strs1)}'")  # Output should be "fl"
    strs2 = ["dog", "racecar", "car"]
    print(f"The longest common prefix of {strs2} is: '{leet_obj.longestCommonPrefix(strs2)}'")  # Output should be ""
    strs3 = ["a"]
    print(f"The longest common prefix of {strs3} is: '{leet_obj.longestCommonPrefix(strs3)}'")  # Output should be "a"
    strs4 = ["", "b"]
    print(f"The longest common prefix of {strs4} is: '{leet_obj.longestCommonPrefix(strs4)}'")  # Output should be ""
    strs5 = ["c", "c"]
    print(f"The longest common prefix of {strs5} is: '{leet_obj.longestCommonPrefix(strs5)}'")  # Output should be "c"
    strs6 = ["ab", "a"]
    print(f"The longest common prefix of {strs6} is: '{leet_obj.longestCommonPrefix(strs6)}'")  # Output should be "a"

    # Problem of Valid Parentheses Testing
    s1 = "()"
    print(f"The string '{s1}' has valid parentheses?: {leet_obj.isValid(s1)}")  # Output should be True
    s2 = "()[]{}"
    print(f"The string '{s2}' has valid parentheses?: {leet_obj.isValid(s2)}")  # Output should be True
    s3 = "(]"
    print(f"The string '{s3}' has valid parentheses?: {leet_obj.isValid(s3)}")  # Output should be False
    s4 = "([)]"
    print(f"The string '{s4}' has valid parentheses?: {leet_obj.isValid(s4)}")  # Output should be False
    s5 = "{[]}"
    print(f"The string '{s5}' has valid parentheses?: {leet_obj.isValid(s5)}")  # Output should be True

    # Problem of length of Last Word Testing
    s6 = "Hello World"
    print(f"The length of the last word in '{s6}' is: {leet_obj.lengthOfLastWord(s6)}")  # Output should be 5
    s7 = "   fly me   to   the moon  "
    print(f"The length of the last word in '{s7}' is: {leet_obj.lengthOfLastWord(s7)}")  # Output should be 4
    s8 = "Joshua is an engineer"
    print(f"The length of the last word in '{s8}' is: {leet_obj.lengthOfLastWord(s8)}")  # Output should be 8

    # Prblem of my sqrt Testing
    x1 = 4
    print(f"The square root of {x1} is: {leet_obj.mysqrt(x1)}")  # Output should be 2
    x2 = 8
    print(f"The square root of {x2} is: {leet_obj.mysqrt(x2)}")  # Output should be 2
    x3 = 0
    print(f"The square root of {x3} is: {leet_obj.mysqrt(x3)}")  # Output should be 0
    x4 = 1
    print(f"The square root of {x4} is: {leet_obj.mysqrt(x4)}")
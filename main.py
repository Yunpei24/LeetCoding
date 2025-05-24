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
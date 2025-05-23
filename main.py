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
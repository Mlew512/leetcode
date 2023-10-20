# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

def maxSubArray(nums):
    max_so_far = nums[0]
    max_ends = nums[0]
    for i in range(1,len(nums)):
        max_ends = max(max_ends + nums[i],nums[i])
        max_so_far = max(max_so_far, max_ends)

    return max_so_far


maxSubArray([5,4,-1,7,8]) #==23
maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) # == 6
maxSubArray([1]) # == 0
def maxSubArray(nums) -> int:
    max_sum = nums[0]
    cur_sum = nums[0]

    for i in range(1, len(nums)):
        numi = nums[i]
        
        cur_sum = max(cur_sum + numi, numi)
        max_sum = max(cur_sum, max_sum)

    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
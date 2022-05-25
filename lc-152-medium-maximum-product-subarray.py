import re


def maxProduct(nums) -> int:
    min_val = nums[0]
    max_val = nums[0]
    max_prod = nums[0]

    for i in range(1, len(nums)):
        numi = nums[i]
        if numi < 0:
            max_val, min_val = min_val, max_val     # based on multiplication by negative value need to sweep values 

        max_val = max(max_val*numi, numi)
        min_val = min(min_val*numi, numi)

        max_prod = max(max_prod, max_val)

    return max_prod


print(maxProduct([6, -3, -10, 0, 2]))
print(maxProduct([-1, -3, -10, 0, 60]))
print(maxProduct([-2, -3, 0, -2, -40]))
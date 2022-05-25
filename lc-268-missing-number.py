
def missingNumber(nums) -> int:
    summ_current = 0
    for i in nums:
        summ_current += i

    quantity_elements = len(nums)


    return (quantity_elements + 1) * quantity_elements // 2 - summ_current
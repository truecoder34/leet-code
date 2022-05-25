class NumArray:

    def __init__(self, nums):
        sums = []
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            sums.append(cur_sum)

        self.sums = sums
        #print(sums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]


obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 2)
param_2 = obj.sumRange(2, 5)
param_3 = obj.sumRange(0, 5)

print(param_1)
print(param_2)
print(param_3)
class NumArray:

    def __init__(self, nums):
        sums = []
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            sums.append(cur_sum)

        self.sums = sums
        self.nums = nums
        print("init nums : ", self.nums)
        print("init sums : ", self.sums)

    def update(self, index: int, val: int) -> None:
        dif = val - self.nums[index]
        self.nums[index] = val      # update value in nums by index

        for i in range(index, len(self.nums)):
            print(f"{i} , change {self.sums[i]} to {self.sums[i] + dif} ")
            self.sums[i] += dif

        print("upd sums: ", self.sums)

    def sumRange(self, left: int, right: int) -> int:
        # if len(self.sums) == 1:
        #     return self.nums[0]
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]

# TEST 4
obj = NumArray([9, -8])
obj.update(0,3)
param_1 = obj.sumRange(1, 1)
param_2 = obj.sumRange(0, 1)
obj.update(1,-3)
param_3 = obj.sumRange(0, 1)

print(param_1)
print(param_2)
print(param_3)

# obj = NumArray([-2, 0, 3, -5, 2, -1])
# param_1 = obj.sumRange(0, 2)

# param_2 = obj.sumRange(2, 5)
# param_3 = obj.sumRange(0, 5)

# print(param_1)
# print(param_2)
# print(param_3)

# TEST 1
# obj = NumArray([1, 3, 5])
# param_2 = obj.sumRange(0, 2)
# obj.update(1,2)
# param_3 = obj.sumRange(0, 2)

# print(param_2)
# print(param_3)

#TEST 2
# obj = NumArray([-1])
# param_2 = obj.sumRange(0, 0)
# obj.update(0,1)
# param_3 = obj.sumRange(0, 0)

# print(param_2)
# print(param_3)




'''
All/Most of the segement tree operations are in post order traversal.

https://leetcode.com/problems/range-sum-query-mutable/discuss/1965061/Python-Best-Segment-Tree-Implementation-with-Detailed-Comments
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)
        
    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.sumRange(left,right)

class SegmentTree:
    
    def __init__(self,nums):
        self.root = self.createTree(nums)
        
    # Create tree for range [i,j] from array nums
    def createTree(self,nums):
        def helper(i,j):
            # Base case
            if i > j: 
                return None
            
            # Base case - Create leaf node
            if i == j: 
                return Node(i,j,nums[i])
            
            # Find mid index and recursively create left and right children
            mid = (i+j)//2
            left = helper(i,mid)
            right = helper(mid+1,j)
            
            # Create and return the current node based on left and right children
            return Node(i,j,left.val + right.val,left,right)
        
        return helper(0,len(nums)-1)
        
    def update(self,index,val):
        def helper(node):
            # Base case - found leaf node
            if node.start == node.end == index:
                node.val = val # Update the value of the leaf node
                return 
            
            # Find mid index and recursively update values of left or right children
            mid = (node.start+node.end)//2
            if index <= mid:
                helper(node.left)
            else:
                helper(node.right)
        
            # Update value of the current node
            node.val = node.left.val + node.right.val
        
        return helper(self.root)
        
    def sumRange(self,left,right):
        def helper(node):
            # Base case current interval falls fully inside query interal [left,right]
            if node.start >= left and node.end <= right:
                return node.val
            
            # Find mid index and recursively find sumRange
            mid = (node.start+node.end)//2
            
            # If query is only on left side
            if right <= mid:
                return helper(node.left)
            # If query is only on right side
            elif left > mid:
                return helper(node.right)
            # Else go on both sides
            else:
                return helper(node.left) + helper(node.right)
        return helper(self.root)

class Node:
    def __init__(self,s,e,t,l=None,r=None):
        self.start = s
        self.end = e
        self.val = t
        self.left = l
        self.right = r

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




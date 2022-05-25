
from ast import List

'''
    XOR for same numbers will give 0000
    0101
        xor
    0101
    ------
    0000


'''


def singleNumber(nums) -> int:
    valBase = toBinary(nums[0])
    for val2 in nums[1:]:

        valBase = xor(valBase, toBinary(val2))
    # print(valBase)
    # print(toDecimal(valBase))
    val = self.toDecimal(valBase)
    if nums.count(val) == 1:
        return val
    else:
        return val * (-1)


def toDecimal(number: str):
    res=0
    exp=len(number)-1
    for i in range(len(number)):
        res += int(number[i]) * pow(2,exp)
        exp-=1
    return res

def toBinary(val: int) -> str:
    if val < 0:
        val = val * (-1)
    resBinList=[]
    res=val
    
    if res == 0:
        return "0"
    while res > 0:
        rem=res%2
        res=res//2
        
        resBinList.append(rem)
    resBinList.reverse()
    resBin = "".join(map(str, resBinList))
    return resBin

def xor(val1: str, val2:str):
    if len(val1) > len(val2):
        diff = len(val1) - len(val2)
        val2 = "0"*diff+val2
    elif len(val2) > len(val1):
        diff = len(val2) - len(val1)
        val1 = "0"*diff+val1
    res = [(ord(a) ^ ord(b)) for a,b in zip(val1, val2)]
    return "".join(map(str, res))




def toBinaryTest():
    print(toBinary(11))
    print(toBinary(0))
    print(toBinary(1))

    testData = [
        [11, "1011"],
        [0, "0"],
        [1, "1"],
        [3, "11"],
        [5000, "1001110001000"],
        [7138, "1101111100010"],
    ]
    for case in testData:
        result = toBinary(case[0])
        print(f"Compare {result} and {case[1]} ")
        assert result == case[1], f"Wrong answer! {result} != {case[1]}"


singleNumber([4,1,2,1,2])
singleNumber([2,2,1])


"""
FAST SOLUTION

mask = 0
for num in nums:
    mask ^= num

return mask


"""

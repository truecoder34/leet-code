
class Solution:
    # extra space solution
    def compress(self, chars) -> int:
        result = ''
        length_of_str = len(chars)

        if length_of_str == 0:
            return 0
        if length_of_str == 1:
            print(1)
            return 0

        last = chars[0]
        cntr = 1
        i = 1
        while i < length_of_str:
            if chars[i] == chars[i - 1]:
                cntr += 1
            else:
                result = result + chars[i - 1] + str(cntr)
                cntr = 1
            i += 1
        result = result + chars[i - 1] + str(cntr)
        print(len(result))
        return 0

    # in place colution
    def compress_in_place(self, chars) -> int:
        result, cnt = 0, 1
        j = 0
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                cnt += 1
            else:
                # 1) update letter
                chars[j] = chars[i - 1]
                j += 1
                # 2) update cnt
                if cnt == 1:
                    continue
                for ch in str(cnt):
                    chars[j] = ch
                    j += 1
                # 3) reset cnt
                cnt = 1
        return j



sl = Solution()
sl.compress("aabbccc")
#sl.compress_in_place("aabbccc")
sl.compress("a")
sl.compress("abbbbbbbbbbbb")

# Ex. 1
# INPUT : ["a", "a", "b", "b", "c", "c", "c"]
# OUTPUT : 6
# a2b2c3

# Ex. 2
# INPUT : ["a"]
# OUTPUT : 1
# a

# Ex. 3
# INPUT : ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# OUTPUT : 4
# ab12


##################################################
###### COMMON SOLUTION
###### RETURN LINE, NOT LENGTH
###### WORKS NOT IN PLACE
##################################################

def string_compressor(line: str):
    if len(line) == 1:
        return line
    if len(line) <= 0:
        return 0

    itter = 1
    result = ''
    cntr = 1
    while itter < len(line):
        if line[itter] == line[itter - 1]:
            cntr += 1
        else:
            if cntr == 1:
                # double check to prevent cases like : aabcdd --> a2bcd2 - CORRECT; aabcdd --> a2b1c1d2 - WRONG
                result = result + line[itter - 1]
            else:
                result = result + line[itter-1] + str(cntr)
            cntr = 1

        itter += 1

    # Finalazing last entery
    if cntr == 1:
        # double check AGAIN to prevent cases like : aabcdd --> a2bcd2 - CORRECT; aabcdd --> a2b1c1d2 - WRONG
        result = result + line[itter - 1]
    else:
        result = result + line[itter - 1] + str(cntr)

    return result


print(string_compressor("aaabbbcccd"))
print(string_compressor("a"))
print(string_compressor("bbbbbbbbbbbacfffff"))

# #
# TESTING
# #
tests = [["aaabbbcccd", "a3b3c3d"],
         ["a", "a"],
         ["bbbbbbbbbbbacfffff", "b11acf5"],
         ["abcd", "abcd"],
         ["", 0], ]

for test in tests:
    data = test[0]
    answer = test[1]
    assert string_compressor(data) == answer, "STRING COMPRESSION is WRONG"

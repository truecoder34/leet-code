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

def catalan(n):
    c = [0] * (n + 1)
    c[0] = 1
    for k in range(1, n + 1):
        c[k] = sum(c[i] * c[k - i - 1] for i in range(k))
    return c[n]


tests = [[0, 1],
         [1, 1],
         [2, 2],
         [3, 5],
         [4, 14],
         [5, 42],
         [6, 132],
         [7, 429],
         [8, 1430],]

for test in tests:
    data = test[0]
    answer = test[1]
    assert catalan(data) == answer, "CATALAN NUMBER is WRONG"

print("CATALAN from 1", catalan(1))
print("CATALAN from 5", catalan(5))
print("CATALAN from 10", catalan(10))
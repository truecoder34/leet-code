
def climbStairs( n: int) -> int:
    """
        n

        n - 2
        +
        n - 1

        like fibonacci 


        climb steps 1 or 2 
    """
    if n == 1:
        return 1
    n1, n2 = 1, 2
    for i in range(3, n+1):
        n1, n2 = n2, n1 + n2
    return n2

climbStairs(5)
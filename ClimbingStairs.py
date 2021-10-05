class Solution:
    def climbStairs(self, n: int) -> int:
        di={1:1,2:2}
        def climb(n):
            if n not in di:
                di[n]=climb(n-1)+climb(n-2)
            return di[n]
        return climb(n)
    # Optimal
    def climbStairs(self, n: int) -> int:  
        z=[1,1]
        for x in range(2,n+1):
            z.append(z[x-1]+z[x-2])
        return z[n]
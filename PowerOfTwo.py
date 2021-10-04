# URL : https://leetcode.com/problems/power-of-two/
# (n & (n-1) == 0) this is the main condition.
# (n != 0) is the edge case check for 0, 0 cannot be a power of two.

# (n & (n-1) == 0)
# If n is a power of two, then bitwise AND operation(&) of n & (n-1) would be 0.

# Any power of 2 minus 1 are all ones, like 7 (which is 8-1 and in binary 111).

# Example n=8
# 8 is 1000, 7 would be 0111
# 8 & 7 will be 0
# 8 = 1000
# 7 = 0111
# & = 0000
# Since the result is 0, 8 is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return (n&(n-1)==0)

Solution().isPowerOfTwo(8)
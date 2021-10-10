# URL : https://leetcode.com/problems/counting-bits/submissions/
# Ans Ref : https://www.youtube.com/watch?v=awxaRgUB4Kw&ab_channel=TECHDOSE

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for x in range(1,n+1):
            # result.append(result[x//1]+x%2) 
            result.append(result[x>>1]+x%2) # >> shifting is faster than divide by 2
        return result
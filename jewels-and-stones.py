# URL : https://leetcode.com/problems/jewels-and-stones/submissions/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        kvmap={}
        for x in stones:
            if x in kvmap:
                kvmap[x]+=1
            else:
                kvmap[x]=1
        for x in jewels:
            if x in kvmap:
                count += kvmap[x]
        return count
        
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for x in stones:
            if x in jewels:
                count += 1
        return count

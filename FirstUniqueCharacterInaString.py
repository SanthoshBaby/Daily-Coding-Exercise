# URL : https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps={}
        for x in s:
            if x in maps:
                maps[x]+=1
            else:
                maps[x]=1
        for pos,x in enumerate(s):
            if maps[x] == 1:
                return pos
        return -1
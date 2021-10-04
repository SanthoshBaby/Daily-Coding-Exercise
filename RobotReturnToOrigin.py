# URL : https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for z in moves:
            if z=='U':
                y+=1
            elif z=='D':
                y-=1
            elif z=='L':
                x+=1
            elif z=="R":
                x-=1
        return x==0 and y==0
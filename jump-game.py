# URL : https://leetcode.com/problems/jump-game/submissions/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_jump=0
        for index,value in enumerate(nums):
            if maximum_jump<index:
                return False
            maximum_jump=max(maximum_jump,index+value)
        return True
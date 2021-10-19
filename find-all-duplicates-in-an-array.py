# URL : https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for x in range(len(nums)):
            if nums[abs(nums[x])-1]<0:
                res.append(abs(nums[x]))
            nums[abs(nums[x])-1]*=-1
        return res
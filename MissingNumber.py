# Problem URL : https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums)*(len(nums)+1))//2
        for x in nums:
            total-=x
        return total
Solution().missingNumber([0,3,1])
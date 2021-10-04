# URL : https://leetcode.com/problems/single-number/submissions/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary={}
        for x in nums:
            if x in dictionary:
                dictionary[x]+=1
            else:
                dictionary[x]=1
        for key in dictionary:
            if dictionary[key]==1:
                return key

#[4,1,2,1,2]
# 0bres 0bx res x
# 0b0 0b100 0 4
# 0b100 0b1 4 1
# 0b101 0b10 5 2
# 0b111 0b1 7 1
# 0b110 0b10 6 2

    def singleNumberMethod2(self, nums):
        res=0
        for x in nums:
          res^=x
        return res
            
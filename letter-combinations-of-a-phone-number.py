# URL : https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" : return []
        kvmap={
            "1" : "",
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        result_list=[]
        def recur(digits,string):
            if len(digits) == 1:
                for x in kvmap[digits]:
                    result_list.append(string+x)
            else:
                for x in kvmap[digits[0]]:
                    recur(digits[1:],string+x)
        recur(digits,"")
        return result_list

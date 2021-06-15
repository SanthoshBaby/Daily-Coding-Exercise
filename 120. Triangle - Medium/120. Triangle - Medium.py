import pprint

class Solution:
    def minimumTotal(self, triangle):
        minimum = triangle[-1]
        for x in range(len(triangle)-2, -1, -1):
            for y in range(len(triangle[x])):
                minimum[y] = min(minimum[y], minimum[y+1])+triangle[x][y]
        print(minimum[0])

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
Solution().minimumTotal(triangle)

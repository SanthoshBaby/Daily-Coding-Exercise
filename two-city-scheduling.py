# URL : https://leetcode.com/problems/two-city-scheduling/submissions/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: x[0] - x[1])
        mid=len(costs)//2
        total=0
        for x in range(mid):
            total += costs[x][0]+costs[x+mid][1]
        return total
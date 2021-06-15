import pprint

class Solution:
    def generateMatrix(self, n: int):
                
        result=[[None for x in range(n)] for y in range(n)]
        direction={(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
        current_direction=(0,1)
        x_position,y_position=0,0
        currentValue=1

        while currentValue <= n*n:
            print((x_position,y_position))
            result[x_position][y_position]=currentValue
            currentValue+=1
            x=x_position+current_direction[0]
            y=y_position+current_direction[1]
            if x==n:
                x-=1
            elif x==-1:
                x+=1
            elif y==n:
                y-=1
            elif y==-1:
                y+=1
            if result[x][y] is not None:
                current_direction=direction[current_direction]
            x_position+=current_direction[0]
            y_position+=current_direction[1]
        
        pprint.pprint(result)
Solution().generateMatrix(5)
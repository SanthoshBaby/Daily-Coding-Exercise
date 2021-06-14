import pprint

class Solution:
    def generateMatrix(self, n: int):

        def validate(result,x,y):
            try:
                return x>=0 and x<n and y>=0 and y<n and result[x][y] is None
            except:
                return False
                
        result=[[None for x in range(n)] for y in range(n)]
        direction={(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
        current_direction=(0,1)
        x_position,y_position=0,0
        currentValue=1

        while True:
            #Add value and Move forward
            if validate(result,x_position,y_position):
                result[x_position][y_position]=currentValue
                currentValue=currentValue+1
                x_position=x_position+current_direction[0]
                y_position=y_position+current_direction[1]
            #Change Direction
            elif validate(result,x_position+direction[current_direction][0],y_position+direction[current_direction][1]):
                current_direction=direction[current_direction]
                x_position=x_position+direction[current_direction][0]
                y_position=y_position+direction[current_direction][1]
            #Go Reverse and Change Direction
            elif validate(result,x_position+(current_direction[0]*-1)+direction[current_direction][0],y_position+(current_direction[1]*-1)+direction[current_direction][1]):
                x_position=x_position+direction[current_direction][0]+(current_direction[0]*-1)
                y_position=y_position+direction[current_direction][1]+(current_direction[1]*-1)
                current_direction=direction[current_direction]
            #No valid Moves , Time to break
            else:
                break
        pprint.pprint(result)
Solution().generateMatrix(5)
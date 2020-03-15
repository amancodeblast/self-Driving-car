# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one
g=0
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    init=[0,0]
    value=[[99 for i in range(len(grid))]for j in range(len(grid[0]))]
    change=True
    
    while change:
        change=False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x==goal[0] and y== goal[1] and value[x][y]==0:
                    change=True
                    value[x][y]=0
                elif grid[x][y]==0:
                    for a in range(len(delta)):
                        x1=x+delta[a][0]
                        y1=y+delta[a][1]
                        if x1>=0 and x1<len(grid)-1 and y1>=0 and y1<len(grid[0])-1:
                            if grid[x1][y1]==0:
                                v2=value[x1][y1]+cost

                                if v2<value[x][y]:
                                    value[x][y]=v2
                                    change=True
                                    
                                    
                            
                        
                    
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
p=compute_value(grid,goal,cost)
for i in range():
    print("{}\n".format(p[i]))

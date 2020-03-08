#grid format:
# 0=navigable space
# 1=occupied space

grid=[[0,0,1,0,0,0],
      [0,0,1,0,0,0],
      [0,0,0,0,1,0],
      [0,0,1,1,1,0],
      [0,0,0,0,1,0],
      ]

init =[0,0]
goal=[len(grid)-1,len(grid[0])-1]
delta=[[-1,0],
       [0,-1],
       [1,0],
       [0,1]]
dleta_name=["^","<","v",">"]
cost=1

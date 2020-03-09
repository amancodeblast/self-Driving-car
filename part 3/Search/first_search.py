#grid format:
# 0=navigable space
# 1=occupied space

grid=[[0,0,1,0,0,0],
      [0,0,1,0,0,0],
      [0,0,0,0,1,0],
      [0,0,1,1,1,0],
      [0,0,0,0,1,0]]

init =[0,0]
goal=[len(grid)-1,len(grid[0])-1]
delta=[[-1,0],
       [0,-1],
       [1,0],
       [0,1]]
dleta_name=["^","<","v",">"]
cost=1
g_val=[0,0,0,0]
for i in range(5):
    for j in range(6):
        
        
def search():
    closed=[[0 for row in range(len(grid[0]))]for col in range(len(grid[00]))]
    closed[init[0]][init[1]]=1
    x=init[0]
    y=init[1]
    gcar

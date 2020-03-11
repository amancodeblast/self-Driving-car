#grid format:
# 0=navigable space
# 1=occupied space

grid=[[0,0,1,0,0,0],
      [0,0,1,0,0,0],
      [0,0,0,0,1,0],
      [0,0,1,1,1,0],
      [0,0,0,0,1,0]]

init =[0,0]
g=1
goal=[len(grid)-1,len(grid[0])-1]
delta=[[-1,0],
       [0,-1],
       [1,0],
       [0,1]]
delta_name=["^","<","v",">"]
cost=1

no_escape=False
mila=False
 
def search():
    closed=[[0 for row in range(len(grid[0]))]for col in range(len(grid))]
    closed[init[0]][init[1]]=1
    x=init[0]
    y=init[1]
    open=[[g,x,y]]
    x1=0
    y1=0
    while no_escape==False and mila=False:
        if len(open)==0:
            no_escape=True
        else:
            open.sort()
            open.reverse()
            next=open.pop()                
            for i in range(len(delta_name)):
                x1=x+delta[i][0]
                y2=y+delat[i][1]
                g2=g+next[0]
                if x1>0 and x1< len(grid[0])and y2 >0 and y2< len(grid):
                    if closed[x1][y1]==0 and grid[x1][y1]==0:
                        open.append([g2,x1,y1])



            
            close[x1][y1]=ArithmeticError
                        
    if no_escape==True:
        print("hamse na ho paega")
    elif mila==True:
        print("ni mila")
    

#grid format:
# 0=navigable space
# 1=occupied space

grid=[[0,0,1,0,0,0],
      [0,0,0,0,0,0],
      [0,0,1,0,1,0],
      [0,0,1,0,1,0],
      [0,0,1,0,1,0]]

init =[0,0]

goal=[len(grid)-1,len(grid[0])-1]
delta=[[-1,0],
       [0,-1],
       [1,0],
       [0,1]]
delta_name=["^","<","v",">"]
cost=1


 
def search():
    closed=[[0 for row in range(len(grid[0]))]for col in range(len(grid))]# dont know why
    #such order for i and j is chosen as grid[0] and grid....it should be the reverse
    expand=[[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    closed[init[0]][init[1]]=1
    x=init[0]
    y=init[1]
    g=0
    gx=0
    open=[[g,x,y]]
    x1=0
    y1=0
    expand[x][y]=0
    no_escape=False#flag set if wee cant find expand
    mila=False#flag set if when search is complete
    while no_escape==False and mila==False:
        if len(open)==0:
            no_escape=True
            print("Fail")
        else:
            open.sort()
            open.reverse()
            next=open.pop()
            g=next[0]
            x=next[1]
            y=next[2]
            expand[x][y]=gx
            gx=gx+1
            if x==goal[0] and y==goal[1]:
                mila=True
                print("milgya")
                print("[{},{},{}]".format(g,x,y))
            else:
                for i in range(len(delta_name)):
                    x1=x+delta[i][0]
                    y2=y+delta[i][1]
                    
                    if x1>=0 and x1< len(grid)and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x1][y2]==0 and grid[x1][y2]==0:
                            g2=g+cost
                            
                            open.append([g2,x1,y2])
                            closed[x1][y2]=1
####12.expansion grid question                             
    for i in range(len(expand)):
        print(expand[i])
search()

#### 11. first search best code
#grid format:
# 0=navigable space
# 1=occupied space

grid=[[0,0,1,0,0,0],
      [0,0,0,0,0,0],
      [0,0,1,0,1,0],
      [0,0,1,0,1,0],
      [0,0,1,0,1,0]]
# print(' i = ',len(grid))
# print('i = ,', len(grid[0]))

init =[0,0]

goal=[len(grid)-1,len(grid[0])-1]
delta=[[-1,0],
       [0,-1],
       [1,0],
       [0,1]]
delta_name=["^","<","v",">"]
cost=1

def search():
    
    closed = [[0 for i in range(len(grid[0])) ]for j in range(len(grid))]
    
    closed[0][0]=1
    x = init[0]
    y= init[1]
    g=0
    open=[[g,x,y]]
    found = False
    quit = False
    
    while (found ==False and quit== False):
        if(len(open))==0:
            print("fail")
            quit=True
        else:
            open.sort()
            open.reverse()
            next=open.pop()
            
            x=next[1]
            y=next[2]
            g = next[0]
            if goal[0]==x and goal[1]==y:
                found=True
                print('found',next)
            else:
                for i in range(len(delta)):
                    x1= x+ delta[i][0]
                    y1 = y+ delta[i][1]
                    if(x1>=0 and x1 < len(grid) and y1>=0 and y1 < len(grid[0])and grid[x1][y1]==0 and closed[x1][y1]==0):                
                        g1=g+1
                        open.append([g1,x1,y1])
                        closed[x1][y1]=1
search()

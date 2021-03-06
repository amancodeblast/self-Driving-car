#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2
def sense(p, Z):
  q=[]
  for i in range(len(p)):
    if world[i]==Z:
      q.append(p[i]*pHit)
    else:
      q.append(p[i]*pMiss)
  return q
print(sense(p,Z))
studentMain.py
#Question
#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    return q
print sense(p,Z)
-----------------------------------------------------------------------
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2
def sense(p, Z):
  q=[]
  for i in range(len(p)):
    if world[i]==Z:
      q.append(p[i]*pHit)
    else:
      q.append(p[i]*pMiss)
  return q
print(sense(p,Z))
-------------------------------------------------------------------------
##NORMALIZE
#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2
def sense(p, Z):
  q=[]
  for i in range(len(p)):
    hit = (Z == world[i])
    q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
  s=sum(q)
  for i in range(len(q)):
      q[i]=q[i]/s
    
  return q

print(sense(p,Z))
-----------------------------------------------------------------------------
#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code 
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q
#
#ADD YOUR CODE HERE
#
for i in range(len(measurements)):
  p=sense(p,measurements[i])

print(p)
----------------------------------------------------------------------------------

from sys import stdin,stdout

t = int(stdin.readline().rstrip())
n = 0
c = 0
ans = []

def initialize():
	global n,a,c
	n = int(stdin.readline().rstrip())
	a = [[int(i) for i in stdin.readline().rstrip().split()] for j in range(0,n)]
	v = [[0 for i in range(0,n)] for j in range(0,n)]
	dfsCountUniquePath(a,0,0,v)
	ans.append(c)
	c = 0
#here (i,j) act as a node for the graph so the graph has n*n nodes and can have max 4 children
# (x-1,y)(x+1,y)(x,y-1)(x,y+1)

def dfsCountUniquePath(a,x,y,v):  #c is the counter
	global c,n
	v[x][y] = 1
	if(x == n-1 and y == n-1):
		c = c+1
	x1,x2,y1,y2 = x-1,x+1,y-1,y+1
	if(x1>-1 and x1<n and a[x1][y] == 0 and v[x1][y]==0):
		dfsCountUniquePath(a,x1,y,v)
		v[x1][y] = 0
	if(x2>-1 and x2<n and a[x2][y] == 0 and v[x2][y]==0):
		dfsCountUniquePath(a,x2,y,v)
		v[x2][y] = 0
	if(y1>-1 and y1<n and a[x][y1] == 0 and v[x][y1]==0):
		dfsCountUniquePath(a,x,y1,v)
		v[x][y1] = 0
	if(y2>-1 and y2<n and a[x][y2] == 0 and v[x][y2]==0):
		dfsCountUniquePath(a,x,y2,v)
		v[x][y2] = 0



for i in range(0,t):
	initialize()

for i in range(0,len(ans)):
	print(ans[i])


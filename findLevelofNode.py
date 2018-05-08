a = [
[1,1,1,0,0,0,0,0],
[1,1,0,1,1,1,0,0],
[1,0,1,0,0,0,1,0],
[0,1,0,1,0,0,0,0],
[0,1,0,0,1,0,0,0],
[0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,1],
[0,0,0,0,0,0,1,1]
]

queue = []
prev = [-1]*len(a)
level = [0]*len(a)
v = [0]*len(a)

def bfs(r,t):
	queue.append(r)
	level[r] = 0
	v[r] = 1
	while(len(queue)!=0):
		x = queue.pop(0)  #here 0 is the index to be popped
		print(str(x)+"  level: "+str(level[x]))
		for i in range(0,len(t[x])):
			if(t[x][i] == 1 and v[i] == 0 ):
				queue.append(i)
				level[i] = level[x] + 1
				v[i] = 1
				prev[i] = x

def pathBetween(x,y,a):
	g = []
	t = y
	while(1):
		print(t)
		g.append(t)
		if(t == x):
			break
		t = prev[t]
	print(list(reversed(g)))

bfs(2,a)
pathBetween(2,5,a)
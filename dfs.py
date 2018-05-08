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

stack = []
v = [0]*len(a) #visited

#normal dfs algo
def dfsIterative(a,s):	#graph,starting node
	stack.append(s)
	v[s] = 1
	while(len(stack)!=0):
		t = stack.pop()
		print(t)
		for i in range(0 , len(a)):
			if(a[t][i]==1 and v[i] == 0):
				v[i] = 1
				stack.append(i)

visited = [0]*len(a)

#normal dfs algo
def dfsRecursive(a,s):
	print(s)
	visited[s] = 1
	for i in range(0,len(a)):
		if(a[s][i] == 1 and visited[i] == 0):
			dfsRecursive(a,i)


dfsIterative(a,0)
print()
dfsRecursive(a,0)


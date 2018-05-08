from sys import stdin,stdout

n,e = map(int,stdin.readline().rstrip().split())

a = [[-1,-1,-1] for i in range(0,e)]

#store root of each node initially root of each node points to itself
#so if we want  to check if weather on adding this edge to the min path will give a cycle
#we check (initially each root[node] = node_itself) if root[x] == root[y] then it will result
#in a cycle and we do not consider the edge
#https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
r = [i for i in range(0,n+1)]


def sortAsc(z):
	global e
	for i in range(0,e):
		for j in range(0,e-i-1):
			if(z[j][0]>z[j+1][0]):
				t = z[j]
				z[j] = z[j+1]
				z[j+1] = t

def root(x):
	while(r[x]!= x):
		r[x] = r[r[x]]
		x = r[x]
	return x

def union(x,y):
	p = root(x)
	q = root(y)
	r[p] = r[q]


#input the edges
for i in range(0,e):
	x,y,w = map(int,stdin.readline().rstrip().split())
	a[i][0]=w;
	a[i][1]=x;
	a[i][2]=y;
#sort the edges in asc
sortAsc(a)
minSum = 0
for i in range(0,e):
	if(root(a[i][1]) != root(a[i][2])):
		minSum = minSum+a[i][0]
		union(a[i][1],a[i][2])
print(minSum)



#https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/travelling-tom-7eadedb7/
from sys import stdin,stdout
n,m,k = map(int,stdin.readline().rstrip().split())
c = [int(i) for i in stdin.readline().rstrip().split()]
a = [[-1 for i in range(0,k+4)] for j in range(0,m)]
l = k+4
r = [i for i in range(0,n+1)]
s = [0 for i in range(0,k+1)]# to store which token to buy

for i in range(0,m):
	x = [int(z) for z in stdin.readline().rstrip().split()]
	a[i][0] = x[0]
	a[i][1] = x[1]
	a[i][2] = x[2]
	v = 0
	for j in range(3,(3+x[2])):
		a[i][j] = x[j]
		v = v+c[x[j]-1]
	a[i][l-1] = v

def sortAsc(z):
	global m
	for i in range(0,m):
		for j in range(0,m-i-1):
			if(z[j][l-1]>z[j+1][l-1]):
				t = z[j]
				z[j] = z[j+1]
				z[j+1] = t


def root(x):
	while(r[x]!=x):
		r[x] = r[r[x]]
		x =r[x]
	return x

def union(x,y):
	p = root(x)
	q = root(y)
	r[p] = r[q]

sortAsc(a)
minSum = 0
for i in range(0,m):
	if(root(a[i][0]) != root(a[i][1])):
		for j in range(3,3+a[i][2]):
			if(s[a[i][j]] == 0):
				minSum = minSum+c[a[i][j]-1]
				s[a[i][j]] = 1
		union(a[i][0],a[i][1])

print(minSum)



"""
3 3 4
1 2 5 10
1 2 2 1 2
1 3 1 4
2 3 1 3
"""
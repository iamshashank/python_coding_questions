#https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/friendless-dr-sheldon-cooper-14/
"""
After a bit of digging around I think I understand the problem: 
a is the number of nodes, b is the number of pairs
b lines follow: each with a pair of nodes that are connected 
the input assures only one connected graph exists, find number of nodes in graph and print that number-1.
I passed all test cases with this understanding.
"""

#https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/travelling-tom-7eadedb7/
from sys import stdin,stdout
t = int(stdin.readline().rstrip())
ans =[]





def root(x):
	while(r[x]!=x):
		r[x] = r[r[x]]
		x =r[x]
	return x

def union(x,y):
	p = root(x)
	q = root(y)
	r[p] = r[q]

for z in  range(0,t):
	n,m = map(int,stdin.readline().rstrip().split())
	a = [[-1, -1] for j in range(0,m)]
	r = [i for i in range(0,n+1)]
	for i in range(0,m):
		x = [int(v) for v in stdin.readline().rstrip().split()]
		a[i][0] = x[0]
		a[i][1] = x[1]
	minSum = 0
	for i in range(0,m):
		if(root(a[i][0]) != root(a[i][1])):
			minSum = minSum+1
			union(a[i][0],a[i][1])
	ans.append(minSum)

for i in range(0,t):
	print(ans[i])




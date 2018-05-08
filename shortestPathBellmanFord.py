#not optimal but can detect Cycle Cycle
#based on principle of relaxing each node (n-1) times cuz shortest path can contain at-most n-1 edges

n,e = map(int,input().rstrip().split())
a = [[int(i) for i in input().rstrip().split()] for j in range(0,e)]
dis = [999999]*(n+1)
dis[1] = 0
for i in range(0,n-1):
	for j in range(0,e):
		if(dis[a[j][0]] + a[j][2] < dis[a[j][1]]):
			dis[a[j][1]] = dis[a[j][0]] + a[j][2]

ans = " "
for i in range(2,n+1):
	ans = ans + " " + str(dis[i])

print(ans.strip())

"""
4 6
1 2 10
1 3 80
2 3 100
3 2 -75
2 4 5
3 4 7
"""
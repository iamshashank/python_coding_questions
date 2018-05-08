#uses min-heap
from sys import stdin,stdout
n,e = map(int,stdin.readline().rstrip().split())
a = [[(0,0)] for i in range(0,n+100)]
#a = [[int(i) for i in input().rstrip().split()] for j in range(0,e)]
visited = [0]*(n+1)
dis = [1000000000]*(n+1)
dis[1] = 0
#(node,weight)
#minHeap = [(i,1000000000) for i in range(0,n+1)]
minHeap = []  

#hMap = {str(i):i for i in range(0,n+1)}
p,q,r = -1,-1,-1

for i in range(0,e):
	p,q,r = map(int, stdin.readline().rstrip().split())
	a[p].append((q,r))  #add the tuple[from]=>[(to,w1)],(to,w2)] eg: [1] => [(2,10)(4,50)] (to,weight)

#input complete

def minHeapify(a,i,l):  #(minHeap,i)
	#if no child exist
	if((i*2+1>l) and (i*2+2>l)):
		return
	#if only left child exist
	if(i*2+1<=l and i*2+2>l): #our counting is from 0
		if(a[i*2+1][1]<a[i][1]):
			t = a[i*2+1]
			a[i*2+1] = a[i]
			#hMap[str(a[i][0])] = i*2+1
			a[i] = t
			#hMap[str(t[0])] = i
			minHeapify(a,i*2+1,l)
	#if both child exist and left child is samller tahn both parent and right child
	elif(a[i*2+1][1]<a[i*2+2][1] and a[i*2+1][1]<a[i][1]):
		t = a[i*2+1]
		a[i*2+1] = a[i]
		#hMap[str(a[i*2+1][0])] = i*2+1
		a[i] = t
		#hMap[str(t[0])] = i
		minHeapify(a,i*2+1,l)
	#if both child exist and left child is samller
	elif(a[i*2+2][1]<a[i*2+1][1] and a[i*2+2][1]<a[i][1]):
		t = a[i*2+2]
		a[i*2+2] = a[i]
		#hMap[str(a[i*2+2][0])] = i*2+1
		a[i] = t
		#hMap[str(t[0])] = i
		minHeapify(a,i*2+2,l)

def getMin(a):
	x = []
	if(len(a)>0):
		x = a[0]
		g = a.pop() #last element poped
		if(len(a)>0):
			a[0] = g
			#hMap[str(a[0][0])] = 0
			minHeapify(a,0,len(a)-1)
	return x

def insert(a,tup):
	a.append(tup)
	l = len(a)-1
	#hMap[str(tup[0])] = l #update hash 
	while(l>0):
		pIndex = int((l-1)/2)
		if(a[pIndex][1]>a[l][1]):
			#swap
			t = a[pIndex]
			a[pIndex] = a[l]
			#hMap[str(a[l][0])] = pIndex
			a[l] = t
			#hMap[str(t[0])] = l
			l=int((l-1)/2)
		else:
			break
"""
def decreaseKey(a,key,value):
	i = hMap[str(key)]
	a[i][1] = value
	minHeapify(a,int((i-1)/2),len(a)-1)
"""
def log():
	print(visited)
	print(dis)
	print(minHeap)
	#print(hMap)

#insert 1st (1,0) in min heap
insert(minHeap,[1,0])

while(len(minHeap)!=0):
	t = getMin(minHeap)
	#check id already visited
	if(visited[t[0]] == 1):
		continue
	#mark it
	visited[t[0]] = 1
	x = t[0]
	y = t[1]
	for i in range(1,len(a[x])):
		p = a[x][i][0]
		q = a[x][i][1]
		if(dis[x] + q < dis[p]):
			dis[p] = dis[x] + q
			insert(minHeap,[p,dis[p]])

ans = " "
for i in range(2,n+1):
	ans = ans +" "+ str(dis[i])

print(ans.strip())
"""
6 17
1 2 3
1 4 20
1 6 50
1 5 10
1 3 4
2 4 7
2 6 2
2 5 3
2 3 2
3 2 4
3 4 3
3 6 2
3 5 1
4 5 3
4 6 1
5 4 6
5 6 3
"""
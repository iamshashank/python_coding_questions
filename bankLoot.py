#https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/description/

key,lock =input().rstrip().split()
key = int(key)
lock = int(lock)
n = input().rstrip()
n = int(n)
keys = [int(x) for x in input().rstrip().split()]
val = [-1] * 100000
val[key] = 0
queue = []

def solveBFS():
	queue.append(key)
	while(len(queue)!=0):
		t = queue.pop(0)
		for i in range(0 , n):
			v = (t * keys[i])%100000
			if(val[v] == -1):
				val[v] = 1 + val[t]
				queue.append(v)
	print(val[lock])

solveBFS()


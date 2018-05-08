#unsorted array
a = [0,2,4,6,3,7,8,9]
alen = 7
b = [0]
blen = 0
def maxHeapify(arr,i,n):
	if((i*2>n) and (i*2+1>n)):
		return
	#only left child 
	if((i*2<=n) and (i*2+1>n)):
		if(arr[i*2]>arr[i]):
			t = arr[i]
			arr[i] = arr[i*2]
			arr[i*2] = t
			maxHeapify(arr,i*2,n)
	elif((arr[i*2]>=arr[i*2+1]) and (arr[i*2]>arr[i])): #or both child and left child is greater than right
		t = arr[i]
		arr[i] = arr[i*2]
		arr[i*2] = t
		maxHeapify(arr,i*2,n)
	elif(arr[i*2+1]>=arr[i*2] and (arr[i*2+1]>arr[i])):
		t = arr[i]
		arr[i] = arr[i*2+1]
		arr[i*2+1] = t
		maxHeapify(arr,i*2+1,n)

def insertInMaxHeap(item,arr):
	arr.append(item)
	global blen
	blen=blen+1
	l = blen
	while(l>1):
		pIndex = int(l/2)
		if(arr[pIndex]<arr[l]):
			#swap
			t = arr[pIndex]
			arr[pIndex] = arr[l]
			arr[l] = t
			l=int(l/2)
		else:
			break


def buildMaxHeap(n,arr):
	for i in range(int((n-1)/2),0,-1):
		maxHeapify(arr,i,n)
	print(arr)
	return

def deleteMax(arr):
	global blen
	if(blen>0):
		item = arr[1]
		blen=blen-1
		arr[1] = arr.pop()  #last element is popped and  put at index 1 and maxheapify is called
		maxHeapify(arr,1,blen)
		return item


buildMaxHeap(len(a)-1,a)


insertInMaxHeap(10,b)
insertInMaxHeap(70,b)
insertInMaxHeap(30,b)
insertInMaxHeap(40,b)
insertInMaxHeap(80,b)
insertInMaxHeap(70,b)
insertInMaxHeap(20,b)
print(b)
print(deleteMax(b))
print(deleteMax(b))
print(deleteMax(b))

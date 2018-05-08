from sys import stdin,stdout

t = int(stdin.readline().rstrip())
for i in range(0,t):
	n = int(stdin.readline().rstrip())
	a = [int(x) for x in stdin.readline().rstrip().split()]
	if(n == 1):
		stdout.write("1 0\nMotu\n")
	elif(n == 2):
		stdout.write("1 1\nTie\n")
	else:
		mIndex = 0
		motu = a[0]
		pIndex = n-1
		patlu = a[n-1]
		while(mIndex<pIndex):
			if(motu>2*patlu):
				pIndex = pIndex-1
				patlu = patlu+a[pIndex]
			if(motu<2*patlu):
				mIndex = mIndex+1
				motu = motu+a[mIndex]
		if(mIndex>(n-pIndex)):
			if((mIndex+(n-pIndex)) < n):
				pIndex = pIndex+1
			stdout.write(str(mIndex)+' '+str(n-pIndex)+"\nMotu\n")
		elif(mIndex<(n-pIndex)):
			stdout.write(str(mIndex)+' '+str(n-pIndex-1)+"\nPatlu\n")
		else:
			stdout.write(str(mIndex)+' '+str(n-pIndex)+"\nTie\n")

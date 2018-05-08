#input a int
#int() for conversion
#str()
n = input()
print(n)
#input 5 int and store in listy
#split by default usses ' ' delimiter 
arr = [int(x) for x in input().split()]
print(arr)
#use '/'as delimiter and input string
arr = [x for x in input().split('/')]
print(arr)


#input to map 
a,b,c = map(int, input().split())
print(a*b*c)

#faster sys stdin stdout
from sys import stdin,stdout
t = int(stdin.readline().rstrip())
a,b,c = map(int , stdin.readline().rstrip().split())
print(a*b*c)
stdout.write(str(a*b*c)+'\n')
#inbild functions
abs(-24) #return 24
bool(1) #true
bool(0) #false
print bool(-1) #true
s = "this is sentence.\n This is gta"
print s.splitlines() #returnes list
x = 10
#type conversion
str(x) #convert to string
float(x) #convert to float
int(x)

print("Hello World")
age = 10
print(age)
a,b,c = 10,20,30
print(a,b,c)
a = b = c = 40
print(a)
name,lastname = "lenovo","pc"
full = name+" "+lastname
print(full)
print("H"*10)
name  = "This is a tutorial video"
print name[0]
print(name[1:4]) #splising bacically substring [statinf Index:Ending Index+1]
print(name[:4])
print(name[:-2]) #every thing but last 2 character
print(name[4:-2])
#place holders
name = "jake"
placeHolderString = "%s is 15 year old"
print(placeHolderString%("jake"))
print(placeHolderString%(name))
# %d integer %f float
placeHolderString = "%s %s is awesome"
print(placeHolderString%("Captain","Levi"))

placeHolderString = "%f"
print(placeHolderString%(10.003))

#list or array counting from 0
shopList = ["apple",11,"oranges","grapes"]  #mixing of datatype allowed
print(shopList[0])
print(shopList[0:2]) #print 0,1 index
shopList.append("pineaple") #at last insertion
shopList[0] = "cherries"  #change the first index
del shopList[2] #delete index 2 from list
print len(shopList) #length of list
print(shopList)
shopList.pop()
print(shopList)
shopList.insert(4,5)  #insert 5 at 4th index
print shopList
shopList.sort()
print(shopList)
shopList.reverse()
print(shopList)
print shopList.index(11) #return the fistindex of 11
print shopList.count(11) #count no of times 11 is in array
#combine 2 list
shopList2 = ["guava","strawberry"]
shopList3 = shopList + shopList2
print(shopList3)
#multiply list
list4 = shopList*3 #mul 3 times
numList = [1,1,3,5,7,33,5]
print(max(numList))
print(min(numList))

#DICTIONARY key value pair
students = {"gta":5,"cod":3,"anime":5}
print(students["cod"])
students["cod"] = 4  #update the value
students["awesome"] = 55
print(students)
del students["cod"]  #delete key value pair\
len(students)  #length of dictonary
#unique keys 

#TUPLES
#are similar to lists but are immutable and cant be modifeid
t1 = ('gta',1,'moron')
t1[0] #for accessing
#splicing
t1[0:3] #print first 3 elemenst
t2 = ('22',44)
t3 = t1+t2
len(t3)
print t3
#you can delete entire tuple 
del t3
#but you cannot indiviusal item iside a tuple
#multiply (replicate) the tuple
t4 = t1*3
print t4

#CONDITIOAL
# == <= >= !=
if(5>3):
	print("hello")
else:
	print("gta")
if((5>3) and (3<2)):
	print('true')
elif(8>9 or 3==3):
	print('elif')
else:
	print('false')


#LOOPS

list1 = ['aple','banana','cheerries',1,3]
t1 = ('apple',1,2,'gta')

for item in list1:
	print(item)
for item in t1:
	print(item)
#range
for i in range(0,10):
	print(i) #preint from 0 to 9

for i in range (0,11,2):
	print(i)  # here '2' is the incerement facor

for i in range(0,5):
	for j in range(0,5):
		print(i*j)
c = 0
while c<5:
	print c
	c=c+1
	if(c == 3):
		break #continue
c = 0
while(c<5):
	print c
	c = c+1

#pass control stament
c = 0
while c<5:
	c = c+1
	if c==3:
		pass
	print c

#try except errot handeling

try:
	if zyx == 0: #varible is not defined
		print 'try block'
except:
	print 'something is wrong'

"""
this how we write multiple line comment
all this is commment
"""


#FUNCTION
def funcName():
	print 'hello world'

funcName()

def add(x,y):
	print x+y
	return x+y
print add(10,30)


#OOPS

class Person:
	def getName(self): #'self' parameter is mandatory
		print 'Alvin'
	def getAge(self):
		print '12'
	def Add(self,x,y):
		return x+y

p = Person()
p.getName()
p.getAge()
print p.Add(10 ,20)

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def getDetails(self):
		print self.name,self.age
		print "%s Age: %d"%(self.name,self.age)
		print str(self.name)+" "+str(self.age)

p = Person('Bob',22)
p.getDetails() 
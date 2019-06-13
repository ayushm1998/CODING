a=[0,4,8,40,28,5,3,20,10,9,13,1,3,4,18,15,17]
b=[]
c=[]
for i in a:
	if i>5:
		b.append(i)
	elif i<=2:
		c.append(i)
print("MY LIST")
print(a)
print("LIST1:")
print(b)
print("LIST2:")
print(c)

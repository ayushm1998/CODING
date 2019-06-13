import datetime
name=input("What's your name?")

now = datetime.datetime.now() 
t=now.hour
print(t)
if t<12 or t>24:
	print("Good Morning",name)
elif t>11 or t<17:
	print ("Good Afternoon",name)
elif t>16 or t<19:
	print("Good Evening",name)
else:
	print("Good Night",name)


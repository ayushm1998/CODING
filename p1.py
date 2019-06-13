#!usr/bin/python3
import datetime

NAME=input("Enter you name:")
AGE=int(input("Enter your age:"))
d= datetime.date.today().year
f=int((95-AGE)+d)
print("NAME:",NAME)
print ("AGE:",AGE)
print("YOU WILL BE 95 IN:",f)

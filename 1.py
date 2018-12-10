#! /usr/bin/python3


def fun1():
	l=[]
	for i in range( 2000 , 3001):
		if (i%7==0) & (i%5!=0):
			l.append(i)
	return l

a=fun1()
for l in a:
	print(l,end=",")

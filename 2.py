#!/usr/bin/python

def fun1(n):
	if n==0:
		return 1
	else:
		return(n*fun1(n-1))

a=fun1(15)
print(a)

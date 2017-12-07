# usr/bin/env python3
# -*- coding=utf-8 -*-

import math
# math.sqrt(2)
# print(math.sqrt(2))

def quadratic(a,b,c):
	L=[a,b,c]
	for d in L:
		if not isinstance(d,(int,float)):
			raise TypeError('bad operand type')
	if a==0:
		print('一元二次方程，a不能为0')
	else:
		dert=(b*b-4*a*c)
		if dert>=0:
			x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
			x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
			return x1,x2
		else:
			print('dert<0无解')
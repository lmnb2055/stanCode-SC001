"""
File: quadratic_solver.py
Name: Sidney
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	enter a, b, c, to ensure Quadratic Solver
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	# discriminant
	y = b * b
	x = -4 * a
	z = c
	discriminant = y + x * z
	if discriminant > 0:
		d = math.sqrt(discriminant)
		b *= -1
		a *= 2
		b += d
		ans1 = b / a
		b -= d
		ans2 = b / a
		print('Two roots'+':  '+ str(ans1)+',  '+str(ans2))
	elif discriminant == 0:
		d = math.sqrt(discriminant)
		b *= -1
		a *= 2
		b += d
		ans3 = b / a
		print('one root'':  '+ str(ans3))
	else:
		print('no root')








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()

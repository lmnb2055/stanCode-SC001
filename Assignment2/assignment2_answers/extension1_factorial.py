"""
File: extension1_factioral.py
Name: Sidney
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

Exit = -100

def main():
	"""
	get a number, and I will list the answer of factorial
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		n = int(input('give me a number, and I will list the answer of factorial:  '))
		# help to us to maintain the original variable n
		m = n
		if n == Exit:
			print('- - - - - - See ya! - - - - - -')
			break
		elif n <= 1:
			print('Answer: ' + '1')
			break
		else:
			while True:
				# n will minus 1 to multiply m which is n.
				if n > 1:
					n -= 1
					m *= n
				else:
					print('Answer: ' + str(m))
					break






# def main():
#     """
#     Call my_smaller function
#     """
#     n1 = int(input('First Number: '))
#     n2 = int(input('Second Number: '))
#     smaller = my_smaller(n1, n2)
#     print(smaller)
#
#
# def my_smaller(n1, n2):
#     """
#     :param n1: int
#     :param n2: int
#     :return: int, the smaller one between n1 and n2
#     """
#     if n1 > n2:
#         return
#     return n2


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
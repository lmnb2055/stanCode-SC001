"""
File: prime_checker.py
Name: Sidney
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
	"""
	TODO:
	"""
	print('Welcome to the prime checker')
	while True:
		n = int(input('n: '))
		a = n - 1
		if n == EXIT:
			print('Have a good one! ')
			break
		else:
			# a > 1 excluding factor 1.
			while a > 1:
				# n divides by all positive integer smaller than n, except for 1
				if n % a != 0:
					a -= 1
				else:
					print(str(n) + ' is not a prime number.')
					n = int(input('n: '))
			print(str(n) + ' is a prime number.')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()

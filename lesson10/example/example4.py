
def factorial(n):
	if n <= 0:
		return 1
	return n*factorial(n-1)

# 8!

if __name__ == '__main__':
    print(factorial(4))
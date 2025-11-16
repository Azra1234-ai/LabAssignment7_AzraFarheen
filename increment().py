def count_down(n):
	while n >= 0:
		print(n)
		n -= 1  # decrement to avoid infinite loop

# example usage
if __name__ == "__main__":
	count_down(5)

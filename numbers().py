numbers = [1, 2, 3]
index = int(input("Enter an index number: "))

if 0 <= index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range")

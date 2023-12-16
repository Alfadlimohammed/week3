num = input("Please enter a number between 1 and 10: ")
num = int(num)
if 1 < num < 10:
    print(f"The entered value {num} is in the requested range.")
else:
    print(f"The entered value {num} is not in the requested range.")
if __name__ == '__main__':
    x = input("enter the first value x ? ")
    y = input("enter the secound value y ? ")
    x = int(x)
    y = int(y)
    if x > y:
        print(f"the value{x}is large than the value{y}")
    else:
        print(f"the value{y}is large than the value{x}")
if __name__ == '__main__':
    value1 = float(input("Enter the first value: "))
    value2 = float(input("Enter the second value: "))
    if value2 != 0:
        result = value1 / value2
        print(f"The result of dividing {value1} by {value2} is: {result}")
    else:
        print("Division by 0 is not possible.")
if __name__ == '__main__':
    count = 0
    while count < 100:
        count += 1
        print("Mohammed")
if __name__ == '__main__':
    for x in range(1, 10):
        for y in range(1, x):
            print("*")
        print()

age = 25
is_under_18 = age < 18
is_under_21 = age < 21
is_under_31 = age < 31
print("Is the age under 18?", is_under_18)
print("Is the age under 21?",  is_under_21)
print("Is the age under 31?", is_under_31)
if __name__ == '__main__':
    age = input("Enter your age: ")
    18 == age
    if __name__ == '__main__':
        age = 30
        re1 = age >= 18 and age <= 65
        re2 = age < 18 or age > 65
        re3 = not age > 18
        print(re1)
        print(re2)
        print(re3)
if __name__ == '__main__':
    age = 30
    result = (age >= 18 and age <= 65) and (not age == 30)
    print(result)
if __name__ == '__main__':
    weight = 150
    height = 140
    expression1 = 100 < weight < 200
    expression2 = 131 < height < 160
    print("Equivalent expression for weight:", expression1)
    print("Equivalent expression for height:", expression2)
if __name__ == '__main__':
    age = float(input("enter your age: "))
    if 18 <= age <= 30:
        print("you are still young")
if __name__ == '__main__':
    age = int(input("Enter your age: "))

    if age > 100:
        print("you are very old,")
        print("well done!")
    elif age > 80:
        print("you are fairly old")
        print("pretty good!")
    elif age > 40:
        print("you are middle-aged")
        print("never mind")
    else:
        print("you are not very old - yet")
if __name__ == '__main__':
    age = int(input("Enter your age: "))

    if age > 100:
        print("You are very old, well done!")
    elif 30 <= age <= 40:
        print("You are between 30 and 40 years old, getting there!")
if __name__ == '__main__':
    total = int(input("Enter a total value: "))
    if total != 0:
        print("Total is non-zero")
    else:
        print("Total is zero")
if __name__ == '__main__':
    name = ("ali", "ahmad", "khaled", "noor")
    for name in name:
        print(name)
if __name__ == '__main__':
    for i in range(2, 11, 2):
        result = i ** i
        print(f"{i} to the power of {i} = {result}")
if __name__ == '__main__':
    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    running_total = 0
    for num in numbers:
        running_total += num
        print(f"Running total: {running_total}")
if __name__ == '__main__':
    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    running_total = 0
    for num in numbers:
        running_total += num
        print(f"Running total: {running_total}")
        if num > 100:
            print(f"Breaking loop. Found value {num} over 100.")
            break
if __name__ == '__main__':
    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    running_total = 0
    for num in numbers:
        running_total += num
        print(f"Running total: {running_total}")
        if num > 100:
            print(f"Breaking loop. Found value {num} over 100.")
            break
        else:
            print("All numbers processed")
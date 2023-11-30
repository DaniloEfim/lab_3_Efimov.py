def Task1():
    john = 3
    mary = 5
    adam = 6

    print(f"{john}, {mary}, {adam}")

    total_apple = john + mary + adam

    print("Total apple:", total_apple)


def Task2():
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

def Task3():
    x = 0
    x = float(x)

    y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
    print("y =", y)

def Task4():

    a = 2
    seconds = 3600

    print("Hours: ", a)
    print("Seconds in Hours: ", a * seconds)

def Task5():
    a = float(4)
    b = float(3)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print("That's all, folks!")

def Task6():
    x = float(-5)
    sum = 1 / (x + 1/(x + 1/(x + 1/(x + 1/(x)))))
    print("Y =", sum)

def Task7():
    h = int(12)
    m = int(17)
    d = int(59)
    sum = (h * 60) + m + d
    print(f"{sum // 60}:{sum % 60}")

print("\n")
print("Task1:\t")
Task1()
print("\n")
print("Task2:\t")
Task2()
print("\n")
print("Task3:\t")
Task3()
print("\n")
print("Task4:\t")
Task4()
print("\n")
print("Task5:\t")
Task5()
print("\n")
print("Task6:\t")
Task6()
print("\n")
print("Task7:\t")
Task7()
print("Hello git!")


def f1(x, y):
    print(x + y)

f1(2, 3)
f1(5, 9)


def func(x):
    print(x ** 5)

func(2)


def f23(x, y, z):
    print(x, y, z)
    x *= y
    y **= z
    z += x
    print(x, y, z)

f23(3, 4, 5)
# Optional Parameters
# To recall, parameters are input that must be passed to a function or
# method from the call statement. Unlike many other languages python supports optional parameters.
# If we setup a parameter to be optional that means we can omit passing it to the function or method
# in the call statement. To declare an optional parameter we simply set a default value for
# it when we create it. If we do not pass a value the default value will be used,
# if we pass a value it will be the value for the parameter.


def myFunc(x=5):
    print(x)


myFunc()  # 5
myFunc(10)  # 10

# It is possible to have multiple optional parameters.


def myFunc2(x=5, y=12):
    print(x, y)
    print(x + y)


myFunc2()  # 5 12
myFunc2(10)  # 10 12
myFunc2(10, 10)  # 10 10
myFunc2(x=1, y=2, z=4)  # TypeError: myFunc2() got an unexpected keyword argument 'z'


# It is also possible to use a combination or optional and non-optional parameters.
def myFunc(x, y=6):
    print(x + y)


myFunc(12)  # 18
myFunc(12, 10)  # 22


def funcSecond(x, y, z=4):
    print(x + y + z)


funcSecond(1, 2)  # 7
funcSecond(1, 2, 3)  # 6
funcSecond(y=0.3, x=0.5, z=0.5)  # 1.3


def compliacteFunc(x, hello="Hello", world="World"):
    if x != 0:
        print(f"{x} is not zero, so {hello} {world}!")
    else:
        print(f"{x} is zero, so {hello} {world} anyways!")


compliacteFunc(5)  # 5 is not zero, so Hello World!
compliacteFunc(0)  # 0 is zero, so Hello World anyways!


def anotherFunc(a="A", b=0, c=None):
    print(f"a: {a}, b: {b}, c: {c} ")


anotherFunc()  # a: A, b: 0, c: None


# We can also use expressions as default values for optional parameters.
# The expression will be evaluated at the time of the function definition,
# not at the time of the function call.
def anotherFunc2(a, b=0, c=10 + 10):
    print(f"We have {a} and b as {b}, but what about c that is {c}?")


anotherFunc2("Hello")  # We have Hello and b as 0, but what about c that is 20?


# Defined parameters should be after non defined parameters.
# If we try to define a parameter before a non defined parameter
# we will get a syntax error.
def aBigFunc(
    a,
    b,
    e,
    c=10,
    d=20,
):
    print(f"Here we have a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")


aBigFunc(1, 3, 90)  # Here we have a: 1, b: 3, c: 10, d: 20, e: 90

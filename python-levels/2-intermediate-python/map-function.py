# Map Function
# The map function can be used to apply a function to every element in a given list.
# For example, if we wanted to apply a function f1 to a list of
# numbers we would usually do something like this:


def f1(x):
    return x + x / 2


nums = [1, 2, 3, 4, 5]

newList = []
for item in nums:
    newList.append(f1(item))

newList  # [1.5, 3.0, 4.5, 6.0, 7.5]

# However the map function can eleminate a lot of this work and perform this same task in one line.


def f2(x):
    return x + x / 2


nums2 = [1, 2, 3, 4, 5]

newList2 = list(map(f2, nums2))
newList2  # [1.5, 3.0, 4.5, 6.0, 7.5]

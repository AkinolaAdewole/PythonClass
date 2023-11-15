# List Methods:
#
# list.append(), list.extend(): Add elements to a list.
# list.pop(), list.remove(): Remove elements from a list.
# list.index(), list.count(): Find the index of an element or count occurrences in a list.
# list.sort(), list.reverse(): Sort elements or reverse the order of elements in a list.

# Set Methods:
# set.add(), set.update(): Add elements to a set.
# set.remove(), set.discard(): Remove elements from a set.
# set.union(), set.intersection(): Perform set union or intersection operations.
# set.difference(), set.symmetric_difference(): Find the difference or symmetric difference
# between sets.

num1 = [0, 1, 2, 3, 4, 5]
num1.clear()
print(num1)

num2 = [0, 1, 2, 3, 4, 5]
num2.append(6)
print(num2)
print(len(num2))

num3 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
num3.insert(0, "A")
print(num3)
print(len(num3))

num4 = [0, 1, 2, 3, 4, 5]
print(2 in num4)
print(8 in num4)
thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)

a_list = list(thistuple)
a_list[1] = "pear"
thistuple = tuple(a_list)
print(thistuple)

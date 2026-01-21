x = [1, 2, 3]
y = x
z = [1, 4, 3]

print(x is y)        # True  (y references the same list as x)
print(x is z)        # False (z is a different list with same value)
print(x == z)        # True  (values are same)

print(x is not z)    # True

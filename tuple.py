#create
fruits = ("apple", "banana", "cherry")
print(fruits)
#length
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#
fruits = ("apple",)
print(fruits)
#accessing
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
print(fruits[2])
print(fruits[-1])
print(fruits[1:4])
print(fruits[:2])
print(fruits[4:])
print(fruits[-4:-2])
#checking
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
if "banana" in fruits:
    print("Yes")
#change
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
y = list(fruits)
y[1] = "watermelon"
x = tuple(fruits)
print(x)
#append
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
y = list(fruits)
y.append("orange")
x = tuple(fruits)
print(x)
#
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
y = ("orange",)
fruits += y
print(fruits)
#remove
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
y = list(fruits)
y.remove("banana")
print(y)


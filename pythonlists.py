#sample
fruits = ["apple", "banana", "cherry"]
print(fruits)
#length
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print (len(fruits))
#accessing
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits[2])
print(fruits[-1])
print(fruits[1:4])
print(fruits[:2])
print(fruits[4:])
print(fruits[-4:-2])
#check
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
if "banana" in fruits:
     print("banana")
#change
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[2] = "blueberry"
print(fruits)
#change range
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[2:4] = ["blueberry", "orange"]
print(fruits)
#append
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
#insert
fruits = ["apple", "banana", "cherry"]
fruits.insert(2,"orange")
print(fruits)
#extend
fruits = ["apple", "banana", "cherry"]
names = ["kiwi", "mango"]
fruits.extend(names)
print(fruits)
#remove
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.remove("cherry")
print(fruits)
#pop()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.pop(2)
print(fruits)
#
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)
#del
fruits = ["apple", "banana", "cherry"]
del fruits[2]
print(fruits)
#clear
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
#loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#indexing in loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in range(len(fruits)):
    print(fruits[x])
#while
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
i=0
while i < len(fruits):
    print(fruits[i])
    i=i+1
#sort
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print(fruits)
#decending
fruits.sort(reverse=True)
print(fruits)
#case insensitive
fruits = ["apple", "Banana", "cherry", "Kiwi", "mango"]
fruits.sort()
print(fruits)
#reverse
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.reverse()
print(fruits)
#copy
fruits = ["apple", "banana", "cherry"]
names = fruits.copy()
print(names)
#add
fruits = ["apple", "banana", "cherry"]
names = ["kiwi", "mango"]
total = fruits + names
print(total)







#create
names = {"Krishna","Palani","Sai","Nagini"}
print(names)
#duplicates are not allowed\
names = {"Krishna","Palani","Sai","Nagini", "Palani"}
print(names)
#true, 1 are same and false, 0 are same
names = {"Krishna","Palani","Sai","Nagini",1,0, True, False}
print(names)
#
names = {"Krishna","Palani","Sai","Nagini"}
print (type(names))
#leng
names = {"Krishna","Palani","Sai","Nagini"}
print(len(names))
#access
#for
names = {"Krishna","Palani","Sai","Nagini"}
for x in names:
    print(x)
#in
names = {"Krishna","Palani","Sai","Nagini"}
print("Krishna" in names)
#add
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
#add sets = update.
fruits = {"apple", "banana", "cherry"}
names = {"Krishna","Palani","Sai","Nagini"}
fruits.update(names)
print(fruits)
#
names = {"Krishna","Palani","Sai","Nagini"}
fruits = ["apple", "banana", "cherry"]
names.update(fruits)
print(names)
#remove
names = {"Krishna","Palani","Sai","Nagini"}
names.remove("Krishna")
print(names)
#discard
names = {"Krishna","Palani","Sai","Nagini"}
names.discard("Krishna")
print(names)
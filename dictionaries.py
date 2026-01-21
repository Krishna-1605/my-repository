#create
mine = {"name": "krishna", "age": 27, "college" :"KLU"}
print(mine)
#length
mine = {"name": "krishna", "age": 25, "college": "KLU"}
print(len(mine))
#access
mine = {"name": "krishna", "age": 25, "college": "KLU"}
x = mine["age"]
print(x)
#get
mine = {"name": "krishna", "age": 25, "college": "KLU"}
x = mine.get("age")
print(x)
#get keys
mine = {"name": "krishna", "age": 25, "college": "KLU"}
x = mine.keys()
print(x)
#get values
mine = {"name": "krishna", "age": 25, "college": "KLU"}
x = mine.values()
print(x)
#get items
mine = {"name": "krishna", "age": 25, "college": "KLU"}
x = mine.items()
print(x)
# check
mine = {"name": "krishna", "age": 25, "college": "KLU"}
if "age" in mine:
    print("Yes")
#change
mine = {"name": "krishna", "age": 25, "college": "KLU"}
mine["age"] = 27
print(mine)
#change update
mine = {"name": "krishna", "age": 25, "college": "KLU"}
mine.update({"age" : 27})
print(mine)
#add
mine = {"name":"Krishna", "age":25, "college": "KLU"}
mine.update({"age":27})
mine.update({"year":2020})
print(mine)
#remove
#pop()
mine = {"name": "krishna", "age":25, "college": "KLU"}
mine.pop("age")
print(mine)
#popitem()
mine = {"name": "krishna", "age":25, "college": "KLU"}
mine.popitem()
print(mine)
#del
mine = {"name": "krishna", "age":25, "college": "KLU"}
del mine["age"]
print(mine)
#clear
mine = {"name": "krishna", "age":25, "college": "KLU"}
mine.clear()
print(mine)
#for
mine = {"name": "krishna", "age":25, "college": "KLU"}
for x in mine:
    print(x)
#for keys
mine = {"name": "krishna", "age":25, "college": "KLU"}
for x in mine.keys():
    print(x)
# values
mine = {"name": "krishna", "age":25, "college": "KLU"}
for x in mine.values():
    print(x)
#for items
mine = {"name": "krishna", "age":25, "college": "KLU"}
for x in mine.items():
    print(x)
#copy()
mine = {"name": "krishna", "age":25, "college": "KLU"}
myself = mine.copy()
print(myself)
#nested


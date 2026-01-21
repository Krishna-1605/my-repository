#
#create a string
s1 = "Hello"
s2 = 'This is'
s3 = """Krishna Nagini"""
print(s1)
print(s2)
print(s3)
#
#accessing
s1 = "Krishna"
print(s1[3])
print(s1[-1])
#
#looping
text = "Python"
for ch in text:
    print(ch)
#reverse looping
text = "Python"
for ch in reversed(text):
    print(ch)
#
#lenght
text = "Krishna Nagini"
print(len(text))
##username too long
username="KrishnaNagini"
if len(username) > 12:
    print("username is too long")
else:
    print("username is ok")
#
#password check
Password="KrishnaNagini"
if len(username) < 8:
    print(" Password is too long")
else:
    print("Password is ok")
#
#check substring
txt = "KrishnaNagini"
print("shn" in txt)
print("thur" in txt)
#
txt = "KrishnaNagini"
if "shna" in txt:
    print("Yes")
else:
    print("No")
#check start and end
txt = "KrishnaNagini"
"KrishnaNagini".startswith ("Kri")
"KrishnaNagini".endswith ("ini")
#
#slicing
text = "KrishnaNagini"
print(text[0:5])
print(text[:5])
print(text[5:])
print(text[:])
print(text[-5:])
print(text[2:14:2])
print(text[::-1])
#
#modify string
txt = "KrishnaNagini"
name = "MANIKRUTHIKA"
username = "palanisai"
print(txt.upper())
print(name.lower())
print(username.title())
print(username.capitalize())
print(txt.swapcase())
#
#replace, split, join, find, count
txt = "Krishna Nagini"
print(txt.replace("Krishna", "Sai"))
txt = "Krishna Nagini, Palani Sai"
print(txt.split(","))
txt = "Krishna Nagini" ,"Palani Sai"
print("," .join(txt))
txt = "Krishna Nagini"
print(txt .find("na"))
print(txt.count("Krishna"))
#
#concatenation
a = "Hello"
b = "World"
c = "Python"
d = a + " " + b + " " + c
print(d)
#
a = "Hello"
a += "World"
a += "Python"
print(a)
#f- string
name = "KrishnaNagini"
course = "Python"
result = f"Hello {name}, this call is regarding {course}"
print(result)
# joining
name = ["Rani", "Krishna", "Nagini"]
result = "".join(name)
print(result)
#

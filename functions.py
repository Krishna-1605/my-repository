def my_name():
    print("My name is ")
my_name()

#parameters, arguments
def my_function(Surname):
    print("My name is ",Surname)
my_function("Krishna")
my_function("Nagini")
my_function("Palani")
#
def my_function(a,b):
    return a+b
print(my_function(4,6))
#
def my_function(animal, name):
    print("I have a",animal)
    print("My", animal  +"name is ",name)
my_function("dog","Jimmy")
#
def my_name(name, age, college):
    print("My name is", name, "my age is", age, "and my college is", college)
my_name("Krishna", age = 24, college = "KLU")
#default
def greet_user( name, greeting = "Hello"):
    return greeting +" "+name
greeting1 = greet_user("BOB")
greeting2 = greet_user("Jimmy", "Hi")
print(greeting1)
print(greeting2)

# *args
def my_names(*args):
    print("my surname is ", args[0])
my_names("Rani", "Kothuri", "Mantha", "Ayyagari")
#
def my_addition(*args):
    total = sum(args)
    print("total is ", total)
my_addition(20,40,80)
# **kwargs
def names(**kwargs):
    print("my name is ", kwargs["name"])
    print("my age is ", kwargs["age"])
names(name = "Krishna", age = 27)
#
def example(name, surname, *args, **kwargs):
    print("name")
    print("surname")
    print("args =", args)
    print("kwargs =", kwargs)

example("Krishna", "Rani", 3, 4, husband="Palani", age=20)
#global scope
a = 5
b = 13
sum = a+b
def my_function():
    print("sum inside is ", sum)
my_function()
print("sum outside is ", sum)
#local scope
def my_function(a, b):
    sum =  a+b
    print("sum inside is ", sum)
my_function(5,13)
#global keyword
a = 5
b = 11
sum = a+b
def my_function():
    global b
    b = 17
    print("sum inside is ", a + b)
my_function()
print("sum outside is ", a + b)

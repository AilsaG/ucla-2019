def doNothing():
    pass
def makeAString():
    return "Hurray!"
def sayHello():
    print("Hello")
    return "Hello"
def sayHello2():   #with a variable
    my_string_variable = "Hello"
    print(my_string_variable)
    return my_string_variable
def sayMyString(s):
    print(s)

sayHello()
a_variable = makeAString()
doNothing()
sayMyString("this is MyString.")
a_variable = sayHello()
print(a_variable)
sayMyString(sayHello2)
sayMyString(sayHello)
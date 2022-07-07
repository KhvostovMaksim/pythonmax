#hello
print("hello, world")

#value
print("value1","value2")

#name
name = "Maksim"
print(name)

#hello,name
name = input("What is your name?")
print("Hello,",name)

#calculator
x = float(input("First number:"))
y = float(input("Second number:"))
Operation = input("operation:")
result = None
if operation == "+":
    result = x+y
elif operation == "-":
    result = x-y
elif operation == "*":
    result = x*y
elif operation == "/":
    result = x/y
else:
    print("Unsupported operation")
if result is not None:
    print("Result:", result)
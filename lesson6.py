#docstrings
def function():
    """example function

    some long definition.
    """
    print("function called")

function()
help(function)

print(function.__doc__)


#radix_change
number=int(input("enter a number: "))

print("binary:", bin(number))
print("octal:", oct(number))
print("hexadecinal:", hex(number))


#reversed_example
for i in reversed("asdf")
    print(i)


#min_max
a=float(input("A= "))
b=float(input("B= "))
c=float(input("C= "))

print("MIN:", min(a, b, c))
print("MAX:", max(a, b, c))


#nested_functions
def outer_function():
    def inner_function():
        print("inner function")
    print("outer function")
    inner_function()

outer_function()



#scoping_example1
def function():
    print()

var="global variable"
function()


#factorial
def nonrecursive_factorial(n):
    result=1
    for multiplier in range(2, n +1):
        result *= multiplier
    return result
print(nonrecursive_factorial(5))



#fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

for i in range(1, 100:
    print(fib(i))

#hanoi_towers
def hanoi(n, a, b, c):
    if n!=0:
        hanoi(n-1, a, c, b
        print("Transfer a ring from", a, "to", c)
        hanoi(n-1, b, a, c)

hanoi(8, 'A', 'B', 'C')

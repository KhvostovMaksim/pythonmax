#int
print("int")
number = 123412341
print(number)
string = "123412341"
number = int(string)
print(number+5)

#bools
print()
print("bools")
bool1 = True
bool2 = False
print(bool1)
print(bool2)

#floats
print()
print('Floats')
a=5.3
b=3.17823
print(a+b)

#dynamicTYPING
print()
print("dynamictyping")
var = 'i am a string'
print(var)
print(type(var))
print ()
var=42
print(var)
print(type(var))
print()
a=5
b=5
print(a+b)

#ariphemitic_operations
print()
print('ariphemitic_operations')
x=2
y=8

result=x+y
print(result)# or print(x+y)
print(x+3)
print(x-y)

print()
print(x*y)
print(x / y)
print(x // y)
print(x % y)

print()

print(x ** y)
print(x ** 0.5)
print(pow(x,y))

print()

z = -2
print(abs(z))
print(z ** 2)

print()

print(3.2 * 0.8 - 2 * 5 - 3 ** 3)

print()

number = 3.26
print(round(number), round(number,1))

#math_operations
import math
print()
print('math_operations')

x=-3.265

print('trunc(x)=',math.trunc(x))
print('floor(x)=',math.floor(x))
print('ceil(x)=',math.ceil(x))

print(math.pi)
print(math.e)
print(math.sin(math.pi/4))
print(1/math.sqrt(2))


#strings
string1='string'
string2='string'

print(string1, string2)
string='first line of text.\n'\
       'Second line of text.'
print(string)


multiline_string ='''
Lesson2. Variables and data types
Some data types explained in this lesson:
-int
-bool
-float
-complex
-str
'''
print(multiline_string)


#print_examples
print(2, 3, 5, sep=', ')
print('he', 'llo', sep='')

print(1, end=' ')
print(2, end='\n\n')
print('he', end='')
print('llo')


#input_example
string=input('Enter a string')
print('You have entered"{}"'.format(string))

print('Press enter to continue...')
input()

n=int(input('First number:'))
m=int(input('Second number:'))
print('{}+{}={}'.format(n, m, n+m))
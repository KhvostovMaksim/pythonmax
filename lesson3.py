#simple_if_example
number=int(input('enter  a number:'))
if number>5:
    print('This number is greater than five.')


#if_else
x=float(input('x= '))
if x > 0:
        y=x ** 0.5
else:
        y=x**2
print(y)

#nested_if
x=int(input('x= '))

if 0<x<7:
    print('value is in range, let`s continue')
    y=2*x-5
    if y<0:
        print('y is negative')
    elif y>0:
            print('y is positive')
    else:
            print('y=0')


#elif_switch
print('''Menu:
1. File
2. View
3. Exit
''')

choice=int(input('enter your choice:'))
if choice ==1:
    print('you have selected "file" menu')
elif choice ==2:
    print('you have selected "view" menu')
elif choice ==3:
    print('stopping')
else:
    print('incorrect choice')

#condition
is_ready=true
print("ready" if is_ready else "not ready yet")

#truth_value_testing
number=int(input('Enter an integer:'))
if number:
     print(' The number is not zero')
else:
    print('The number is zero')



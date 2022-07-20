#example1
def hello():
    print('hello, world')
    print("(this text gets printed from a function")
    print()

hello()
hello()


#example2
def print_numbers(limit):
    for i in range(limit):
        print(i)

print_numbers(5)
print()
print_numbers(8)


#example3
def add_numbers(first, second):
    print('add numbers called with', first, second)
    return first + second

add_numbers(9,10)
result=add_numbers(2,3)-add_numbers(1,2)
print(result)

#example4
def function(x):
    if x<0:
        return x*2
    else:
        return x*3
def main():
    for i in range(-3,4):
        y=function(i)
        print('function(',i,'))=',y,sep='')

main()



#example5
def print_info(object_name, color, price):
    print('object:', object_name, sep='\t')
    print('color:', color, sep='\t')
    print('price:', price, sep='\t')
    print()

print_info('pen', 'blue', 1)

print_info(object_name='pen',
           color='blue',
           price=1)
print_info(price=5, object_name='cup', color='orange')

print_info('coffee', price=10, color='black', )

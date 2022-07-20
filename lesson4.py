#while_example1
response=""
while response!= "exit":
    response=input("type 'exit' to exit:")

#while_example2
n=1
while n<=3:
    print("n=", n)
    n +=1

#while_example3
number=0
while number <=0:
    number=int(input("enter a positive integer:"))

print("you have enetered", number)


#while_example4
print("all natural numbers:")

n=2
while True:
    print(n)
    n+=1

#break_example1
while True:
    print("enter 'exit' to exit loop")
    response=input('>')
    if response == "exit":
        break
print('loop has stopped')


#break_example2
name= None
while true:
    print('menu')
    print('1. enter name')
    print("2. Print greeting")
    print('3. Quit')

    response=input("please choose an action: ")

    print()

    if response =="1":
        name=input("enter your name")
    elif response == "2":
        if name:
            print("hello,", name, "!", sep="")
        else:
            print("i don`t know your name")
    elif response == "3":
        break
    else:
        print("incorrect input")

print()


#continue_example
number=0
while number <10:
    number +=1
    if number ==5:
        continue
    print('current number is', number)


#while_else
counter =5
while counter:
    print(counter)
    counter -=1
    print('loop is complete')
    print('counter=', counter)


#while_else_break
attemts_left=3
while attempts_left >0:
    attempts_left -=1
    password=input("enter your password"
                    "(you have {} attempts left) ".format(attemts_left+1))
    if password=="98eaxc":
        print('access granted')
    break
else:
    print('access denied')



#for_else
for attempts_left in range(3, 0, -1):
    password=input("enter your password"
                    "(you have {} attempts left) ".format(attemts_left))
    if password=="98eaxc":
        print('access granted')
        break
else:
    print('access denied')



#nested_loops
for row in range(5):
    for column in range(30):
        print("*", end="")
    print()

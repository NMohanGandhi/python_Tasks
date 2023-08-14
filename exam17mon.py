 
#1. How to fetch an alternative elements from the given list, MyList=[1,10,2,20,3,30,4,40,5,50,6,60]

#The result should be [10,20,30,40,50,60]
'''
mylist=[1,10,2,20,3,30,4,40,5,50,6,60]
print(mylist[1::2])
'''
#2. Write a python program which accepts a sequence of comma-separated numbers from console and generate a list which contains every number.
'''
mylist='1,10,2,20,3,30,4,40,5,50,6,60'
y=mylist.split(',')
print(y)
'''
#3. Write a python program which will find all such numbers which are divisible by 7 but are not a multiple of 5, and those numbers are between 100 and 200 (both included).
'''
n=200
for x in range(100,n+1):
    if x%7==0 and x%5!=0:
        print('{} givin number is divisible by 7 and not divisible by 5'.format(x))
'''    
#4. Write a python program to generate a dictionary that contains (i, ii) such that is anintegral number between 1 and n (both included), and then the program should printthedictionary.
#Suppose the following input is supplied to the program:4 Then, the output should be
#:,1:1, 2: 4, 3:9, 4:16-

n=5
a=[]
for i in range(0,n):
    a.append(i*i)
d={}.fromkeys(a)
print(d)

#5.Our organization contains 1000 employees. All the names are stored in the list. Now Iwant check whether my name is stored or not in the list? What should I do?
'''
name=input('enter ur name: ')
if name in existed_list:
    print('{} is already in list'.format(name))
else:
    print('{} is not in the list'.format(name))
'''
#6. How can we create a new dictionary by using existing tuple object? Tuple1=(10,20,4,3,5) arayanThe result dict should be like dict1-(10:0,20,0,4,0,3:0,5)
'''
tuple1=(10,20,4,3,5)
n=0
for i in tuple1:
    print({i:n},end=',')
'''
#7. Define a python function that can accept two strings as input and print the stringwith maximum length in console. If two strings have the same length, then thefunctionshould print all strings line by line.
'''
n1=input('enter first word: ')
n2=input('enter second word: ')
if len(n1)==len(n2):
    print(n1)
    print(n2)
else:
    print('not match length')
'''
#8. Define a python function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
'''
n=eval(input('Enter Any NUmber: '))
if n%2==0:
    print('it is an even number')
else:
    print('it is an odd number')
'''
#9. Define a python function which can print a dictionary where the keys are numbers between1 and 3 (both included) and the values are square of keys.
'''
n=3
k=[]
i=[1,2,3]
for i in range(1,n+1):
    k.append(i*i)
for x in k:
    print('{}:{}'.format(i,k))
'''
#10. Define a python function which can print a dictionary where the keys are numbersbetween 1 and 20 (both included) and the values are square of keys.

#11. Define a python function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

#12. Define a python function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
'''
n=20
a=[]
for i in range(0,n+1):
    a.append(i*i)
print(a)
'''
#13. Define a python function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
'''
n=20
a=[]
for i in range(0,n+1):
    a.append(i*i)
print(a[0:5])
'''
#14. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a python program to print the first half values in one line and the last half values in one line.
'''
tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple[:4],end='\n')
print(tuple[5:])
'''
#15. Write a python program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

#16. Write a python program which accepts a string as input to print "yes" or "YES" or "Yes", otherwise print "No".
'''
x=input('enter word: ')
if x:
    print(x.capitalize(),end=' or ')
    print(x.upper(),end=' or ')
    print(x.lower())
else:
    print("no")
'''
#17. Write a python program which can map() to make a listelements in 1,2,3,4,5,6,7,8,9,10+. Narayana elements are square of

#18. Write a python program which can filter() to r number between 1 and 20 (both included), ke a list whose elements are even

#19. Write a python program which can map() to make a list whose elements are square of numbers between 1 and 20(both include)
















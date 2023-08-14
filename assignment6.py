#1. Write a program to generate all 5 divisibles from 10 to 50?
'''
a=[]
for num in range(10,50):
    if num%5==0:
        a.append(num)
print(a)
'''
#2. Write a program to generate all 10 divisibles from 100 to 10?
'''
a=[]
for i in range(100,9,-1):
    if i%10==0:
        a.append(i)
print(a)
'''
#3. Write a program to generate all odd numbers from 11 to 25?
'''
a=[]
for i in range(11,25):
    if i%2!=0:
        a.append(i)
print(a)
'''
#4. Write a program to generate all even numbers from -2 to -22?
'''
a=[]
for i in range(-2,-22,-1):
    if i%2==0:
        a.append(i)
print(a)
'''
#5. Write a program to generate all numbers from -3 to 5?
'''
for i in range(-3,5):
    print(i)
'''
#6. Write a program to generate all 7 divisibles from -21 to 21?
'''
a=[]
for i in range(-21,21):
    if i%7==0:
        a.append(i)
print(a)
'''
#7. Write a program to generate all numbers from 1 to 10 except 2 and 6?
'''
a=[]
for i in range(1,10):
    if i!=2 and i!=6:
        a.append(i)
print(a)
'''
#8. Write a program to generate all numbers from 15 to 1 except 3,6,9 and 12?
'''
a=[]
for i in range(15,1,-1):
    if i!=3 and i!=6 and i!=9 and i!=12:
        a.append(i)
print(a)
'''
#9. Write a program to generate all numbers from -2 to 2 except -1 and 1?
'''
a=[]
for i in range(-2,2):
    if i!=-1 and i!=1:
        a.append(i)
print(a)
'''
#10. Write a program to generate all 3 divisibles from 15 to -15 except even numbers?
'''
a=[]
b=[]
for i in range(15,-15,-1):
    if i%3==0:
        a.append(i)
for i in a:
    if i%2!=0:
        b.append(i)
print(b)
'''

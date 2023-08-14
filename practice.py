''''marks=eval(input('enter your marks: '))
if marks>35:
    print('hellow student')
    print('ur pass in the exam')
    print('congratulation')
'''

'''
n=eval(input('enter any number: '))
if n%2==0:
    print(n,' is an even number')
'''



'''
name=eval(input('enter any name: '))
age=eval(input('enter any number: '))
if age>=18:
    print('helo {} your {} years old'.format(name,age))
    print('ur eligibe to vote')
    
          
enter any name: 'hari'
enter any number: 25
helo hari your 25 years old
ur eligibe to vote
'''


'''
marks=eval(input('enter any marks: '))
if marks>=35:
    print('hellow student')
    print('ur pass in the exam')
    print('congratulation')
else:
    print('you failed to the exam')
    print('better time next')
print('thank you for using www.nth.com')
      
'''



'''
n=eval(input('enter any number: '))
if n%2==0:
    print('{}  as an even number'.format(n))
else:
    print('{} is an odd number'.format(n))

    
'''




'''

options=''1.addition
           2.substraction
           3.multiplication
           4.division
           ''
option=eval(input('plese select any option: '))
if option >=1 and option <=4:
    n1=eval(input('enter first number: '))
    n2=eval(input('enter second number: '))
if option==1:
    n=n1+n2
    print('the addition of {} and {} is {}'.format(n1,n2,n))
elif option==2:
    n=n1-n2
    print('the substraction of {} and {] is {}'.format(n1,n2,n))
elif option==3:
    n=n1*n2
    print('the multiplication of {} and {} is {}'.format(n1,n2,n))
elif option==4:
    n=-n1%n2
    print('the division of {} and {} is {}'.format(n1,n2,n))
else:
    print('plese chosse either 1 or 2 or 3 or 4 only')

    
'''

'1'


'''



team=['kohil','dhoni','sachin','surya']
pname=eval(input("enter a player name: "))
if pname not in team:
    team.append(pname)
    print(team)
else:
    print('{} is available in team{}'.format(pname,team))


  '''

'7'
'''


name=input('enter your  name:')
gender=input('enter your gender: ')
if gender=='male' or 'female':
        age=eval(input('enter your age: '))
        if gender=='male' and age>30:
            print('you ready to marry')
        elif gender=='female' and age>25:
            print('you ready to marry')
else:
    print('pls enter correct age')
    
'''




'3'

'''


n=eval(input('enter any number: '))
if n%10==0:
    print('{} is divisible by 10'.format(n))
else:
    print('{} is not divisible by 10'.format(n))
'''

'4'

'''

name=eval(input('enter any number: '))
if type(name)==int:
    print('{} is an integer number'.format(name))
elif type(name)==float:
    print('{} is an flot number'.format(name))
elif type(name)==bool:
    print('{} is an boolian number'.format(name))
elif type(name)==str:
    print('{} is an string '.format(name))
else:
    print('not number')
'''
'8'

'''
n=eval(input('enter any number: '))
if n>=0 and n<=5:
    print('you are an infant of () years'.format(n))
elif n>=6 and n<=16:
    print('you are school going kid of {} years'.format(n))
elif n>=17 and n<=22:
    print('you are college going kid of {} years'.format(n))
elif n>=23 and n<=30:
    print('you need to settle in life and get marry of {} years'.format(n))
elif n>=31 and n<=45:
    print('yor need to work and earn money of {} years' .format(n))
elif n>=46 and n<=60:
    print('you need to do bussiness of {} years'.format(n))
elif n>=61:
    print('you need to take rest of {} years'.format(n))
else:
    print('invalid age,please check once')

'''
'''
10
'''

'''

n=eval(input('enter any number: '))
if n>=1 and n<=10:
    if n%2==0:
        print('you have enter even number')
    elif n%2!=0:
        print('you have entered odd number')
else:
    print('please enter any number between 1 and 10')

'''


'5'

'''
n=eval(input('enter name : '))
n=n.capitalize()
if n=='hari':
    print('{} string is available '.format(n))
elif n=='jamal':
    print('{} string is available '.format(n))
elif n=='krishna':
    print('{} string is available '.format(n))
else:
    print('string is not available ')
print(type(n))


'''


'6'



'''


n=eval(input('enter any week : '))
if n=='monday' or 'tuesday' or 'wednesday' or 'thursday':
    print('you can  wear school uniform on {}'.format(n))
elif n=='friday':
    print('you can wear civil dress on {}'.format(n))
elif n=='saturday':
    print('you can wear white and white on {}'.format(n))
elif n=='sunday':
    print('its your choice on {}'.format(n))
else:
    print('not any wear')




'''


'''


name='Python Narayana Tech House Hydrabed'
i=[word[0] for word in name.split()]
print(i)

'''

'''

names=['python','django','ui','mysql']
print([len(word) for word in names])
'''

'''


names=['akhil','python','Ice','django']
new_names=[]
vow='aeiouAEIOU'
for i in names:
    if i[0] in vow:
        new_names.append(i)
print(new_names)



'''




'''
names=['python','django','ui','mysql']
new_name=[]
for name in names:
    if len(name)==6:
        new_name.append(name)
print(new_name)

'''



'''



names=['narayana','python','akhil','akhila','priya']
new_name=[]
for name in names:
    if name.endswith('a'):
        new_name.append(name)
print(new_name)


'''

'''
names=['python','django','mysql']
new_name=[]
for name in names:
    name=name[::-1]
    new_name.append(name)
print(new_name)

'''


'''
names=('mom','python','malayalam','madam','django')
new_name=[]
for name in names:
    if name==name[::-1]:
        new_name.append(name)
print(new_name)




'''


'doubt'


'''

name=input('enter any name: ')
gender=input('enter your gender: ')
if gender=='him' or 'her':
    print('you learnind upddated skill')
else:
   print('you learn python')



'''

'''

n=eval(input('enter any number: '))
if n>10 and n<50:
    if n%5==0:
        print('{} divisible by 5'.format(n))
    elif n%5!=0:
       print('{} is not divisible by 5'.format(n)) 
else:
    print('u enter out of range')

'''


'''
lower=int(input('enter any number: '))
upper=int(input('enter any number: '))
n=int(input('enter number is divisible by: '))
for i in range(lower,upper+1):
    if (i%n==0):
        print('{} is divisible by {}'.format(i,n))


'''

'''
n1=100
n2=10
for i in range(n1+1,n2):
    if (i%10==0):
        print(i)

    
'''
#file handling

#wap to read the data from the file?
'''
x=open('read.txt')
y=x.read()
print(y)
'''

#wap to read first line from the file?
'''
x=open('read.txt')
y=x.readline()
print(y)


print(open('read.txt').readline())
'''
#3.wap to read the last line from the file?
'''
x=open('read.txt')
y=x.readlines()[-1]
print(y)

print(open('read.txt').readlines()[-1])
'''
#4.wap to read the 2nd line from the file?
'''
x=open('read.txt')
y=x.readlines()[1]
print(y)

print(open('read.txt').readlines()[1])
'''
#5.wap to read all the line from the file?
'''
x=open('read.txt')
y=x.read()
print(y)

print(open('read.txt').read())
'''
#6.wap to read the first word from the secondline?
'''
x=open('read.txt')
y=x.readlines()[1]
y=y.split(',')
print(y[0])

print(open('read.txt').readlines()[1].split(',')[0])
'''
#7.wap to read the last word from the last line?
'''
x=open('read.txt')
y=x.readlines()[-1]
h=y.split(',')[-1]
print(h)

print(open('read.txt').readlines()[-1].split(',')[-1])
'''
#8.wap to read the first character from second word in the third line?
'''
x=open('read.txt')
y=x.readlines()[2]
h=y.split(',')[1][0]
print(h)

print(open('read.txt').readlines()[2].split(',')[1][0])
'''
#9.wap to read lost word from the third line?
'''
x=open('read.txt')
y=x.readlines()[2]
h=y.split(',')[-1]
print(h)

print(open('read.txt').readlines()[2].split(',')[-1])
'''
#10.wap to read all the word which stat with vowel?
'''
x=open('read.txt')
y=x.read()
h=y.split(',')
for i in h:
    if i[0]in 'aeiouAEIOU':
        print(i)

print([i for i in open('read.txt').read().split(',') if i[0] in 'aeiouAEIOU'])
'''
#11.wap read all the words which has only 4character?
'''
x=open('read.txt')
y=x.read()
c=y.split(',')
for i in c:
    if len(i)==4:
        print(i)

print([i for i in open('read.txt').read().split(',') if len(i)==4])

'''
#12.wap to read all the word which stat with consonent?
'''
x=open('read.txt')
y=x.read()
h=y.split(',')
for i in h:
    if i[0] not in 'aeiouAEIOU':
        print(i)

print([i for i in open('read.txt').read().split(',') if i[0] not in 'aeiouAEIOU'])
'''

#13.wap to read the all word contains the u character?
'''
x=open('read.txt')
y=x.read().split(',')
for i in y:
    if 'u' in i:
        print(i)
print([i for i in open('read.txt').read().split(',') if 'u' in i])

'''
#14.wap to read the first word from each line?
'''
x=open('read.txt')
y=x.readlines()
for i in y:
    print(i.split(',')[0])

print ([i.split(',')[0] for i in  open('read.txt').readlines()])
'''
#15.wap to read the last word from each line?
'''
x=open('read.txt')
y=x.readlines()
for i in y:
    print(i.split(',')[-1])

print ([i.split(',')[-1] for i in  open('read.txt').readlines()])
'''

#16.wap to read the last character of third word in second line?
'''
x=open('read.txt')
y=x.readlines()[1]
x=y.split(',')[2][-1]
print(x)
    
print([ open('read.txt').readlines()[1].split(',')[2][-1]])
'''
#17.wap to read the biggest word in the file?
'''
x=open('read.txt')
y=x.read().split(',')
lst=[]
for i in y:
    lst.append(len(i))
for i in y:
    if len(i)==max(lst):
        print(i)


print([i for i in open('read.txt').read().split(',') if len(i)==max(len(i) for i in open('read.txt').read().split(','))])
'''
#18.wap to read the shortest word in the file?
'''
x=open('read.txt')
y=x.read().split(',')
lst=[]
for i in y:
    lst.append(len(i))
for i in y:
    if len(i)==min(lst):
        print(i)


        
print([i for i in open('read.txt').read().split(',') if len(i)==min(len(i) for i in open('read.txt').read().split(','))])
'''
#19.wap to count number of employees with name tarun?
'''
x=open('read.txt')
y=x.read().split(',')
count=0
for i in y:
    if i=='Tarun':
        count=count+1
print(count)
'''
'''
print([i for i in open('read.txt').read().split(',')])
'''

#20.wap to count total number of words in the files?
'''
x=open('read.txt')
y=x.read().split(',')
count=0
for i in y:
    count=count+1
print(count)

print([len ( open('read.txt').read().split(','))])
'''
#21wap count  tatol no.of characters in the file (excludind coma and /n)?
'''
x=open('read.txt').read()
count=0
for i in x:
    if i!=',' and i!='/n':
        count=count+1
print(count)

print(len([i for i in open('read.txt').read() if i !=',' and i!='/n']))
'''
#22.wap to count total no.of commas in the file?
'''
x=open('read.txt').read()
count=0
for i in x:
    if i==',':
        count=count+1
print(count)

print(len([i for i in open('read.txt').read() if i==',']))
'''
#23.wap to count total no.of '/n' in the file?
'''
x=open('read.txt').read()
count=0
for i in x:
    if i=='\n':
        count=count+1
print(count)

print(len([i for i in open('read.txt').read() if i=='\n']))
'''
#24.wap to count all the employes of 'tcs'?
'''
x=open('read.txt').readlines()[0]
y=x.split(',')
print(y[1::])

print([open('read.txt').readlines()[0].split(',')[1::]])
'''
#25.wap to read the company name of ganga employee?
'''
x=open('read.txt').readlines()[1].split(',')[0]
print(x)

print([open('read.txt').readlines()[1].split(',')[0]])
'''
#26. wap to read the name which are repeted
'''
open('read.txt')
'''
#27.wap to read all words which are in uppercase?
'''
x=open('read.txt').read()
y=x.split(',')
lst=[]
for i in y:
    if i.isupper():
        lst.append(i)
        print(lst)

print([i for i in open('read.txt').read().split(',') if i.isupper()])
'''
#28.wap to count employee names who name stat with 's' chararcter?
'''
x=open('read.txt').readlines()
a=[]
for i in x:
    i=i.split(',')[1:]
    if i=='s':
        a.append(i)
    print(a)
'''
#29.wap to read company name which has less no of employess?
'''
x=open('read.txt').readlines()
k=[]
for i in x:
    y=i.split(',')[1:]
    k.append(len(y))
for i in x:
    len(y)==min(k)
print(y)
'''


#30.wap to count all ovels in files?
'''

x=input('enter any number: ')


if int(x[0])**4+int(x[1])**4+int(x[2])**4+int(x[3])**4==int(x):
    print('{} its armstorng number'.format(x))
else:
    print('{} its not armstrong number'.format(x))

'''

#Registration
'''
existing_users = {'hari':'hari232', 'ganga':'ganga@310', 'muni':'@1334'}
while True:
    user = input('Enter user name: ')
    if user in existing_users:
        print('{} is already existed,please enter new user name'.format(user))
        continue
    else:
        pwd = input("Enter your password: ")
        print('Rregistration completed successfully...')
        existing_users[user]=pwd
        #print(existing_users)
    break
'''
import string
import re
while True:
    Name=input('Enter Any ID: ')
    if string.punctuation('^_@',Name):
        if string.printable('^A-ZName[0]^\d',Name):
            if re.fullmatch('\S',Name):
                print('u enter wrong user id')
                countinue
    
    
             



































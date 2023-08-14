#1. Write a program to check whether a specific player is available in team or not, if not available then append in the team
'''
team = ['Kohli', 'Dhoni', 'Sachin', 'Surya']
pname=input('enter ur name: ')
if 'pname' in team:
    print('{} is available in {}',format(pname,team))
else:
    team.append(pname)
print(team)
'''
#2. Write a program to check which language is learning by student.If he is learning Python
#then tell him/her that he/she is learning updated skill otherwise tell him/her to learn python




#3. Write a program to check whether the given number is divisible by 10 or not?
'''
n=eval(input('enter any number: '))
if n%10==0:
    print('given number is divible by 10')
else:
    print('given number is not divisible by 10')
'''

#4. Write a program to check what type of value is given by user?
'''
n=eval(input('enter any number: '))
if type(n)==int:
    print('n is an integer number')
elif type(n)==str:
    print('n is an string ')
elif type(n)==bool:
    print('n is an bool value ')
elif type(n)==complex:
    print('n is an complex number ')
else:
    print('n is an invalid')
'''
#5. Write a program to check whether a given string is available or not in the string?
'''
n=eval(input("enter any value: "))
n=n.capitalize()
if n=='hari':
    print('n is avalable in string')
elif n=='jamal':
    print('n is availble in string')
else:
    print('n is not available in string')
'''  
#6. Write a program for following requirement:
'''
Monday, Tuesday, Wednesday, Thursday --> You can wear School Uniform
 Friday --> You can wear Civil Dress
 Saturday --> You can wear white and white
 Sunday --> Its your choice
''' 



#7. Write a program for following requirement:
'''
you need to ask user to enter name, gender.
if gender is male then ask him to enter age. if age is more then 30 then ask him to marry.
if gender is female then ask her to enter age. if age is more then 25 then ask her to marry.
'''
'''
name=input('enter your name: ')
gender=input('enter ur gender: ')
if gender=='male' or 'female':
    age=eval(input('enter ur age: '))
elif gender=='female' and age>25:
    print('you ready to marry')
elif gender=='male' and age>30:
    print('you ready to marry')
else:
    print('pls enter correct age')
'''
#8. Write a program for following requirement:
'''
0 to 5 --> You are an Infant
6 to 16 --> You are school going kid
17 to 22 --> You are college going kid 
23 to 30 --> You need to settle in life and get marry
31 to 45 --> You need to work and earn money 
46 to 60 --> You need to do business 
61 and above --> You need to take rest.
below 0 --> Invalid Age, please check once 
'''
#9. Write a Python Program to find BMI(Body Mass Index)?
'''
Take height (in cms) and weight (in kgs) from user.
Calculate BMI by using height and weight.
Note: Convert cms into metres
BMI = Weight(in kg) / Height*Height(in metre)
if BMI between 0 and 18.5, display "Underweight",
if BMI between 18.5 and 24.9, display "Normal Weight"
if BMI between 25.0 and 29.9, display "Pre-Obesity"
if BMI between 30.0 and 40.0, display "Obesity"
if BMI between 40. and above, display "Extremly Obesity".
'''
#10. Write a Python Program to take any one number from user, that number must be between 1 and 10.
'''
If the number is below 1 or more than 10 then display "Please enter any number between 1 and 
10".
If the number between 1 and 10 then check it whether the number divisible by 2 or not.
If the number divisible by 2 then display "You have entered even number."
If the number is not divisible by 2 then display "You have entered odd number."
'''





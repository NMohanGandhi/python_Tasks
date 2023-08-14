#1. Write a pattern to get employee name who is working in TCS.
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('TCS',i):
        print([re.findall('[A-Z][a-z]{1,2}. [a-zA-Z ]{1,}',i)])
'''
#2. Write a pattern to get employee name whose email id contains django?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('django',i):
        print([re.findall('[A-Z][a-z]{1,2}. [a-zA-Z ]{1,}',i)])
'''
#3. Write a pattern to get employee name who born before 1990?    
'''
x=open('abcd.txt')
y=x.readlines()
import re
lst=[]
for i in y:
    lst.extend([i.replace('-','')for i in re.findall('-\d{4}',i)])
print(lst)
j=0
for i in y: 
    if lst[j] in lst and int(lst[j])<1990:
        print(re.findall('[A-Z][a-z]{1,2}. [a-zA-Z ]{1,}',i))
    j=j+1
'''
#4. Write a pattern to get employee name who belongs to Andhra Pradesh?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('AP',i):
        print([re.findall('[A-Z][a-z]{1,2}. [a-zA-Z ]{1,}',i)])
'''
#5. Write a pattern to get employee name whose mobile number not starts with 90?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('[90]\d{8}',i) not in i :
        print([re.findall('[A-Z][a-z]{1,2}. [a-zA-Z ]{1,}',i)])
'''      
#6. Write a pattern to get employee name who contains orkut account?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('orkut',i):
        print([re.findall('[A-Z][a-z]{1,2}. [a-zA-Z ]{1,}',i)])

'''

#7. Write a pattern to get employee name who born in March Month?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('\d{2}-[03]-\d{4}',i):
        print(i)
'''
#8. Write a pattern to get Company Name of Mr. Rajesh?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('Mr. Rajesh',i):
        print([i.replace(' Company','')for i in re.findall('[a-zA-Z]{1,} Company',i)])

'''
#9. Write a pattern to get Mobile Number of Mrs. Sravya?
'''
x=open('abcd.txt')
y=x.readlines()
im port re
for i in y:
    if re.findall('Mrs.Sravya',i):
        print([re.findall('[6-9]\d{9}',i)])
'''

#10. Write a pattern to get Company Names of all male employees?
'''
x=open('abcd.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('[A-Z][a-z]. [a-zA-Z ]{1,}',i):
        print([i.replace(' Company','')for i in re.findall('[a-zA-Z]{1,} Company',i)])
'''
#11. Write a pattern to count total number of employees working in TCS?
'''
x=open('abcd.txt')
y=x.readlines()
import re
a=[]
for i in y:
    if 'TCS' in i:
        a.append(re.findall('[A-Z][a-z]. [a-zA-Z ]{1,}',i))
print(len(a))
'''
#12. Write a pattern to count total number of female employees?
'''
x=open('abcd.txt')
y=x.readlines()
import re
a=[]
for i in y:
    a.append(re.findall('[A-Z][a-z]{2}. [a-zA-Z ]{1,}',i))
print(len(a))

'''
#13. Write a pattern to get date of birth of youngest employee?
'''
x=open('abcd.txt')
y=x.read()
import re
print(max(re.findall('\d{1,2}-\d{1,2}-\d{4}',y)))
'''
#14. Write a pattern to get the age of Mrs. Sonia?
'''
import datetime as dt
today = dt.datetime.today()
current_year=today.year
x=open('abcd.txt')
y=x.readlines()
import re
print([current_year-int(i.replace('-','')) for i in y if 'Sonia' in i for i in re.findall('-\d{4}',i)])
'''
#15. Write a pattern to get the age of oldest employee?
'''
x=open('abcd.txt').read()
import datetime as dt
today = dt.datetime.today()
current_year=today.year
import re
print([current_year- int(min(i.replace('-','')for i in re.findall('-\d{4}',x)))])
'''


#dates & year & times















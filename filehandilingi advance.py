#1. Write a program to fetch all Employees names?
'''
x=open('hari2.txt')
y=x.read()
import re
print([i.replace('.','') for i in re.findall('[M.][A-Z]{1}[a-z]{1,}',y)])
'''
#2. Write a program to fetch all mobile numbers from file?
'''
x=open('hari2.txt')
y=x.read()
import re
print([re.findall('[6-9]\d{9}',y)])
'''
#3. Write a program to fetch all PAN Numbers from file?
'''
x=open('hari2.txt')
y=x.read()
import re
print([re.findall('[A-Z]{5}\d{4}[A-Z]',y)])
'''
#4. Write a program to fetch all email ids from file?
'''
x=open('hari2.txt')
y=x.read()
import re
print(re.findall('[a-z\d_@a-z]*.com',y))
'''
#5. Write a program to fetch all registration numbers from file?
'''
x=open('hari2.txt')
y=x.read()
import re
print(re.findall('[A-Z]{2}\s?\d{2}\s?[A-z]{1,2}\s?\d{4}',y))
'''
#6. Write a program to fetch all company names?
'''
x=open('hari2.txt')
y=x.read()
import re
print([i.replace(' Company','')for i in re.findall('[A-Za-z]{1,} Company',y)])
'''
#7. Write a program to fetch all date of births?
'''
x=open('hari2.txt')
y=x.read()
import re
print([re.findall('\d{1,2}/\d{1,2}/\d{1,}',y)])
'''
#8. Write a program to fetch company name Mr. Sai?
'''
import re
x=open('hari2.txt')
y=x.readlines()
for i in y:
    if 'Mr.Sai' in re.findall('[A-Za-z]{1,}.[A-Za-z]{1,}',i):
        print([i.replace(' Company','') for i in re.findall('[A-Za-z]{1,} Company',i)])

print([i.replace(' Company','') for i in open('hari2.txt').readlines()if 'Mr.Sai' in i for i in re.findall('[A-Za-z]{1,} Company',i)])
'''
#9. Write a program to fetch email id of Mr. Rohan?
'''
import re
x=open('hari2.txt')
y=x.readlines()
for i in y:
    if 'Mr. Rohan' in re.findall('[A-Za-z]{1,}.[A-Za-z]{1,}',i):
        
        print([re.findall('[a-z\d_@a-z]*.com',i)])

print([i for i in open('hari2.txt').readlines() if "Mr.Rohan" in i for i in re.findall('[a-z\d_.@a-z]*.com',i)])
'''
#10. Write a program to fetch employee name who is using 9090909090?
'''
x=open('hari2.txt')
y=x.readlines()
for i in y:
    if '9090909090' in i:
        import re
        print([i.replace('.','')for i in re.findall('[M.][A-Z]{1}[A-Za-z]{1,}',i)])

print([i.replace('.','')for i in open('hari2.txt').readlines() if '9090909090' in i for i in re.findall('[M.][A-Z]{1}[A-Za-z]{1,}',i)])
'''
#11. Write a program to fetch PAN number of Mrs. Satya?
'''
x=open('hari2.txt')
y=x.readlines()
for i in y:
    if 'Satya' in i:
        import re
        print([re.findall('[A-Z]{5}\d{4}[A-Z]',i)])

print([i for i in open('hari2.txt').readlines() if 'Satya' in i for i in re.findall('[A-Z]{5}\d{4}[A-Z]',i)])
'''
#12. Write a program to fetch contact number of both Nani and Satya?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if 'Mrs.Satya' in i and 'Mr.Nani' in i  :
        print(re.findall('[6-9]\d{9}',i))
'''
#13. Write a program to fetch emp names of Infosys and TCS companies?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if 'Infosys' in i or 'TCS' in i  :
        print([i.replace('.','') for i in re.findall('[M.][A-Z]{1}[a-z]{1,}',i)])
'''
#14. Write a program to fetch DOB of TCS Employee?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if 'TCS' in i:
        print(re.findall('\d{2}/\d{2}/\d{1,}',i))
'''
#15. Write a program to fetch birth year of Mr. Nani?           
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if 'Mr.Nani' in i:
        print(re.findall('\d{1,2}/\d{2}/\d{1,}',i))
'''
#16. Write a program to fetch the emp name whose mobile number starts with 8?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('[8]\d{9}',i) :
        print([i.replace('.','') for i in re.findall('[M.][A-Z]{1}[a-z]{1,}',i)])
'''
#17. Write a program to fetch odisha emp name?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('[OD]\s?\d{2}\s?[A-Za-z]{1,2}\s?\d{4}',i):
        print([i.replace('.','') for i in re.findall('[M.][A-Z]{1}[a-z]{1,}',i)])
'''
#18. Write a program to fetch youngest employee name?
'''
import re
x = open('hari2.txt','r').readlines()
lst = []
for  i in x:
    lst.extend([i.replace('/','')for i in re.findall('/\d{4}',i)])
for i in x:
    if max(lst) in i:
        print(re.findall('[A-Z][a-z][s]?[.][A-Za-z]{1,}',i))
'''
        
        
#19. Write a program to fetch all Male Employees?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    for i in re.findall('[A-Z][a-z].[A-Z][a-z]{1,}',i):
        print(re.findall('[A-Z][a-z].[A-Z][a-z]{1,}',i))
'''
#20. Write a program to fetch total count of female employees?
'''
x=open('hari2.txt')
y=x.readlines()
import re
a=[]
for i in y:
    for i in re.findall('[A-Z][a-z]{2}.[A-Z][a-z]{1,}',i):
        print(len(re.findall('[A-Z][a-z]{2}.[A-Z][a-z]{1,}',i)))
'''
#21. Write a program to fetch all employees names who born in January?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('(\d{1,2}/[1]/\d{1,4})+',i):
        print([i.replace('.','') for i in re.findall('[M.][A-Z]{1}[a-z]{1,}',i)])
'''
#22. Write a program to fetch contact number of Telangana Employee?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if re.findall('[TS]\s?\d{2}\s?[A-Za-z]{1,2}\s?\d{4}',i):
        print([i.replace('.','') for i in re.findall('[6-9]\d{9}',i)])
'''
#23. Write a program to fetch Company Name and Mobile Number of Wipro Employee?
'''
x=open('hari2.txt')
y=x.readlines()
import re
for i in y:
    if 'Wipro' in i:
        print([re.findall('[6-9]\d{9}',i),re.findall('[A-Za-z]{1,} Company',i)])
'''      
   
#24. Write a program to fetch Emp name who born in leaf year?
'''
x=open('hari2.txt')
y=x.readlines()
lst=[]
import re
for i in y:
    lst.extend([i.replace('/','')for i in re.findall('/\d{4}',i)])
j=0
for i in y:
    if lst[j] in lst and int(j)%4==0:
        print(re.findall('[A-Z][a-z][s]?[.][A-Za-z]{1,}',i))
    j=j+1   
''' 


#25. Write a program to fetch all details of emp whose name not ends with vowel?
'''
x=open('hari2.txt')
y=x.readlines()
a=[]
import re
for i in y:
    if [i for a in re.findall('[A-Z][a-z]{1,2}.[A-Z][a-z]{1,}',i)if a[-1] not in 'aeiou']:
        print(i) 
'''

data='''Mr. Narayana Trainer is teaching Python Language

since 5 years in both online mode and offline mode,

He also teaches Java Language very rarely.

Python course fee 3000Rs and Java course fee 2000Rs.
Mr. Roshan Trainer is also teaching SAP Course and MSBI Course.
'''
'''
#1. Write a program to fetch Trainers Names?
import re
    
print([i.replace(' Trainer','')for i in re.findall('[A-Z][a-z]. [A-Za-z]{1,} Trainer',data)])
    

#2. Whats are the languages that Mr. Narayana teach?

import re

print([i.replace(' Language','')for i in re.findall('[A-Za-z]{1,} Language',data)])
        

#3. What are the mode that Mr Narayana teach?

import re

print([i.replace(' mode','')for i in re.findall('[A-Za-z]{1,} mode',data)])
        
        
#4. What are the fee structures of both Python and Java?

import re

print([i.replace('fee ','')for i in re.findall('fee \d{1,}[A-Za-z]{1,2}',data)])
#5. What are the courses that Mr. Roshan teach?

import re

print([i.replace(' Course','') for i in re.findall('[A-Za-z]{1,} Course',data)])

''' 
    

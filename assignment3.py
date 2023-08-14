employees={
    'emp1':{'name':'sai','salary':20000,'company':['TCS','Capgemini','infosis'],'htown':'hyd'},
    'emp2':{'name':'nani','salary':30000,'company':['Wipro','NTH'],'htown':'bangalore'},
    'emp3':{'name':'sathya','salary':40000,'company':['NTH','infosis','CTS'],'htown':'chennai'},
    'emp4':{'name':'rohit','salary':25000,'company':['infosis','TCS','defteam'],'htown':'pune'},
    'emp5':{'name':'mohan','salary':22000,'company':['NTH','HCL','deepcompute'],'htown':'hyd'},
    'emp6':{'name':'sanjay','salary':45000,'company':['wipro','infosis','defteam'],'htown':'mumbai'}}
 
 
#1.disply sai salary?
 
'''print(employees['emp1']['salary'])'''
 
#2.diplay nani home town?
 
'''print(employees['emp2']['htown'])'''
 
#3.disply emp name who is working in pune?
'''
for i in employees:
    if employees[i]['htown']=='pune':
        print(employees[i]['name'])
'''
 
#4.display all companies of sathya?
'''
print(employees['emp3']['company'])
'''
#5.to display all employees names who worked in tcs?
'''
for i in employees:                          
    if 'TCS' in employees[i]['company']:      
        print(employees[i]['name'])
 
'''
#6.disply   all employees names who did not work in infosis?
'''
for i in employees:
    if 'infosis' not in employees[i]['company']:
        print(employees[i]['name'])
'''
 
#7.disply all employees names?
'''
for i in employees:
    print(employees[i]['name'])
'''
#8.display the sum of all salaries?
'''
sum=0
for i in employees:
    sum=sum+employees[i]['salary']
print(sum)
'''
 
#9.to disply the latest company of rohit? 
'''
for i in employees:
    if employees [i]['name']=='rohit':
        print(employees[i]['company'][-1])
'''
#10.write a program to display total companies of satya?
'''
ename=input('enter ename: ')
sum=[]
for i in employees:
    if employees[i]['name']==ename:
        sum.extend(employees[i]['company'])
        print(len(sum))
'''
#11.write a program to display the employees name who is working in hcl?
'''
for i in employees:
    if 'HCL' in employees[i]['company']:
        print(employees[i]['name'])
'''
#12.wap to display the employes names who are working in hyd?
'''
for i in employees:
    if  employees[i]['htown']=='hyd':
        print(employees[i]['name'])
'''
#13.wap to display all employees whoes names starts with 's' character?
'''
for i in employees:
    if employees[i]['name'][0]=='s':
        print(employees[i]['name'])
'''
#14.wap to display all employees whoes name ends with vowels?
'''
for i in employees:
    v='aeiou'
    if employees[i]['name'][-1] in v:
        print(employees[i]['name'])
'''
#15.wap to display the employe name who worked only in two companies?


 
 
#20.display the name and salary of the bangaloor employee?
'''
for i in employees:
   if employees[i]['htown']=='bangalore':
        print(employees[i]['name'])
        print(employees[i]['salary'])             
'''

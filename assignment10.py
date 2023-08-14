

#1.wrp to fetch all data from the file?
'''
x=open('hari.txt')
y=x.read()
print(y)

print([open('hari.txt').read()])
'''
#wrp to read the first line from the file?
'''
x=open('hari.txt')
y=x.readlines()[0]
print(y)

print([open('hari.txt').readlines()[0]])
'''
#3.wap to read the last line from the file?
'''
x=open('hari.txt')
y=x.readlines()[-1]
print(y)

print([open('hari.txt').readlines()[-1]])
'''
#4.wap to read the 3rd line from the file?
'''
x=open('hari.txt')
y=x.readlines()[2]
print(y)

print([open('hari.txt').readlines()[2]])
'''
#5.wap to count total number of character in the file?
'''
a=[]
x=open('hari.txt')
y=x.read()
for i in y:
    a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').read()]))
'''
#6.wap to count total number of commas in the file?
'''
a=[]
x=open('hari.txt')
y=x.read()
for i in y:
    if i == ',':
        a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').read() if i==',']))
'''
#7. Write a program to count total number of words in the first line?
'''
a=[]
x=open('hari.txt')
y=x.readlines()[0].split(',')
for i in y:
    a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').readlines()[0].split(',')]))
'''
#8. Write a program to count total number of lines in the file?
'''
x=open('hari.txt')
y=x.readlines()
print(len(y))

print(len([i for i in open('hari.txt').readlines()]))
'''
#9. Write a program to count total number of 'Sai' name in the file?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i=='Sai':
        a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').read().split(',') if i=='Sai']))
'''
#10. Write a program to fetch the first word from each line in the file?
'''
x=open('hari.txt')
y=x.readlines()
for i in y:
    print(i.split(',')[0])

print([i.split(',')[0] for i in open('hari.txt').readlines()])

'''
#11. Write a program to fetch the last word from each line?
'''
x=open('hari.txt')
y=x.readlines()
for i in y:
    print(i.split(',')[-1])

print([i.split(',')[-1] for i in open('hari.txt').readlines()])
'''
#12. Write a program to fetch all words which starts with 'a' Character?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i[0]=='A':
        a.append(i)
print(a)

print([i for i in open('hari.txt').read().split(',') if i[0]=='A'])
'''
#13. Write a program to fetch all words which ends with an vowel?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i[-1] in 'AEIOUaeiou':
        a.append(i)
print(a)

print([i for i in open('hari.txt').read().split(',') if i[-1] in 'AEIOUaeiou'])
'''

#14. Write a program to fetch all words which has either 'a' or 'i' characters in the file?\
'''
a=[]
x=open('hari.txt')
y=x.read().replace('\n',',').split(',')
for i in y:
    if 'a' in i or 'i' in i:
        a.append(i)
print(a)

print([i for i in open('hari.txt').read().replace('\n',',').split(',') if 'a' in i or 'i' in i])
'''
#15. Write a program to fetch all words which contains only 5 characters in the file?
'''
a=[]
b=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    a.append(i)
for x in a:
    if len(x)==5:
        b.append(x)
print(b)

print([i for i in open('hari.txt').read().split(',') if len(i)==5])
'''
#16. Write a program to fetch all words which does not contains vowels except I in the file?  #@#doubt
'''
a=[]
x=open('hari.txt')
y=x.read().replace('\n',',').split(',')
for i in y:
    if 'aeiouAEIOU' not in i:
        a.append(i)
print(a)

'''
#17. Write a program to fetch all words which ends with uppercase character in the file?   #@#doubt
'''
x=open('hari.txt')
y=x.read().replace('\n',',').split(',')
for i in y:
    if i[-1]==i.upper()[-1]:
        print(i)

print([i for i in open('hari.txt').read().replace('\n',',').split(',') if i[-1]==i.upper()[-1]])
'''
#18. Write a program to count total number of characters in the file excluding commas and \ns?
'''
a=[]
x=open('hari.txt')
y=x.read()
for i in y:
    if i !=',' and i!='/n':
        a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').read() if i!=',' and i!='/n']))
'''
#19. Wrme a program to count total number of words in the entire file?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').read().split(',')]))
'''
#20 Write a program to fetch all even number words from from every line the file?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if len(i)%2==0:
        a.append(i)
print(a)

print([i for i in open('hari.txt').read().split(',') if len(i)%2==0])
'''
#21. Write a program to fetch all words which ends with 'bha' in the file?
'''
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i.endswith('bha')==True:
        print(i)

print([i for i in open('hari.txt').read().split(',') if i.endswith('bha')])
'''
        

#22. Write a program to display all TCS employees?
'''
x=open('hari.txt')
y=x.readlines()[0].split(',')
print(y[1::])

print([i for i in open('hari.txt').readlines()[0].split(',')])
'''
#23. Write a program to display the company name of Chinna Employee?
'''
x=open('hari.txt')
y=x.readlines()
for i in y:
    n=i.split(',')
    if 'Chinna' in n:
        print(n[0])
'''
#24. Write a program to fetch the 2nd from 3rd line in the file?
'''
x=open('hari.txt')
y=x.readlines()[2].split(',')
print(y[1])

print([open('hari.txt').readlines()[2].split(',')[1]])
'''
#25. Write a program to fetch the first character from each word in the 3rd line?
'''
x=open('hari.txt')
y=x.readlines()[2].split(',')
for i in y:
    print(i[0])

print([i[0] for i in open('hari.txt').readlines()[2].split(',')])
'''
#26. Write a program to fetch first and last character of each word in the last line?   
'''
a=[]
x=open('hari.txt')
y=x.readlines()[-1].split(',')
for i in y:
    a.append(i[0]+i[-1])
print(a)


print([i[0]+i[-1] for i in open('hari.txt').readlines()[-1].split(',')])
'''
#27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
'''
x=open('hari.txt')
y=x.readlines()[1].split(',')
for i in y:
    print(i[1:-1])

print([i[1:-1] for i in open('hari.txt').readlines()[1].split(',')])
'''
#28 Write a program to count total number of words which starts with 'S' character?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i[0]=='S':
        a.append(i)
print(len(a))

print(len([i for i in open('hari.txt').read().split(',') if i[0]=='S']))
'''
#29. Write a program to fetch all duplicate names in the file?    
'''
a=[]
x=open('hari.txt')
y=x.read().replace('\n',',').split(',')
for i in y:
    if y.count(i)>1:
        print(set([i]))


print(list([i for i in open('hari.txt').read().replace('\n',',').split(',') if open('hari.txt').read().replace('\n',',').split(',').count(i)>1]))  #doubt
'''
#30. Write a program to count all vowels in the file? (Note: output must be in dict)  
'''
x=open('hari.txt')
y=x.read()
v='aeiouAEIOU'
d={}.fromkeys(v,0)                                                            #doubt
for i in y:
    if i in d:
        d(i)==d(i)+1
print(d)

print(list([len([i for i in open('hari.txt').read() if i in 'aeiouAEIOU'])]))
'''
#31. Write a program to reverse all words in the file?
'''
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    print(i[::-1])

print([i[::-1] for i in open('hari.txt').read().split(',')])
'''
#32. Write a program to fetch all words which contains two or more then a' characters?
'''
a=[]
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i.count('a')>2:
        a.append(i)
print(a)

print([i for i in open('hari.txt').read().split(',') if i.count('a')>2])
'''
#33. Write a program to fetch all words which starts and ends with 'a' character?
'''
x=open('hari.txt')
y=x.read().replace('\n',',').split(',')                                           #doubt
for i in y:
    if i[0]=='a':
        print(i)
'''
#34. Write a program to fetch word which has more number of 'a' characters?     

a=[]
 
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    a.append(i.count('a'))
for i in y:
    if max(a)==i.count('a'):
        print(i)

#doubt

print(i for i in open('hari.txt').read().split(',') if max==([for i in open('hari.txt').read().split(',')]))     

#35. Write a program to fetch all company names which starts with vowel?      #doubt()
'''
a=[]
x=open('hari.txt')
y=x.readlines()
for i in y:
    n=i.split(',')
print(n)

    if n[0] in 'aeiouAEIOU':
        a.append(i)
print(a)
'''
#36. Write a program to display company name which contains Saroj Employee?
'''
x=open('hari.txt')
y=x.readlines()[0].split(',')
print(y[0])

print([open('hari.txt').readlines()[0].split(',')[0]])
'''
#37. Write a program to count all words which starts and ends with consonants?
'''
x=open('hari.txt')
y=x.read().split(',')
for i in y:
    if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU':
        print(i)

print([i for i in open('hari.txt').read().split(',') if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU'])
'''

#38. Write a program to fetch all company names which does not contain Venkat employee?
'''
x=open('hari.txt')
y=x.readlines()
for i in y:
    n=i.split(',')
    if 'Venkat' not in n:
        print(n[0])
'''
#39. Write a program to display company name where Narayana is working?     
'''
x=open('hari.txt')
y=x.readlines()
for i in y:
    n=i.split(',')
    if 'Narayana' in n:
        print(n[0])
'''
#40. Write a program to display the first word and last word from each line in dict format?
'''
x=open('hari.txt')
y=x.readlines().split(',')                                    #doubt
print(y[0])
'''
#41. Write a program to fetch all names whose name starts with a in NTH company?
'''
a=[]
x=open('hari.txt')
y=x.readlines()[4].split(',')[1::]
for i in y:
    if i[0] in 'aA':
        a.append(i)
print(a)

print([i for i in open('hari.txt').readlines()[4].split(',')[1::] if i[0] in 'aA'])
'''
#42. Write a program to count total number of employees in CTS company?
'''
x=open('hari.txt')
y=x.readlines()[3].split(',')[1::]
print(len(y))

print(len([i for i in open('hari.txt').readlines()[3].split(',')[1::]]))
'''
#43. Write a program to fetch all companies where Venkat employee is working?
'''
x=open('hari.txt')
y=x.readlines()
for i in y:
    n=i.split(',')
    if 'Venkat' in n:
        print(n[0])
'''
#44. Write a program to fetch all companies names which name starts with Vowel?    #doubt
'''
a=[]
x=open('hari.txt')
y=x.readlines()
for i in y:
    if i[0] in 'aeiouAEIOU':
        a.append(i)
print(a)
'''
#45. Write a program to fetch all palindrome names from the file?   #doubt
'''
a=[]
x=open('hari.txt')
y=x.read().replace('\n',',').split(',')
for i in y:
    if i.lower()==i.lower()[::-1]:
        a.append(i)
print(a)

open('hari.txt').read().replace()
'''
#46. Write a program to fetch all companies names where palindrome named employees working?
'''
x=open('hari.txt')
y=x.read().split('\n')
for i in y:
    z=i.split(',')
print(z)
'''
#47. Write a program to fetch the lengthiest company name?
'''
x=open('hari.txt')
y=x.readlines()
for i in y:                                                                    #doubt
    n=i.split(',')
print(n[0])
'''
#48. Write a program to fetch the lengthiest employee name in ABC company?
'''
a=[]
x=open('hari.txt')
y=x.readlines()[5].replace('\n',',').split(',')[1::]
for i in y:
    a.append(len(i))
for i in y:
    if len(i)==max(a):
        print(i)
'''   
    
#49. Write a program to fetch shortest employee name in the WIPRO company?
'''
a=[]
x=open('hari.txt')
y=x.readlines()[2].replace('\n',',').split(',')[1::]
for i in y:
    a.append(len(i))
for i in y:
    if max(a)==len(i):
        print(i)
'''

#50. Write a program count total number of employees in each company(in dict format)?
'''
x=open('hari.txt')
y=x.readlines().replace('\n',',').split(',')
for i in y:
    print(y)
'''

















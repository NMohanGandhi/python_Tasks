#file handling

#wap to read the data from the file?
'''
print(open('read.txt').read())
'''

#wap to read first line from the file?
'''
x=open('read.txt')
y=x.readlines()
print([y[0]])

print([open('read.txt').readlines()[0]])
'''
#3.wap to read the last line from the file?
'''
x=open('read.txt')
y=x.readlines()
print([y[-1]])

print([open('read.txt').readlines()[-1]])
'''
#4.wap to read the 2nd line from the file?
'''
x=open('read.txt')
y=x.readlines()
print([y[1]])

print([open('read.txt').readlines()[1]])
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
print([open('read.txt').readlines()[1].split(',')[0]])


x=open('read.txt')
y=x.readlines()[1].split(',')
print(y[0])
'''
#7.wap to read the last word from the last line?
'''
print([open('read.txt').readlines()[0].split(',')[-1]])


x=open('read.txt')
y=x.readlines()[0]
z=y.split(',')
print(z[-1])
'''
#8.wap to read the first character from second word in the third line?
'''
x=open('read.txt')
y=x.readlines()[2].split(',')[1]
print(y[0])

print([open('read.txt').readlines()[2].split(',')[1][0]])
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
y=x.read().replace('\n',',').split(',')
for i in y:
    if i[0] in 'aeiouAEIOU':
        print(i)

print([i for i in open('read.txt').read().replace('\n',',').split(',')if i[0] in 'aeiouAEIOU'])
'''
#11.wap read all the words which has only 4character?
'''
x=open('read.txt')
y=x.read().replace('\n',',').split(',')
for i in y:
    if len(i)==4:
        print([i],end=',')

print([i for i in open('read.txt').read().replace('\n',',').split(',') if len(i)==4])
'''
#12.wap to read all the word which stat with consonent?
'''
x=open('read.txt')
y=x.read()
h=y.split(',')
for i in h:
    if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU':
        print(i)

print([i for i in open('read.txt').read().split(',') if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU'])
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
    print(i.split(',')[0],end=',')

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
y=x.readlines()[1].split(',')[2]
print(y[-1])

print([open('read.txt').readlines()[1].split(',')[2][-1]])
'''
#17.wap to read the biggest word in the file?
'''
x=open('read.txt')
y=x.read().replace('\n',',').split(',')
a=[]
for i in y:
    a.append(len(i))
for i in y:
    if max(a)==len(i):
        print(i)
print([i for i in open('read.txt').read().replace('\n',',').split(',')if len(i)==max(len(i) for i in open('read.txt').read().replace('\n',',').split(','))])
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


print(len([i for i in open('read.txt').read().split(',')if i=='Tarun']))
'''

#20.wap to count total number of words in the files?
'''
x=open('read.txt')
y=x.read().replace('\n',',').split(',')
count=0
for i in y:
    count=count+1
print(count)
    

print([len ( open('read.txt').read().replace('\n',',').split(','))])
'''
#21wap count  tatol no.of characters in the file (excludind coma and /n)?
'''
x=open('read.txt')
y=x.read()
count=0
for i in y:
    count=count+1
print(count)

print(len([i for i in open('read.txt').read()]))
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
x=open('read.txt')
y=x.readlines()
for i in y:
    if 'Ganga' in i:
        print(i.split(',')[0])

print([i.split(',')[0] for i in open('read.txt').readlines() if 'Ganga' in i])
'''
#26. wap to read the name which are repeted

x=open('read.txt').read().replace('\n',',').split(',')
a=[]
for i in x:
    for i==>1:
        a.append(i)
print(a)
        
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
a=[]
x=open('read.txt')
y=x.read()
for i in y:
    if i[0]=='S':
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
x=open('read.txt')
y=x.read()
v='aeiouAEIOU'
d={}.fromkeys(v,0)
for i in y:
    if i in d:
        d[i]=d[i]+1
print(d)
'''
     
     
         
     
 











#1.wap to fetch all even numbers from list?
'''
lst=[10,1,13,14,9,8]
def findindeven(lst1):
    a=[]
    for i in lst1:
        if i%2==0:
            a.append(i)
    print(a)
findindeven(lst)
'''
#2.wap to fetch the all string values from the list?
'''
lst=[10,'a',True,'b',False]
def findingstr(lst1):
    a=[]
    for i in lst1:
        if type(i)==bool:
            a.append(i)
    print(a)
findingstr(lst)
'''
#3.wap to fetch all 5 divisibles from list?
'''
lst=[12,15,27,20,5]
def divisible5(lst1):
    a=[]
    for i in lst1:
        if i%5==0:
            a.append(i)
    print(a)
divisible5(lst)
'''
#4.wap to count total no.of int values in the list?
'''
lst=[10,'a',20,True,30,'b',40]
def intvalues(lst1):
    a=[]
    for i in lst:
        if type(i) is int:
            a.append(i)
    print(len(a))
intvalues(lst)
'''
#5.wap to count total no.of characters in the string(including space)?
'''
st='python language'
def totalnumber(st1):
    a=[]
    for i in st1:
        a.append(i)
    print(len(a))

totalnumber(st)
'''
#6.wap to count total no.of words in string?
'''
st='python narayana tech house hyd'
def totalwords(st1):
    a=[]
    for i in st.split():
        a.append(i)
    print(len(a))
totalwords(st)
'''
#7.wap to fetct all vowels from the string?
'''
st='python language'
def allvowels(st1):
    a=[]
    for i in st1:
        if i in 'aeiou':
            a.append(i)
    print(a)
allvowels(st)
'''
#8.wap to count total no.of vowels?
'''
st='python narayana'
def totalvowel(st1):
    a=[]
    for  i in st1:
        if i in 'aeiou':
            a.append(i)
    print(len(a))
totalvowel(st)
'''
#9.wap to count total no.of characters in the string(excluding space)?
'''
st='python is a simple language'
def totalchar(st1):
    a=[]
    for i in st1:
        if i!=' ':
            a.append(i)
    print(len(a))
totalchar(st)
'''
#10.wap to count total no.of counsonents in the string?

st='python language'
def totalcon(a):
    b=[]
    for i in a:
        if i not in 'aeiou':
            a.append(i)
    print(len(b))

totalcon(st)

#11.wap a program to fetch all words which starts with vowel from givin string?
'''
st='python is simple and easy language'
a=st.split(' ')
for i in a:
    if i[0] in 'aeiou':
        print(i)
'''
#12.wap to fetch all words wchich ends with consonents in the givin string?
'''
st='python is simple and easy language'
a=st.split(' ')
for i in a:
    if i[-1] not in 'aeiou':
        print(i)
'''
#13.wap to fetch all words which 'a' two or more then tow times?
'''
st='python is simple and easy language'
a=st.split(' ')
for i in a:
    if i.count('a')>=2:
        print(i)
'''
#14.wap to count no.of characters of each word in the string?
'''
st='python is simple and easy language'
a=st.split(' ')
lst=[]
for i in a:
    lst.append(len(i))
print(lst)
'''
#15.wap to fetch the first and last character from each word in the string?
'''
st='python is simple and easy language'
a=st.split(' ')
h=[]
for i in a:
    if len(i)>=1:
        n1=i[0]
        n2=i[-1]
        h.append((n1,n2))
print(h)
'''
#16.wap to fetch all words which contains 'a' character in the string?
'''
st='python is simple and easy language'
a=st.split(' ')
for i in a:
    if 'a' in i:
        print(i)
'''
#17.wap to fetch all words which does not contines 'e' character in the string?
'''
st='python is simple and easy language'
a=st.split(' ')
for i in a:
    if 'e' not in i:
        print(i)
'''
#18.wap to fetch all words which contains only 4 or less then 4 characters?
'''
st='python is simple and easy language'
a=st.split(' ')
for i in a:
    if len(i)<=4:
        print(i)
'''
#19.wap to  fetch all words which contains odd no.of chsracters in the string?
'''
st='python is simple and easy language'
a=st.split(' ')
h=[]
for i in a:
   if len(i)%2!=0:
       print(i)
'''
#20.wap to fetch all words which starts and ends with vowels in the string?
'''
st='python is number one language'
a=st.split(' ')
for i in a:
    if i[0] in 'aeiou' and i[-1]  in 'aeiou':
        print(i)
'''
#21.wap to fetch all palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
for i in names:
    if i[-1::-1]==i:
        print(i)
'''
#22.wap to fetch all non palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
for i in names:
    if i[-1::-1]!=i:
        print(i)
'''
#23.wap to fetch all palindrom words wchich starts with 'm' character?
'''
names=['madam','python','dad','language','eye','malayalam']
for i in names:
    if i[0]=='m' in i[-1::-1]:
        print(i)
'''
#24.wap to fetch all palindrom words which more the 3 characters?
'''
names=['madam','python','dad','language','eye','malayalam']
for i in names:
    if i[-1::-1]==i and len(i)>3:
        print(i)
'''
#25.wap to longest palindrom in word?
'''
names=['madam','python','dad','language','eye','malayalam']
a=[]
for i in names:
    if i[-1::-1]==i:
        a.append(len(i))
for i in names:
    if len(i)==max(a):
        print(i)
'''




























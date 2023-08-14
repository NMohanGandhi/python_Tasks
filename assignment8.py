#1.wap to fetch all even numbers from list?
'''
lst=[10,1,13,14,9,8]
print([i for i in lst if i%2==0])
'''
#2.wap to fetch the all string values from the list?
'''
lst=[10,'a',True,'b',False]
print([i for i in lst if type(i) is str])
'''
#3.wap to fetch all 5 divisibles from list?
'''
lst=[12,15,27,20,5]
print([i for i in lst if i%5==0])
'''
#4.wap to count total no.of int values in the list?
'''
lst=[10,'a',20,True,30,'b',40]
print([i for i in lst if type(i) is int])
'''
#5.wap to count total no.of characters in the string(including space)?
'''
st='python language'
print(len([i for i in st]))
'''
#6.wap to count total no.of words in string?
'''
st='python narayana tech house hyd'
print(len([i for i in st.split(' ')]))
'''
#7.wap to fetct all vowels from the string?
'''
st='python language'
print([i for i in st if i in 'aeiou'])
'''
#8.wap to count total no.of vowels?
'''
st='python narayana'
print(len([i for i in st if i in 'aeiou']))
'''
#9.wap to count total no.of characters in the string(excluding space)?
'''
st='python is a simple language'
print(len([i for i in st]))
'''
#10.wap to count total no.of counsonents in the string?
'''
st='python language'
print(len([i for i in st if i not in 'aeiou' and i not in  ' ']))
'''
#11.wap a program to fetch all words which starts with vowel from givin string?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if i[0] in 'aeiou'])
'''
#12.wap to fetch all words wchich ends with consonents in the givin string?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if i[-1] not in 'aeiou'])
'''
#13.wap to fetch all words which 'a' two or more then tow times?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if i.count('a')>=2])
'''
#14.wap to count no.of characters of each word in the string?
'''
st='python is simple and easy language'
print([len(i) for i in st.split(' ')])
'''
#15.wap to fetch the first and last character from each word in the string?
'''
st='python is simple and easy language'
print([(i[0],i[-1]) for i in st.split(' ') if len(i)>=1 ])
'''
#16.wap to fetch all words which contains 'a' character in the string?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if 'a' in i])
'''
#17.wap to fetch all words which does not contines 'e' character in the string?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if 'e' not in i])
'''
#18.wap to fetch all words which contains only 4 or less then 4 characters?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if len(i)<=4])
'''
#19.wap to  fetch all words which contains odd no.of chsracters in the string?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if len(i)%2!=0])
'''
#20.wap to fetch all words which starts and ends with vowels in the string?
'''
st='python is number one language'
print([i for i in st.split(' ') if i[0] in 'aeiou' and i[-1] in 'aeiou'])
'''
#21.wap to fetch all palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1]==i])
'''
#22.wap to fetch all non palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1]!=i])
'''
#23.wap to fetch all palindrom words wchich starts with 'm' character?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[0]=='m' and i[-1::-1]])
'''
#24.wap to fetch all palindrom words which more the 3 characters?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1]==i and len(i)>3])
'''
#25.wap to longest palindrom in word?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[-1::-1]==i and len(i)==max([len(i) for i in names if i[-1::-1]==i])])
'''










































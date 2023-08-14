#1.wac to fetch all words which name has Mr.intial?
'''
Names=['Mrs Kavya','Mr.Satya','Mr.Rajesh','Ms.Rajani']
print([i for i in Names if 'Mr.' in i])
'''
#2.wac to count total no.of characters?
'''
st='python narayana tech house hyderabada'
print([len(st)])
'''
#3.wac to fetch all palindrome words from list?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if i[::-1]==i])
'''
#4.wac to longest palindrom word?
'''
names=['madam','python','dad','language','eye','malayalam']
print([i for i in names if len(i)==max(len(i) for i in names)])
'''
#5.wac to fetch the first and last char from ech word in the st?
'''
st='python is simple and easy language'
print([(i[0]+i[-1]) for i in st.split(' ') if len(i)>=1])
'''
#6.wac to fetch starts and ends with vowels?
'''
st='python is simple and easy language'
print([i for i in st.split(' ') if i[0] in 'aeiou' and i[-1] in 'aeiou' ])
'''
#7.wac to fetch all  words which contains a character in the string?
'''
st='python is simple and easy language'
print([i for i in st.split() if 'a' in i])
'''

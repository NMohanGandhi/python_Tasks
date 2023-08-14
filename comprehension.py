#8.wac to fetch all words which starts with vowels and end with vowel?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i[0] in 'aeiou' and i[-1] in 'aeiou'])
'''

#9.wac to fetch all words which starts with vowel and ends with consonent?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i[0] in 'aeiou' and i[-1] not in 'aeiou'])
'''
#10.wac to fetch all words which starts  and ends with consonent?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i[0] in 'aeiou' and i[-1] in 'aeiou'])
'''
#11.wac to fetch all words which starts  consonents and ends with vowels?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i[0] not in 'aeiou' and i[-1] in 'aeiou'])
'''
#12.wac to fetch all words which has more then two 'a' character?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i.count('a')>=2])
'''
#13.wac to fetch the all worfs wchich word ends with vowels?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i[-1] in 'aeiou'])
'''
#14.wac to fetch all words which stars with cosonent?
'''
names=['narayana','apple','andoied','python']
print([i for i in names if i[0] not in 'aeiou'])
'''
#15.wac to fetch all words expect first and last character from each word?
'''
 names=['narayana','apple','andoied','python']
print([i[1:-1] for i in names])
'''
#16.wac to fetch all wrods wchich has 3 or 4 character in the string?
'''
st='python is simple and easy language'
print([i for i in st.split() if len(i)>3 and 4])
'''
#17.wac to fetch the smallest word from string? {doubt}
'''
st='python is simple and easy language'
print([i for i in st.split() if len(i)==min([len(i) for i in st.split()])])
'''
#18.wac to fetch the bigest word from string? {doubt}
'''
st='python is simple and easy language'
print([i for i in st.split() if len(i)==max([len(i) for i in st.split()])])
'''
#19.wac to count a total number in string? {doubt}
'''
st='python is simple and easy language'
print(len([i for i in st.split()]))
'''
#20.wac to count no. of character in each word?
'''
st='python is simple and easy language'
print([len(i) for i in st.split()])
'''
#21.wac to fetch all palindram word from list?
'''
name=['python','madam','django','malayalam','language','dad']
print([i for i in name if  i[::-1]==i ])
'''
#22.wac to fetch biggest palindroom word from list?
'''
name=['python','madam','django','malayalam','language','dad']
print([i for i in name if len(i)== max([len(i)for i in name if i==i[-1::-1]])])
'''


#23.wac to fetch smallest palindroom word from list?
'''
name=['python','madam','django','malayalam','language','dad']
print([i for i in name if len(i)== min([len(i)for i in name if i==i[-1::-1]])])
'''
#24. wac to fetch the palindrom word which stars and ends with 'd' fromlist?
'''
name=['python','madam','django','malayalam','language','dad']
print([i for i in name if i[0] and i[-1] in 'd'])
'''
#25.wac to fetch all palindram word which does not contain 'd' character?
'''
name=['python','madam','django','malayalam','language','dad']
print([i for i in name if 'd' not in i[::-1]==i ])
'''

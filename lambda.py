#1.WAL EXPRESSION TO FILTER ALL EVEN NUMBERS FROM THE LIST?
lst=[5,3,2,7,6,9,1,2]
print(list(filter(lambda i:i%2==0,lst)))

#2.wal expression to filter all numbers which are divisible by both 3 and 6?
lst=[12,15,21,30,24]
print(list(filter(lambda i:i%3==0 and i%6==0,lst)))
#3.wal lambda expression to filter to all words wich stats with upper case?

lst=['Python','django','Narayana','hydrabad']
print(list(filter(lambda i:i[0].isupper(),lst)))

#4.wal expression to fillter all words which contains only 6characters?
st='python is simple and easy language'
print(list(filter(lambda i:len(i)==6,st.split(' '))))
#5.wal expression to fillter all words which are palindrom?
names=['python','madam','django','malayalam']
print(list(filter(lambda i:i==i[::-1],names)))

#6.wal expression to fillter all words which are not contains 'm' characters?
names=['python','madam','django','malayalam']
print(list(filter(lambda i:'m' not in i,names)))
#7.wal expression to fillter all vowels from the givin string?
st='python'
print(list(filter(lambda i:i in 'aeiou',st)))
#8.wal expression to fillter the biggest word in the list?
names=['python','madam','django','malayalam']
bigest=max(names,key=lambda i:len(i))
print(bigest)


#9.wal expression to fillter the smallest palindrom word in the list?

names=['python','madam','django','malayalam']
bigest=min(names,key=lambda i:i[::-1])
print(bigest)

#10.wal expression to fillter all duplicates words from givin string?     #doubt
st='python is easy language because python is easy to understand'
print(list(filter(lambda i:i==i,names)))
#11.wal expression to fillter all bool values from list?
lst=['python',10,False,2+3j,True]
print(list(filter(lambda i:type(i)==bool,lst)))




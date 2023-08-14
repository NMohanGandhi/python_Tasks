 
#WALE to add 5 to each element in the list?
lst=[10,20,30,40,50]
print(list(map(lambda i : i+5,lst)))
#2.WALE  to find the square of each element?
lst=[3,5,6,3,8]
print(list(map(lambda i:i*i,lst)))
#3.WALE to fetch the first character  from each word?
st='python narayana tech house'
print(list(ma p(lambda i:i[0],st.split())))
#4.WALE to fins lenth of each word?
st='python narayana tech house'
print(list(map(lambda i: len(i),st.split())))
#5.WALE to fetch all words except first and last character?
st='python narayana tech house'
print(list(map(lambda i:i[1:-1],st.split())))
#6.WALE to fetch first and last character from the each word?
st='python narayana tech house'
print(list(map(lambda i:i[0] + i[-1],st.split())))
#7.WALE to find the cubes of all odd numbers?
lst=[2,3,5,4,6]
x=[i for i in lst if i%2!=0]
print(list(map(lambda i:i*i*i,x)))
#8.WALE to display the next number of each even numbers?
lst=[2,True,'a',4,7,2+3j]
n=[i for i in lst if type(i) is int and i%2==0] 
print(list(map(lambda i:i+1,n)))

#9.WALE to find the length of each word wchich stats with vowel?
st='python is easy language because python is easy to understand '
x=[i for i in st.split() if i[0] in 'aeiou']
print(list(map(lambda i:len(i),x)))

#10.WALE to find the length top 3 biggest words in string?
st='python is easy language because python is easy to understand '
lst=[]
for i in st.split():
    lst.append(len(i))
n=list(set(lst))
print(n[-3:])

x=sorted([len(i) for i in st.split()])[-3::]
print(list(set(map(lambda i:i,x))))
#11.WALE to find the reverse the three smallest words in striing?
st='python is easy language because python is easy to understand '


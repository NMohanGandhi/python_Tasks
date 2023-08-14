#1. Write a program to display all 1 to 9 divisibles between 1 to 100 in dict format?
#Like {1:15, 2:10, 3:5.......9:10} Notes: Its just a reference.
'''
n=100
n1=9
for i in range(1,n+1):
    for j in range(1,n1+1):
        if j%i==0:
            a={},fromkeys(j,i)
print(a)
'''
#2. Write a program to count total number of 5 divisibles between 1 to 100?
'''
n=eval(input('Enter any number: '))
a=[]
for i  in range(1,n+1):
    if i%5==0:
        a.append(i)
print(a)
'''
#3. Write a program to Check Whether the Given String is Pangram without using lower() or upper()
'''
n=input('Enter any name: ')
n=n.replace(' ','a')
print(len(set(n)))
if len(set(n))==26:
    print('{} is  an  pangram'.format(n))
else:
    print('{} is not an pangram'.format(n))
'''
#4. Write a program to display the common elements from both lists?
'''
lst1 = ['Anu', 'Sonu', 'Raanu', 'Poonu', 'Kaanu']
lst2 = ['Renu', 'Poonu', 'Sonu', 'Anu', 'Venu']               #OutPut: ['Anu','Sonu']

a=[]
for i in lst1:
    for j in lst2:
        if i==j:
            a.append(i)
print(a)




def find_common_element(lst1,lst2):
    common_elements=set(lst1) & set(lst2)
    return list(common_elements)
   a=find_common_element(lst1,lst2)
print('common element: ',a)
'''

#5. Write a program to display the names which are available in lst2 but not in lst1?
'''
lst1 = ['Ravali', 'Komali', 'Anjali']
lst2 = ['Komali', 'Ravali', 'Mouli','Vishali']



def find_uniqueelements(lst1,lst2):
    uniqee=set(lst2) - set(lst1)
    return list(uniqee)
a=find_uniqueelements(lst1,lst2)
print('lst2 but not in lst1: ',a)
'''
#6. Write a program to count number of repeatations of each character, like below 
st = 'aaaaabbbbcccdde'                             #OutPut: a5b4c3d2e1

        
    

#7. Write a program to find the factors of given number
'''
a=eval(input('Enter Any Number: '))
x=[]
for i in range(1,a+1):
    if a%i==0:
        x.append(i)
print(x)
'''
#8. Write a program to reverse first and last word of lengthy string which can have n number of words?
'''
st = 'python narayana tech house'                 #Output: esuoh narayana tech nohtyp
def reverse_first_and_last_word(st):
    words=st.split()
    if len(words) == 1:
        return s
    first_word = words[0]
    last_word= words[-1]
    modified_string = last_word
    for word in words[1:-1]:
        modified_string+=" "+word
    modified_string+=" "+first_word
    return modified_string
input_string=st
output=reverse_first_and_last_word(input_string)
print(output)
'''
#9. Write a program to get nest character of each character in the string?

st = 'narayana'                                       #OutPut: obsbzbob
def get_next_character(st):
    result=""
    for i in st:
        next_char=chr(ord(char)+1)
        result +=next_char
    return result
a=st

print(a)
#10. Write a program to get day name as per user requirement?
'''
Note: 1 will be Monday, 2 will be Tuesday.....7 will be Sunday
Eg:
Enter Any Number: 1
Monday 
Enter Any Number: 7
Sunday 
Enter Any Number: 10
10 is invalid number.
'''

#11. Write a program to display the calendar as per year and month numbers given user?
'''
Eg:
Enter Month Number: 3
Enter Year Number: 2023
'''
#12. Write a program to display the number of days of specific month given by user?
'''
Eg:
Enter Month Number: 3
Enter Year Number: 2023
Number of days in March Month: 31
Enter Month Number: 10
Enter Year Number: 2010
Number of days in October month:31
'''

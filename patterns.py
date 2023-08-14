

#1.pattern?
'''
* 
* * 
* * * 
* * * * 
* * * * * 

n=eval(input('enter any number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
'''
#2.pattern
'''
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * * 

n=eval(input('enter any number: '))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print('*',end=' ')
    k=k+2
    print()
'''
#3.pattern
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''
n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for z in range(1,i+1):
        print('*',end=' ')
    print()
  

#4.pattern
'''
1 
2 2 
3 3 3 
4 4 4 4 

n=eval(input('Enter Any Number: '))
for i in range(0,n):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
'''
#5.patterns
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end=' ')
    print()
'''
#6.patterns
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
#7.pattern
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

n=int(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(n-i+1,end=' ')
    print()
'''
#8.patterns
'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n,end=' ')
    print()
'''
#9.patterns
'''
5 
5 5 
5 5 5 
5 5 5 5 
5 5 5 5 5 


n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=' ')
    print()
'''
#10.pattern
'''
        5 
      5 5 
    5 5 5 
  5 5 5 5 
5 5 5 5 5 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for z in range(1,i+1):
        print(n,end=' ')
    print()
'''
#11.patterns
'''
5 5 5 5 5 
  5 5 5 5 
    5 5 5 
      5 5 
        5 

n=eval(input("Enter Any Number: "))
for i in range(1,n+1):
    for j in range(0,i-1):
        print(' ',end=" ")
    for z in range(1,n+2-i):
        print(n,end=' ')
    print()
'''
#12.patterns
'''
5 5 5 5 5   5 5 5 5 5 
5 5 5 5       5 5 5 5 
5 5 5           5 5 5 
5 5               5 5 
5                   5 


n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n,end=' ')
    for z in range(1,i+1):
        print(' ',end=' ')
    
    for z in range(1,i+1):
        print(' ',end=' ')
    for x in range(1,n+2-i):
        print(n,end=' ')
    print()
'''
#13.patterns
'''
5                   5 
5 5               5 5 
5 5 5           5 5 5 
5 5 5 5       5 5 5 5 
5 5 5 5 5   5 5 5 5 5 


n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=' ')
    for z in range(1,n+2-i):
        print(' ',end=' ')
    for c in range(1,n+2-i):
        print(' ',end=' ')
    for b in range(1,i+1):
        print(n,end=' ')
    print()
'''
#14.patterns
'''
5 5 5 5 5   5 5 5 5 5 
5 5 5 5       5 5 5 5 
5 5 5           5 5 5 
5 5               5 5 
5                   5 
5                   5 
5 5               5 5 
5 5 5           5 5 5 
5 5 5 5       5 5 5 5 
5 5 5 5 5   5 5 5 5 5 
n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for a in range(1,n+2-i):
        print(n,end=' ')
    for b in range(1,i+1):
        print(' ',end=' ')
    for c in range(1,i+1-1):
        print(' ',end=' ')
    for d in range(1,n+2-i):
        print(n,end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=' ')
    for k  in range(1,n+2-i):
        print(' ',end=' ')
    for l in range(1,n+1-i):
        print(' ',end=' ')
    for m in range(1,i+1):
        print(n,end=' ')
    print()
'''
#15.patterns
'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for a in range(i,0,-1):
        print(a,end=' ')
    print()
'''

#16.patterns
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()
'''
#17.patters
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 


n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=' ')
    print()
'''
#18.patters
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
#19.patterns
'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()
'''
#20.patterns
'''
        1 1 
      1 2 1 2 
    1 2 3 1 2 3 
  1 2 3 4 1 2 3 4 
1 2 3 4 5 1 2 3 4 5 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for z in range(1,i+1):
        print(z,end=' ')
    for c in range(1,i+1):
        print(c,end=' ')
    print()
'''
#21.patterns
'''
        1 1 
      1 2 2 1 
    1 2 3 3 2 1 
  1 2 3 4 4 3 2 1 
1 2 3 4 5 5 4 3 2 1 


n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for z in range(1,i+1):
        print(z,end=' ')
    for c in range(i+1-1,0,-1):
        print(c,end=' ')
    print()
'''
#22.patterns
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for i in range(1,n+1):
    for a in range(1,n+2-i):
        print(a,end=' ')
    print()
'''
#23.pattern
'''
1                 1 
1 2             1 2 
1 2 3         1 2 3 
1 2 3 4     1 2 3 4 
1 2 3 4 5 1 2 3 4 5 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for a in range(1,n+1-i):
        print(' ',end=' ')
    for b in range(1,n+1-i):
        print(' ',end=' ')
    for c in range(1,i+2-1):
        print(c,end=' ')
    print()
'''
#24.patterns
'''
1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 

n=eval(input('Enter Any Number: '))
for i in range(1,n+1):
    for  j in range(1,i+1):
        print(j,end=' ')
    for z in range(1,n-i+1):
        print(' ',end=' ')
    for c in range(1,n-i+1):
        print(' ',end=' ')
    for m in range(i+1-1,0,-1):
        print(m,end=' ')
    print()
'''
#25.pattern
'''
        1 1 
      1 2 2 1 
    1 2 3 3 2 1 
  1 2 3 4 4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
  1 2 3 4 4 3 2 1 
    1 2 3 3 2 1 
      1 2 2 1 
        1 1 

n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for a in range(1,i+1):
        print(a,end=' ')
    for b in range(i,0,-1):
        print(b,end=' ')
    print()
for i in range(1,n+1):
    for d in range(1,i):
        print(' ',end=' ')
    for c in range(1,n+2-i):
        print(c,end=' ')
    for e in range(n+1-i,0,-1):
        print(e,end=' ')
    print()
'''
#26.pattrens
'''
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 

n=5
for i in range(0,n):
    for j in range(0,n+1-i):
        print(j,end=' ')
    print()
'''
#27.patterns                                          
'''
1 
2 3 
4 5 6 
7 8 9 10 

n=20
k=1
for  i in range(1,n+1):
    for j in range(i):
        if k>n:
            break
        print(k,end=' ')
        k=k+1
    if k>n:
        break
    print()
'''
#28.patterns
'''
1 
1 2 1 
1 2 3 1 2 
1 2 3 4 1 2 3 
1 2 3 4 5 1 2 3 4 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(1,i):
        print(k,end=' ')
    print()
'''
#29.patterns
'''
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for z in range(i-1,0,-1):
        print(z,end=' ')
    print()
'''
#30.patterns
'''
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 3 4 5 
5 4 3 3 4 5 
5 4 4 5 
5 5 

n=5
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=' ')
    for k in range(i,n+1):
        print(k,end=' ')
    print()

'''
#alphabates patterns
#31.pattern
'''
A 
B B 
C C C 
D D D D 
E E E E E 

n=5
num=65
for i in range(0,n):    #0,1,2,3,4
    for j in range(0,i+1):   #0 0,1 0,1,2 0,1,2,3, 0,1,2,3,4
        ch=chr(num)
        print(ch,end=' ')
    num=num+1
    print()
'''
#32.pattern
'''
A 
B C 
D E F 
G H I J 
K L M N O 


n=5
num=65
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(num)
        print(ch,end=' ')
        num=num+1
    print()
'''
#33.patterns
'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 

n=5
num=65
for i in range(0,n):
    for j in range(0,n+1-1):
        ch=chr(num)
        print(ch,end=' ')
        num=num+1
    print()
'''
#34.patterns
'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 

n=5
num=65
for i in range(0,n):
    for j in range(0,n+1-1):
        ch=chr(num)
        print(ch,end=' ')
    num=num+1
    print()
'''
#35.patterns
'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 

n=5
for i in range(0,n):
    for j in range(65,65+n):
        print(chr(j),end=' ')
    print()

'''
#36.pattern
'''
A 
A B 
A B C 
A B C D 
A B C D E 

n=5
for i in range(0,n):
    for j in range(0,1+i):
        print(chr(j+65),end=' ')
        
    print()
'''
#37.patterns
'''
          A 
        A B 
      A B C 
    A B C D 
  A B C D E 

n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(' ',end=' ')
    for k in range(0,i+1):
        print(chr(k+65),end=' ')
    print()

'''

















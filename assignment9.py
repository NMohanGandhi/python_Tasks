 
movies = {
    'actors':{
        'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
        'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},

        'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
        'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},

        'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1},
        'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married',
        'sRate':'50%'},

        'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
        'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},

        'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2,
        'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
    },

    'actress':{

        'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1},
        'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single',
        'sRate':'40%'},

        'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},
        'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single',
        'sRate':'30%'},

        'saipallavi':{'knownAs':'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},
        'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single',
        'sRate':'60%'},

        'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15,
        'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},

        'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
        'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
 }
}
#1. Write a program to display all actors names
'''
lst=[]
for i in movies:
    if i=='actors':
        for a in movies['actors']:
            lst.append(a)
        print(lst)
'''
#2. Write a program to display all actress names
'''
lst=[]
for i in movies:
    if i=='actress':
        for a in movies['actress']:
            lst.append(a)
        print(lst)
'''
#3. Who is Darling?
'''
for i in movies['actors']:
    if 'Darling' in movies['actors'][i]['knownAs']:
        print(i)
'''
#4. What are the total number of Nandi Awards won by actors?
'''
count=0
for i in movies['actors']:
    for a in movies['actors'][i]['awards']:
        if movies['actors'][i]['awards']['nandi']:
            count=count+1
print(count)
'''
#5. What is the name of Prince?
'''
for i in movies['actors']:
    if 'Prince' in movies['actors'][i]['knownAs']:
        print(i)
'''
#6. What are the total number of awards own by Ram Charan?
'''
for i in movies['actors']:
    if i in 'ramcharan':
        x=Cprint(x)   
'''
#7. Which actor won more number of Nandi Awards?
'''
a=[]
for i in movies['actors']:
    a.append(movies['actors'][i]['awards']['nandi'])
    
for i in movies['actors']:
    if movies['actors'][i]['awards']['nandi'] == max(a):
        print(i)
'''
#8. What is the success rate of Prince?
'''
for i in movies['actors']:
    if 'Prince' in movies['actors'][i]['knownAs']:
        print(movies['actors'][i]['sRate'])
'''        
#9. Which artist has more number of Hits?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']+movies[i][j]['hits']['flops'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']+movies[i][j]['hits']['flops']==max(a):
            print(j)
'''       

#10. Who is Milky Beauty?
'''
for i in movies['actress']:
    if 'Milky Beauty' == movies['actress'][i]['knownAs']:
        print(i)
'''
#11. What is the nick name of Rashmika?
'''
for i in movies['actress']:
    if i=='rashmika':
        print(movies['actress'][i]['knownAs'])
'''
#12, What are actress names who did not win at least one Nandi Award?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['awards']['nandi'])
    
for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi'] <=1:
        print(i)
'''
#13. What are the total number of SIIMA awards won by all artists?
'''
count=0
for i in movies:
    for j in movies[i]:
        count=count+ movies[i][j]['awards']['siima']
print(count)
'''
#14. What is the artist name who has more success rate?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['sRate']==max(a):
            print(j)
'''
#15. What is the age of actor who has more super hit movies?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['hits']['super'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['hits']['super']==max(a):
            print(movies[i][j]['age'])
'''
#16. What is the actress name who is married?
'''
for i in movies['actress']:
    if 'married' == movies['actress'][i]['mStatus']:
        print(i)
'''
#17. Who is the tallest actress?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['height'])
for i in movies['actress']:
    if movies['actress'][i]['height']==max(a):
        print(i)
'''
#18. Who is the Youngest artist?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['age']==min(a):
            print(j)
'''
#19. Who are unmarried actress?
'''
for i in movies['actress']:
    if 'married' != movies['actress'][i]['mStatus']:
        print(i)
'''
#20. Who is smallest actress?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['height'])
for i in movies['actress']:
    if movies['actress'][i]['height']==min(a):
        print(i)

'''
#21. Which actress has more Flops?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['hits']['flops'])
for i in movies['actress']:
    if movies['actress'][i]['hits']['flops']==max(a):
        print(i)
'''
#22. What is the age of butter milky beauty?
'''
for i in movies['actress']:
    if 'Butter Milky Beauty' == movies['actress'][i]['knownAs']:
        print(movies['actress'][i]['age'])
'''
#23. What are the total number of flops of all actress?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['hits']['flops'])
print(sum(a))
'''
#24. What are the ages of Sam and Kaj?
'''
a=[]
for i in movies['actress']:
    if 'Sam'== movies['actress'][i]['knownAs']:
        a.append(movies['actress'][i]['age'])
for i in movies['actress']:
    if 'Kaj'==movies['actress'][i]['knownAs']:
        a.append(movies['actress'][i]['age'])
print(a)    
'''
#25. Which actress own highest total number of Awards?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['awards']['nandi']+movies['actress'][i]['awards']['cinemaa']+movies['actress'][i]['awards']['siima'])    
for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi']+movies['actress'][i]['awards']['cinemaa']+movies['actress'][i]['awards']['siima'] == max(a):
        print(i)
'''
#26. Who is the tallest artist?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['height'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['height']==max(a):
            print(j)
'''
#27. What are the total number of Industry hits of who has more Success Rate?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['sRate']==max(a):
            print(movies[i][j]['hits']['industry'])
'''
#28. What is the success rate of youngest actress?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['age'])
for i in movies['actress']:
    if movies['actress'][i]['age']==min(a):
        print(movies['actress'][i]['sRate'])
'''
#29. Who is youngest married actress?
'''
a=[]
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        a.append(movies['actress'][i]['age'])
for i in movies['actress']:
    if movies['actress'][i]['age']==min(a):
    
        print(i)
'''
#30. Who is oldest unmarried actor?
'''
a=[]
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        a.append(movies['actress'][i]['age'])
for i in movies['actress']:
    if movies['actress'][i]['age']==max(a):
        print(i)
'''
#31. Who are the high successful actor and actress?
'''
a=[]
for i in movies['actors']:
   a.append(movies['actors'][i]['sRate'])
print(i)
for i in movies['actress']:
   a.append(movies['actress'][i]['sRate'])
print(i) 
'''
#32. Totally how many unmarried artists are acting in movies?
'''
a=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['mStatus']!='married':
            a.append([j])
print(len(a))
'''
#33. Which actress is having more industry hit movies?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super']+movies['actress'][i]['hits']['flops'])
for i in movies['actress']:
   if movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super']+movies['actress'][i]['hits']['flops']==max(a):
        print(i)
'''
#34. Which actress does not have atleast one industry hit also?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['hits']['industry'])
    
for i in movies['actress']:
    if movies['actress'][i]['hits']['industry'] <=1:
        print(i)
'''
#35. What are the total number of industry and super hits of tallest actress?
'''
a=[]
b=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['height'])
for i in movies['actress']:
    if movies['actress'][i]['height']==max(a):
        b.append(movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super'])
print(b)
'''
#36. Which actress is having lengthiest nick name?
'''
a=[]
for i in movies['actress']:
    a.append(len(movies['actress'][i]['knownAs']))
for i in movies['actress']:
    if str(max(a)) in str(len(movies['actress'][i]['knownAs'])):
        print(i)
'''
#37. Who are the youngest unmarried artist?
'''
a=[]
for i in movies:
    for j in movies[i]:
        if 'married' != movies[i][j]['mStatus']:
            a.append(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['age']==min(a):
            print(j)
'''
#38. What are the total number of Industry hits and Super Hits of the actress who got more SIIMA awards? 
'''
a=[]
b=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['awards']['siima'])    
for i in movies['actress']:
    if movies['actress'][i]['awards']['siima'] == max(a):
        b.append(movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super'])
print(b)
'''
#39. What are the ages of Darling and Milky Beauty?
'''
a=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Darling':
            a.append(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Milky Beauty':
            a.append(movies[i][j]['age'])
print(a)
'''
#40. What are names of actors whose nick name contains star?
'''
for i in movies['actors']:
    if 'Star' in movies['actors'][i]['knownAs']:
        print(i)
'''
#41. What is the total remuneration of all actors?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['remuneration'])
print(sum(a))
'''
#42. What is the remuneration of an actor who has more flops?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['hits']['flops'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['hits']['flops']==max(a):
            print(movies[i][j]['remuneration'])
'''
#43. What is the highest remuneration of an unmarried actress?
'''
for i in movies['actress']:
    if movies['actress'][i]['mStatus']!='married':
        print(max([movies['actress'][i]['remuneration']]))
'''    
#44. What are the names of artists who has more remuneration?
'''
a=[]
for i in movies:
    for j in movies[i]:
        a.append(movies[i][j]['remuneration'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['remuneration']==max(a):
            print(j)
'''
#45. What is the remuneration of high successful Actress?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['sRate'])
for i in movies['actress']:
    if str(max(a)) in str(movies['actress'][i]['sRate']):
        print(movies['actress'][i]['remuneration'])
'''
        
#46. What is the remuneration of actress who has more industry hits?
'''
a=[]
for i in movies['actress']:
    a.append(movies['actress'][i]['hits']['industry'])
for i in movies['actress']:
    if str(max(a)) in str(movies['actress'][i]['hits']['industry']):
        print(movies['actress'][i]['remuneration'])
'''
#47. What are the ages of an actors whose remuneration is more then 90 crores?
'''
for i in movies['actors']:
    if movies['actors'][i]['remuneration']>90:
        print(movies['actors'][i]['age'])
'''
#48. What are the total number of industry hits of both Prince and Butter Milky Beauty?

#49. What is the age of Laughing Queen?
'''
for i in movies['actress']:
   if 'Laughing Queen' in movies['actress'][i]['knownAs']:
       print(movies['actress'][i]['age'])

'''
#50. What are the total number of awards won by an actor who has less successful rate?
a=[]
for i in movies['actors']:
    a.append(movies['actors'][i]['sRate'])
for i in movies['actors']:
    if min(a) in movies['actors'][i]['sRate']:
        print(movies['actors'][i]['awards']['nandi']+movies['actors'][i]['awards']['cinemaa']+movies['actors'][i]['awards']['siima'])

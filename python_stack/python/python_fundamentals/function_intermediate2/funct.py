# ---------------------------------sec1

from itertools import count
from turtle import update


x = [ [5,2,3], [10,8,9] ] 
student = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1------
x[1][0]=15
print(x)
#2-------
student[0]['last_name']='Bryant'
print(student[0]['last_name'])
#3-----------------------------
        
sports_directory['soccer'][0]='Andres'

print(sports_directory)
#4-------------------------
z[0]["y"]=30

print(z)



#---------------------------------section2

slash=" - "
temp = ""
def iterateDictionary(students) :
    for i in range(len(students)):
        print(',')
        temp=""
        for key in students[i].keys():
            
            temp += key+slash+students[i][key]+","
        print(temp) 


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# for i in range(len(students)) :
#     print(students[i]['first_name'])


iterateDictionary(students)

# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#--------------------------------------Get Values From a List of Dictionaries

def value_from_list(students,first) :
    for i in range(len(students)):
        print(students[i][first])
        

        print("------------------------------")
value_from_list(students,'first_name')
value_from_list(students,'last_name')




#------------------------------------4-final one
# 
def printInfo(dojos):
   for i in dojos.keys():
        print(len(dojos[i]))
        print(i)
        print("new")
        print(" ")
        for x in range(len(dojos[i])):
            print(dojos[i][x])
       


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
 
printInfo(dojo)





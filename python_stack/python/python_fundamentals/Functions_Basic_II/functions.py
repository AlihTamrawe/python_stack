

#------------------------1-counting down
def countdown(x):
    list = []
    for i in range(x,0,-1) :
        list.append(i)
    return list

print(countdown(5))

#-----------------------2-Print and Return

def print_return(list2):
    print(list2[0])
    c=list2[1]
    return c

print( print_return([1,2]))


#--------------------3-First Plus Length

def First_Plus_Length(list3):
    return (list3[0]+len(list3))

print(First_Plus_Length([5,8,9]))


#--------------------4-Values Greater than Second 

def greater_than_second(list11):
    temp = len(list11)
    list22 = []
    for i in range(0,temp):
        if list11[1] < list11[i]:
            list22.append(list11[i])
    return list22

li2=[]
li=[1,6,3,4,9,8]
greaternum=li[1]
if len(li) > 2 :
    li2=greater_than_second(li)
print(li2)
#--------------------5-This Length, That Value

def length_this_value(size,value):
    list=[]
    for i in range (1,size):
        list.append(value)
    return list


lis=length_this_value(7,9)

print(lis)

#------------------Biggie Size------------

def bigge(positive_list):
    leng=len(positive_list)
    str = "big"
    for i in range(0,leng):
        if positive_list[i]>0 :
            positive_list[i]=str
    return positive_list

changelist =bigge([-1,1,2,3,4,-1])
print(changelist)


#---------------Count Positives----------

def positive(positive_list):
    leng=len(positive_list)
    str = "big"
    counter = 0
    for i in range(0,leng):
        if positive_list[i]>0 :
            counter+=1

    positive_list[leng-1]=counter
    return positive_list

changelist =positive([-1,1,2,3,4,-1])
print(changelist)


#-----------------Sum Total 

def total(total_list):
    leng=len(total_list)
    sum = 0
    for i in range(0,leng):
        sum+=total_list[i]
    return sum
            

print(total([-1,4,5,-3,2]))


#--------------------Average

def avg(avg_list):
    leng=len(avg_list)
    sum = 0
    for i in range(0,leng):
        sum+=avg_list[i]
    return sum/leng
            

print(avg([-1,4,5,-3,2]))
# in intager result>> print(int(avg([-1,4,5,-3,2])))

#------------------------
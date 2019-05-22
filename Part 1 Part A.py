marks=0 # initializing marks to 0
#variables to store the number of stars
category1 = " " 
category2 = " "
category3=" "
category4=" "
category5=" "
# to check how many marks are entered withing a specific range
count1=0 
count2=0
count3=0
count4=0




while(marks>=0):
    marks=int(input("Please enter your marks: \n"))
    if marks>0 and marks<29: # marks between 0 to 29
        count1=count1+1 
        category1="*"*count1
    elif marks>=30 and marks<=39: # marks between 30 to 39
        count2=count2+1
        category2="*"*count2
    elif marks>=40 and marks<=69:# marks between 40 to 69
        count3=count3+1
        category3="*"*count3
    elif marks>=70 and marks<=100:# marks between 70 to 100
        count4=count4+1
        category4="*"*count4

print("-----------------------Histogram---------------------------")
totalCount=count1+count2+count3+count4 # opeation to get the totalnumber of students
print("0-29  ",category1,"\n30-39 ",category2,"\n40-69 ",category3,"\n70-100",category4)
print("--------------------Details--------------------")
print("Total number of students : ",totalCount)



        

marks=0 # initializing marks to 0
#variables to store the number of stars
category1=" " 
category2=" "
category3=" "
category4=" "
category5=" "
# to check how many marks are entered withing a specific range
count1=0 
count2=0
count3=0
count4=0
listOfMarks=[]
totalMarks=0
passed=0




while(marks>=0):
    try:
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
            passed+=1
        elif marks>=70 and marks<=100:# marks between 70 to 100
            count4=count4+1
            category4="*"*count4
            passed+=1
        elif marks>100:
                print("Error..........Please enter a value between 1 to 100")
                      
        else:
            break
        listOfMarks.append(marks) #adding the marks to a array list
        totalMarks+=marks # adding the marks together to find the average

    except:
         print("Please enter a integer value")
    
maxMark=max(listOfMarks)
minMark=min(listOfMarks)
print("---------------------------------Histogram-------------------------------------")
totalCount=count1+count2+count3+count4 # opeation to get the totalnumber of students
print("0-29\t30-39\t40-69\t70-100")
#to print the stars vertically down
while count1>0 or count2>0 or count3>0 or count4>0:
    if count1>0:
        print(" *",end="\t")
        count1=count1-1
    else:
        print(" ",end="\t")

    if count2>0:
        print("  *",end="\t")
        count2=count2-1
    else:
        print(" ",end="\t")

    if count3>0:
        print("  *",end="\t")
        count3=count3-1
    else:
        print(" ",end="\t")

    if count4>0:
        print("   *",end="\t")
        count4=count4-1
    else:
        print(" ",end="\t")
    print() 
print("-----------------------------------Details-----------------------------------")
print("Total number of students :",totalCount)
print("Average mark is",totalMarks/totalCount)
print("Number of student who have passed the exam:",passed)
print("Highest marks:",maxMark)
print("lowest marks:",minMark)



        

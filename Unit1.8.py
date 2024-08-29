#Find out pass-percentage of a class.A teacher is entering the marks of students. A student passes a course if the marks are at 
#least 40 (out of 100). The teacher wants to know the percentage of students passed

Students=int(input(" How Many Students : "))
Pass=0
I=1
while(I<=Students):
    Marks=int(input("Enter {} Student Marks : ".format(I)))
    if(Marks>100 or Marks<0):
        print("Please Enter Valid Marks :")
        continue
    if(Marks>=40):
        Pass+=1
    I+=1    
print("Percantage Of Passing Students {}%".format((Pass*100)/Students))

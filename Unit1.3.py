#Extracting fields of a roll number using string indexing and slicing.

String = "CS-MCA-22"
#String = input("Enter String : \n");

Department = String[:2]
print(Department) 

Course = String[3:6]
print(Course)  

Roll_no = String[7:]
print(Roll_no) 

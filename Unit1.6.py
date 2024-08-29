#Find the student from CS department where the roll number may be in capital or smallcase Letters.

Rollno=str(input("Enter Your Roll Number : "))

Branch=Rollno[0:2]

if Branch == "Cs" or Branch=="cS" or Branch=="CS" or Branch=="cs":
     print("\n {} Is Computer Scince Department Student : ".format(Rollno))
  
else:
    print("\n{} Is Not Computer Scince Department Student : ".format(Rollno))

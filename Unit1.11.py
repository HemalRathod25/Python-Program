# Check The Positive Integer is prime or Not :

Number = int(input("Enter The Number :"))
if Number > 1:
  
    for i in range(2, (Number//2)+1):
      
        if (Number % i) == 0:
            print(Number, "Is Not A Prime Number")
            break
    else:
        print(Number, "Is A Prime Number")

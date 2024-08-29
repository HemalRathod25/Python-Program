#Print Fibonacci sequence.

N1 , N2 =  0 , 1
Numbers = int(input("Enter Numbers You Want : "))
for i in range(0,Numbers):
    Temp = N1 + N2
    print(N1)
    N1 = N2
    N2 = Temp

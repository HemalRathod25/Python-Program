#Collatz sequence.

Number = int(input("Enter The Number  :"))

while Number != 1:
    if Number % 2 == 0:
        Number = Number // 2
    else:
        Number = (Number*3)+1

    print(Number,end=" ")

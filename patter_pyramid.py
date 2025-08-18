row = 10
for i in range(row):
    for j in range(row - i):
        print(" " , end=" " )
        
    for u in range(i):
        print("*" , end=" ")
    print()
        
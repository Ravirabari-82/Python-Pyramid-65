m=65
row=int(input("Enter the row=>"))
for i in range (1,row+1):
    for j in range (row-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(chr(m),end=" ")
        m=m+1
    print()
    
"""Output-3
     A
   B C D
E F G H I
"""
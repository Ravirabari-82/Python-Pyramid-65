no=int(input("Enter the row =>"))
n=no*2
for i in range(no,0,-1):
    for j in range(1,i+1,1):
        if n%2==0:
            print("",n-1,end="")
            n=n-2
        else :
            print("",n,end="")
            n=n-2
    n=no*2
    print("")
"""Output
Enter the row =>5
 9 7 5 3 1
 9 7 5 3
 9 7 5
 9 7
 9
"""
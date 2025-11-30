n=1
k=2
for i in range(1,5+ 1):
    for j in range(1,i+1):
        print("",n, end="")
        n=n-2
    n=1
    n=n+k
    k=k+2
    print()
"""Output
1
 3 1
 5 3 1
 7 5 3 1
 9 7 5 3 1
"""
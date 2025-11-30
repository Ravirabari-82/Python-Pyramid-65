no=int(input("enter no=>"))
for i in range(1,no):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()
"""Output-6
54321
5432
543
54
5
"""
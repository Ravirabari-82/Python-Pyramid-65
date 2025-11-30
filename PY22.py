row=int(input("Enter row=>"))
for i in range(1,row):
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
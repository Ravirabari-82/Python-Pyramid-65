row=int(input("Enter limit => "))
k=1
for i in range(1, row+1):
    for j in range(1, i+1):
        print(k, end="")
        k=k+1
    print("")
"""Output-4
1
23
456
78910
"""
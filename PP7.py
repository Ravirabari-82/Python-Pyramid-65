rows= int(input("Enter limit => "))
k=2
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(k, end="")
        k=k+2
    print("")
"""Output-4
24
6810
14161820
"""
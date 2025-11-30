row=5
for i in range(row):
    num = 1
    for j in range(row- i):
        print(num, end="")
        num += 2
    print()
"""output
13579
1357
135
13
1
"""
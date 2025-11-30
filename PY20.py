rows=int(input("Enter no of rows=>"))
for i in range(rows,0,-2):
    for j in range(1,i-1):
      print(i,end="")
    print("")
"""output-6
12345
1234
123
12
1
"""
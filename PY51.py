rows=int(input("Enter no of rows=>"))
for i in range(rows,0,-1):
    print(" ",end=" ")
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
      print("*",end=" ")
    print()
for i in range(1,4+1):
	
	for j in range(4-i):
		print(" ",end=" ")
	for k in range(1,2*i):
		print("*",end=" ")
	print()
row=int(input("enter the rows=>"))
for i in range(1,row+1):
	for j in range(row-i):
		print(" ",end=" ")
	for k in range(1,2*i):
		print(k,end=" ")
	print()
"""Output-3
    1
  1 2 3
1 2 3 4 5
"""

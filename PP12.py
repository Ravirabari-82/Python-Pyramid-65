row=int(input("enter the row=>"))
a=65
for i in range(row):
	for j in range(i+1):
		alpha=chr(a)
		print(alpha,end="")
	a+=1
	print("")
	
"""Output-3
A
BB
CCC
"""
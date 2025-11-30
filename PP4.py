rows=int(input("Enter no of rows=>"))
k=1
for i in range(rows,0,-1):
    for j in range(1,i+1):
      print(k,end="")
      k=k+2
    print("")
    
"""Output-3
135
79
11
"""
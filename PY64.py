for i in range(1,6,1):
    for j in range(1,i+1):
        if 4>=j:
           print("",j,end="")
    for k in range(1,2*(5-i),1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        print("",l,end="")
    print()
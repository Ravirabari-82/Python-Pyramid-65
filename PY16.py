no=5*2
k=2
for i in range(5,0,-1):
    for j in range(i,0,-1):
        if no%2==0 :
              print("",no-1,end="")
              no=no-2
        else :
            print("",no,end="")
            no=no-2
    no=5*2
    no=no-k
    k=k+2
    print()
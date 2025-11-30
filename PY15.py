num=1
m=2
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("",num,end="")
        num=num+2
    num=1
    num=num+m
    m=m+2
    print()
"""Output
13579
3579
579
79
9
"""
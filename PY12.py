num=1
k=2
for i in range(1,5+ 1):
    for j in range(1,i+1):
        print("",num, end="")
        num=num-2
    num=1
    num=num+k
    k=k+2
    print()
"""Output-5
1
 3 1
 5 3 1
 7 5 3 1
 9 7 5 3 1
"""

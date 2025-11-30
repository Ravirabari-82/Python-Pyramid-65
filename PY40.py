num=5
for i in range(5, 0, -1):
    for s in range(5-i):
        print(" ", end="")
    for num in range(1, i + 1):
        print(num,end=" ")
        num=num-1
    num=5
    print() 
"""Output
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""
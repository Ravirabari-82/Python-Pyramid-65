for i in range(5,0,-1):
    print(" ",chr(39),end="")
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(5+1-i,0,-1):
        print(" ",chr(92),end="")
    print()
"""Output
'       \
'      \  \
'     \  \  \
'    \  \  \  \
'   \  \  \  \  \
"""
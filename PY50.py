num=1
for i in range(5,0,-1):
    for j in range((5-i)*2):
        print(" ",end="")
    for k in range(i):
    	if i%2==0:
           print("#",end="")	
    	else:
           print("*",end="")	
    num=num+1
    print( )
"""Output
*****
 ####
     ***
      ##
         *
"""
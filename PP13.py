row= int(input("Enter limit => "))
M=65
for i in range(1,row+1):
    
    for j in range(row-i):
        
        print(" ", end=" ")
    for k in range(1,2*i):
    	print(chr(M),end=" ")	
    M+=1
    print( )
 
"""Output-4
       A
     B B B
   C C C C C
D D D D D D D
"""
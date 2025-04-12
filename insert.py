A= [10, 5, 6, 4, 8, 7]
#traverse through the array

for i in range(1, len(A)):
    
    value= A[i]
    
    #Move the elements of A[0... i-1], that are greater than value, to one position ahead of their current position
    
    j= i-1
    while j >=0 and A[j] > value:
        A[j+1]= A[j]
        j-= 1
        A[j+1]= value
        
        
        
print("Sorted Array")
for i in range(len(A)):
    print("%d" %A[i], end= " ")
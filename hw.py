A= list(map(int, input("Enter elements: ").split()))

for i in range(1, len(A)):
    value = A[i]
    j= i-1
    
    while j >=0 and A[j] > value:
        A[j+1] = A[j]
        j-= 1
        A[j+1]= value
        
        
print("Sorted Array")
for i in range(len(A)):
    print("%d" %A[i], end=" ")
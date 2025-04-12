A= [1, 2, 3, 4, 5, 6]
#initialising start and end
start=0
end= len(A)- 1

#reverse A from start to end
while start < end:
    #swapping the elements of an array in the reverse order of the same array
    A[start], A[end]= A[end], A[start]  
    start += 1
    end -= 1
    
print("Reversed Array")
print(A)
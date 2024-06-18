#Bubble Sort

a =  [13,46,24,52,20,9]
for i in range(len(a), 1, -1):
    for j in range(0,i-1):
        if a[j]>a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j]=temp

print("a_final=",a)

'''
Time Complexity is O(n2)

It can be further Optimised if in any iteration swap does not happen then array is sorted

'''

a =  [13,46,24,52,20,9]
for i in range(len(a), 1, -1):
    didSwap = 0
    for j in range(0,i-1):
        if a[j]>a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j]=temp
            didSwap = 1

        if didSwap == 0:
            break

print("a_final=",a)

'''
In this case the time complexity = O(n) the best case
as if the array is already sorted then in first iteration only it will exit the loop
'''
            
    
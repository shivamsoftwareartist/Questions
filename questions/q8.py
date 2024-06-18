#Insertion Sort

a = [8,9,6,14,15,13]

for i in range(len(a)):
    j = i
    while j > 0 and a[j-1]>a[j]:
        temp = a[j-1]
        a[j-1] = a[j]
        a[j] = temp
        j -= 1
        
'''
Time complexity of this code is O(n2)

Best case would be if array is already sorted then O(n)
'''
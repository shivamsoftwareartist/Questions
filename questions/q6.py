# Python program to write Selection sort

a = [19, 12, 34, 4, 6, 1, 14]

def swap(min, i):
    temp = a[min]
    a[min] = a[i]
    a[i] = temp

for i in range(len(a)-1):
    min = i
    for j in range(i, len(a)):
        if a[j] < a[min]:
            min = j
    swap(min, i)

'''
Time complexity of the program
Suppose the length of list a is n
- time for 1st loop is O(n-1)
- time for 2nd loop is O(n-1)

so Total = O(n-1) * O(n-1)
Time Complexity = O(n^2)
 
'''
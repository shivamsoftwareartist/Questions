# Python program to Find Out Pairs with given sum in an array in python of time complexity O(n log n)- FACEBOOK,AMAZON

'''Brute Force Approach'''
def pairs():
    a = [3, -2, 5, 7, 8, 9, 19, 2, 21]
    sum = 17
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j] == sum:
                print(a[i],a[j])

'''
Time complexity of the program
Suppose the length of list a is n
- time for 1st loop is O(n)
- time for 2nd loop is O(n-1)

so Total = O(n) * O(n-1)
Time Complexity = O(n^2)
 
'''
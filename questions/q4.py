# Python program to FIND MISSING NUMBER IN AN ARRAY IN PYTHON
def missing_number():
    a = [1,2,4,5,6]
    n = len(a)
    sum_of_n_numbers = int(n * (n+1) / 2)
    arr_sum = 0
    for i in a:
        arr_sum += i
    
    missing_num = arr_sum - sum_of_n_numbers
    
    print("missing number: ", missing_num)
    
missing_number()

'''
Time complexity of the program
Suppose the length of list a is n
- time to iterate each in list is O(n)

so Time Complexity = O(n)
'''
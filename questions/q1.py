# Python program to find out common letters between two strings

def common_letters():
    str1 = input("Enter first str: ")
    str2 = input("Enter second str: ")
    
    common_letters = set(str1) & set(str2)
    print("common_letters: ",common_letters)
    
common_letters()

'''
Time complexity of the program
Suppose the lenght of input str1 and str2 is n & m
- so time to read the input is O(n+m)
- time to convert each str into set it O(n) & O(m)
- Intersection of string with take O(min(n,m))

so total = O(n+m) + O(n) + O(m) + O(min(n,m))
Time Complexity = O(n+m)
'''
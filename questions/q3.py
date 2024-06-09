#Conversion of two list into Dictionary Using Python

def converted_dict():
    list1 = ['sheetal', 'ramesh', 'suresh']
    list2 = [1,2,3]
    converted_dict = {}
    for i in range(len(list1)):
        converted_dict[list1[i]] = list2[i]
        
    print(converted_dict)

converted_dict()

'''
Time complexity of the program
Suppose the length of list1 is n
- time to iterate each in list1 is O(n)

so Time Complexity = O(n)
'''
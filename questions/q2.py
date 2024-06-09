# Python program to Count the frequency of words appearing in a string Using Python

def freq_words():
    str = input("Enter str: ")
    words_list = str.split()
    words_dict = {} 
    for i in words_list:
        if i not in words_dict.keys():
            words_dict[i]=0
            
        words_dict[i] += 1
        
    print("words_dict: ", words_dict)
    
freq_words()

'''
Time complexity of the program
Suppose the length of input str is n
- so time to read the input is O(n)
- time to split str is O(n)
- time to read iterate each in list is O(n)

so total = O(n) + O(n) + O(n)
Time Complexity = O(n)
'''
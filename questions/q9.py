#Merge Sorting in a recursive way

def merge(nums, low, mid, high):
    temp = []
    left = low          #referring to 0th / first position of left array
    right = mid+1       #referring to 0th / first position of right array

    #Now check if element of left is smaller then element in right and save it in temp
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    '''Codition where two array are of different size then there are some elements remains in any of the arrays'''
    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1
    
    '''Now add temp array to main array nums'''
    for i in range(low, high+1):
        nums[i] = temp[i-low]
    
    print("nums_merge=", nums)  

'''Recursive way to merge'''
def sortArray(nums, low, high):
    if low<high:                    #Base condition or we can say if low >= high means there are more than 1 element
        mid = int((low+high) / 2)
        sortArray(nums, low, mid)
        sortArray(nums, mid+1, high)
        merge(nums, low, mid, high)

    print(nums)
    
nums = [5,2,3,1]
sortArray(nums,0,len(nums)-1)
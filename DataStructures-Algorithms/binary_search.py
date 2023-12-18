
# binary search recursive implementation 
def binary_search(ar,value,start,end):
    if start<=end:
        middle = int((start+end)/2) # finding the middle 
        if value == ar[middle]: 
            return middle
        elif value>ar[middle]:  
            return binary_search(ar,value,middle+1,end)
        elif value<ar[middle]:
            return binary_search(ar,value,start,middle-1)
    else:
        return -1


# binary search while loop implementation  
def binary_search(ar,value):
    start,end = 0,len(ar)-1
    while start<=end:
        mid = int((start+end)/2)
        if value == ar[mid]:
            return mid 
        elif value>ar[mid]:
            start = mid+1 
        elif value<ar[mid]:
            end = mid-1
    else:
        return -1

# first and last occurence of a sorted array 
def find_first_occurence(ar,value,first =True):
    start,end = 0,len(ar)-1
    result = -1 
    while start<=end:
        mid = int((start+end)/2)
        if value == ar[mid]:
            if first == True:
                end = mid -1
            else:
                start = mid+1 
            result = mid 
        elif value <ar[mid]:
            end = mid -1 
        elif value >ar[mid]:
            start = mid+1 
    return result


# finding count of value in a sorted array 
def find_count(ar,value):
    first = find_first_occurence(ar,value)
    last = find_first_occurence(ar,value,first =False)
    if first==-1:
        return -1
    else:
        count = (last -first)+1 
        return count
        
# rotations happend in a sorted array with no duplicates 
def get_rotations(ar,n):
    low,high = 0,n-1
    while low<=high:
        if ar[low]<=ar[high]:  # case 1 
            return low
        else:
            mid = int((low+high)/2)
            next_ = (mid+1)%n 
            prev = (mid+n-1)%n 
        if ar[mid]<=ar[next_] and ar[mid]<=ar[prev]: # case 2 
            return mid
        elif ar[mid]<=ar[high]:
            high = mid-1
        elif ar[mid] >=ar[low]:
            low = mid+1
    return -1                  


# finding index of a value in a circularly sorted array with no duplicates
def circular_search(ar,n,x):
        low = 0; high = n-1
        while low<=high:
            mid = int((low+high)/2)
            if(x==ar[mid]):  # case 1 : found x 
                return mid 
            if (ar[mid]<=ar[high]): # case 2 ; right half is sorted 
                if (x>ar[mid] and x<=ar[high]):
                    low = mid +1 
                else:
                    high = mid -1
            else:
                if (x>=ar[low] and x<ar[mid]):
                    high = mid -1 
                else:
                    low = mid+1
        return -1



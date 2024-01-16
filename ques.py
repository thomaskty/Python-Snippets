
# reversing an array using pointers 
def reverse(ar):
    i = 0 
    j = len(ar)-1
    while i<=len(ar)//2:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1
        j+=1
    return ar 

# reversing an array based on recursion 
def reverse_recur(ar):
    if len(ar)<=1:
        return ar 
    else:
        return reverse_recur(ar[1:])+reverse_recur(ar[:1])

# rotating an array forward by one step 
def rotate_forward(ar):
    for i in range(len(ar)-1):
        ar[0],ar[i+1] = ar[i+1],ar[0]
    return ar

# rotating an array backward by one step 
def rotate_backwards(ar):
    j = len(ar)-1
    i = len(ar)-2
    while i>=0:
        ar[i],ar[j] = ar[j],ar[i]
        i -=1
    return ar



# function helps in merging two splitted arrays
def merge(elements,start,mid,end):
    len1=mid-start+1
    len2=end-mid
    # left and right arrays taken 
    left_array=[0]*len1
    right_array=[0]*len2
    # based on mid , left of mid are stored in leftarray
    for i in range(len1):
        left_array[i]=elements[start+i]
    # right of mid are stored in rightarray 
    for j in range(len2):
        right_array[j]=elements[mid+1+j]
    k=start
    i=0
    j=0
    # comparing both left and right and min val is placed in req array
    while i<len1 and j<len2:
        if left_array[i]<=right_array[j]:
            elements[k]=left_array[i]
            k+=1
            i+=1
        else:
            elements[k]=right_array[j]
            k+=1
            j+=1
    while i<len1:
        elements[k]=left_array[i]
        k+=1
        i+=1
    while j<len2:
        elements[k]=right_array[j]
        k+=1
        j+=1

# this function helps in dividing the problem into simpler problems
def partition(elements,start,end):
    if start<end:
        mid=(start+end)//2
        partition(elements,start,mid)
        partition(elements,mid+1,end)
        merge(elements,start,mid,end)
# taking input as unsorted elements
elements=list(map(int,input().strip().split()))
partition(elements,0,len(elements)-1)
print(elements)

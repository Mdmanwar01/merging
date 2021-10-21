#Implementation of MergeSort in Python
def Display(l):      #Display function
        print(l)

def MergeSort(l):    #MergeSort function
    if len(l)>1:
        mid=len(l)//2

        left=l[0:mid]
        right=l[mid:]

        MergeSort(left)
        MergeSort(right)

        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):     #Merging the values into the list
            if left[i]<right[j]:          
                l[k]=left[i]
                i=i+1
            else:
                l[k]=right[j]
                j=j+1
            k=k+1
        #Merging the remianing values into the list.
        while i<len(left):      
            l[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            l[k]=right[j]
            j=j+1
            k=k+1
def main():
    l=[ ]         #creating a list
    n=int(input("Enter the size of the list:"))
    for i in range(0,n):              #initializing the list
         print("Enter ",i+1," Element of the List:",end="")
         temp=int(input())
         l.append(temp)
    Display(l)       #CAlling Display function
    MergeSort(l)
    print("After merging:")
    Display(l)       #CAlling Display function
    
main()         #calling main function

#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


# In[2]:


def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

print(power(3,4))


# In[4]:


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)


# In[6]:


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

       
        mergeSort(left)
        mergeSort(right)

        
        i = 0
        j = 0
        
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              
              myList[k] = left[i]
             
              i += 1
            else:
                myList[k] = right[j]
                j += 1
           
            k += 1

        
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [29,13,22,37,52,49,46,71,56]
mergeSort(myList)
print(myList)


# In[16]:


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
      
        while low <= high and array[high] >= pivot:
            high = high - 1

        
        while low <= high and array[low] <= pivot:
            low = low + 1

       
        if low <= high:
            array[low], array[high] = array[high], array[low]
           
        else:
            
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array = [29,13,22,37,52,49,46,71,56]
    
quick_sort(array, 0, len(array) - 1)
print(array)


# In[ ]:





# In[ ]:





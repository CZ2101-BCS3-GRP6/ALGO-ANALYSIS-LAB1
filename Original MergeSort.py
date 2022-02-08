#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:03:33 2022

@author: pangchenghao
"""
import numpy as np
from time import process_time

# Python program for implementation of MergeSort
def mergeSort(arr):
    
    keyComp = 0
    
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        keyComp += mergeSort(L)

        # Sorting the second half
        keyComp += mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                keyComp+=1
            else:
                arr[k] = R[j]
                j += 1
                keyComp+=1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return keyComp  # report key comparisons


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
t1_start = process_time() #Get start time

if __name__ == '__main__':
    np.random.seed(0)
    arr = np.random.randint(1,26,10) #Random array failed?
    print("Given array is", end="\n")
    printList(arr)
    kc = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    print("No. of key comparisons: ", kc, end="\n")
print("\n")

if __name__ == '__main__':
    arr = [13, 16, 22, 1, 4, 4, 8, 10, 20, 22 ]
    print("Given array is", end="\n")
    printList(arr)
    kc = mergeSort(arr)
    print("Sorted array with MergeSort is: ", end="\n")
    printList(arr)
    print("No. of key comparisons: ", kc, end="\n")
print("\n")    

if __name__ == '__main__':
    arr = [8,7,5,9,1,7,8,2,8,4]
    print("Given array is", end="\n")
    printList(arr)
    kc = mergeSort(arr)
    print("Sorted array with MergeSort is: ", end="\n")
    printList(arr)
    print("No. of key comparisons: ", kc, end="\n")

t1_stop = process_time() #Get end time
   
 
print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start) #Elapsed Time 

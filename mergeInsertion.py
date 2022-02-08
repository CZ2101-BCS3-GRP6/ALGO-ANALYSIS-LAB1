from time import process_time


def insertMergeSort(arr, S):
    keyComp = 0
    if len(arr) > S:
        mid = len(arr) // 2  # floor division

        left = arr[:mid]
        right = arr[mid:]
        keyComp += insertMergeSort(left, S)
        keyComp += insertMergeSort(right, S)

        # merge
        # index to keep track of arr
        index = 0

        while len(left) > 0 and len(right) > 0:
            keyComp += 1
            if left[0] < right[0]:
                arr[index] = left[0]  # write into arr (sorted array)
                left.pop(0)
                # remove the element from left sublist
            else:
                arr[index] = right[0]  # write into arr (sorted array)
                right.pop(0)
                # remove the element from right sublist
            index += 1

        # Check for remaining elements
        # Only one of these loops will run
        while len(left) != 0:
            arr[index] = left[0]
            left.pop(0)
            index += 1
        while len(right) != 0:
            arr[index] = right[0]
            right.pop(0)
            index += 1
    else:
        # Insertion Sort
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                keyComp += 1
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break

    return keyComp  # report key comparisons


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
t1_start = process_time()  #Get start time

if __name__ == '__main__':
    arr = [12, 11, 13, 8, 5, 6, 7, 10]
    print("Given array is", end="\n")
    printList(arr)
    kc = insertMergeSort(arr, 4)
    print("Sorted array with insertMergeSort is: ", end="\n")
    printList(arr)
    print("No. of key comparisons: ", kc, end="\n")

t1_stop = process_time()  #Get end time

print("Elapsed time during the whole program in seconds:",
      t1_stop - t1_start)  #Elapsed Time

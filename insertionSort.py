def insertion_sort(A):
    for i in range(1, len(A)):
        cur = A[i]
        j = i
        while j > 0 and A[j-1] > cur:  # element Arr[j-1] must be after cur
            A[j] = A[j-1]
            j -= 1
        A[j] = cur



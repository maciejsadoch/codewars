def find_uniq(arr):
    for i in range (len(arr)):
        if arr[i-1] != arr[i-2] and arr[i-1] != arr[i]:
            return arr[i-1]

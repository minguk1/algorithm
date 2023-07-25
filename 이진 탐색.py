def binary_search(arr, n, key):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            print(f"find")
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else :
            start = mid + 1
    print("cant find")
    return -1
arr = [2, 3, 5, 7, 8, 16, 77]
n= len(arr)
print(binary_search(arr, n, 77))
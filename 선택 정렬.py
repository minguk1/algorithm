def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        #반복 다 돌았으면 제일 작은 숫자를 현재 자리 i로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = [10, 25, 5, 31, 44, 26]
n = len(arr)

print(selection_sort(arr, n))

def selection_sort_dec(arr, n):
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if arr[max_idx] < arr[j]:
                max_idx = j
        #반복 다 돌았으면 제일 작은 숫자를 현재 자리 i로 이동
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr
print(selection_sort_dec(arr, n))
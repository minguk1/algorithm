n,m = map(int, input().split())
trees = list(map(int, input().split()))



a = 1
b = sum(trees)

while a <= b:

    mid = (a + b) // 2

    cut_tree = 0

    for tree in trees:
        if tree > mid:
            cut_tree += (tree - mid)

    if cut_tree >= m:
        a = mid + 1
    else:
        b = mid - 1

print(b)
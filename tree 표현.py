'''
4
1 2 1 3 3 4 3 5
'''

n = 5
e = int(input())
tree = list(map(int, input().split()))

#1. 인덱스 번호 : 부모 노드 번호

child_left = [0]*(n+1)
child_right = [0]*(n+1)

for i in range(e):
    parent = tree[i*2]
    child = tree[i*2 + 1]
    if child_left[parent] == 0:
        child_left[parent] = child
    else:
        child_right[parent] = child

print(child_left)
print(child_right)
print("====================")

#2. 인덱스 번호 : 자식 노드 번호

parent = [0] * (n+1)
for i in range(e):
    p = tree[i*2]
    c = tree[i*2 + 1]
    parent[c] = p

print(parent)

#5번 노드 조상 탐색

now = 5
while parent[now] != 0:
    now = parent[now]
print(now)
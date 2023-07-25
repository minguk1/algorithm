'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''



n = int(input())
tree = list(map(int, input().split()))

#인덱스가 부모노드 번호
c_left = [0] * (n+1)
c_right = [0] * (n+1)

for i in range(n-1):
    p = tree[i*2]
    c = tree[i*2 + 1]
    if c_left[p] == 0:
        c_left[p] = c
    else:
        c_right[p] = c

print(c_left)
print(c_right)
pre_list = []
def preorder(t):
    # pre_list.append(t)
    # if c_left[t] != 0:
    #
    #     preorder(c_left[t], pre_list)
    #     if c_right[t] != 0:
    #         preorder(c_right[t], pre_list)
    # else:
    #     return
    if t:
        print(t, end=" ")
        preorder(c_left[t])
        preorder(c_right[t])

preorder(1)
print()



    # t노드가 존재한다면
    # 데이터 처리
    # 왼쪽 노드 방문
    # 오른쪽 노드 방문

def inorder(t, in_list):
    if c_left[t] != 0:
        inorder(c_left[t], in_list)

from collections import deque

# n개의 송전탑 중 연결됨을 표시하는 리스트 배열들이 wires에 주어진다.
# 여기에서 어떤 리스트를 골라 잘라야 할지는 반복문을 돌면서 차이가 가장 작은 것을 골라야 한다.
def solution(n, wires):
    # 전력망 차이의 최대 개수는 n이다.
    min_value = n
    # wires에서 wire는 현재 끊어야 할 리스트 객체이다.
    for wire in wires:
        A = deque()
        B = deque()
        # 방문 리스트를 만들어준다.
        visited = [0] * (n+1)
        visited[wire[0]] = 1
        visited[wire[1]] = 2
        # wire에 각 두 원소에 해당하는 송전탑은 방문을 했다고 표시한다.
        # 또한 각각의 q에 넣어주어 트리들을 다 찾아준다.
        print(wire[0], wire[1])
        A.append(wire[0])
        B.append(wire[1])
        print(A,B, visited)
        # 첫 번째 원소랑 연결되어 있는 것들을 순서대로 찾는다.
        while A:
            # a번째 송전탑에 대해
            a = A.popleft()
            print(a)
            # 다시 wires에 wire가 아닌 리스트 k 중에
            for k in wires:
                if k != wire:
                    # a번째를 포함하고 있다면
                    if (a in k):
                        # 그 리스트 k중 a가 아니라면
                        for l in k:
                            if l != a and visited[l] == 0:
                                # 그 번호가 다음에 연결되어 있는 송전탑의 번호이다.
                                # q에 넣어준다.
                                visited[l] = 1
                                A.append(l)
                                # 이렇게 해서 끝까지 가면 q에 아무 값도 들어가지 않게 되므로 끝이난다.
        # 두번째 원소랑 연결된 송전탑들도 똑같이 구해준다.
        while B:
            b = B.popleft()
            print(b)
            for k in wires:
                if k != wire:
                    print(k)
                    if (b in k):
                        for l in k:
                            if l != b and visited[l] == 0:
                                visited[l] = 2
                                B.append(l)
        print(visited)
        print(visited.count(1), visited.count(2))
        # 현재 wire를 잘라 차이값이 저장된 최솟값보다 작다면 그것으로 갱신한다.
        if abs(visited.count(1)-visited.count(2)) < min_value:
            min_value = abs(visited.count(1)-visited.count(2))
            # 이미 그 차이가 0이면 최솟값이므로 뒤에 경우를 그만해도 된다.
            if min_value == 0:
                break

    answer = min_value
    return answer

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))
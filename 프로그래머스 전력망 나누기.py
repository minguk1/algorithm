from collections import deque

def solution(n, wires):
    min_value = n
    for wire in wires:
        A = deque()
        B = deque()

        visited = [0] * (n+1)
        visited[wire[0]] = 1
        visited[wire[1]] = 2
        print(wire[0], wire[1])
        A.append(wire[0])
        B.append(wire[1])
        print(A,B, visited)
        while A:
            a = A.popleft()
            print(a)
            for k in wires:
                if k != wire:
                    if (a in k):
                        for l in k:
                            if l != a and visited[l] == 0:
                                visited[l] = 1
                                A.append(l)
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
        if abs(visited.count(1)-visited.count(2)) < min_value:
            min_value = abs(visited.count(1)-visited.count(2))
            if min_value == 0:
                break
    answer = -1
    answer = min_value
    return answer

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))
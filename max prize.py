T = int(input())
for tc in range(1, T + 1):

    # 입력 받기
    a, x = map(int, input().split())
    # 입력 받은 수를 문자열화 시키고 리스트로 변경
    prize = list(str(a))

    # 1.
    l = len(prize)

    # 내림차순으로 만들면 주어진 숫자들로 가장 큰 수를 만들 수 있어 미리 최댓값 설정
    answer = sorted(prize, reverse=True)
    # 2.
    change_list = []

    # 리스트 lst 중 원소 두 개의 위치를 한 번 바꿔주는 함수, cnt 는 위에 입력 받은 x가 도달했을 때 끝내주려고 설정
    def change(lst, cnt):
        # 2.
        global change_list
        # 종료조건 : 총 x번 만큼 위치를 바꿔주었으니 현재 리스트를 문자열로 합쳐 다시 출력
        if cnt == x:

            print(f"#{tc} {''.join(lst)}")
            return

        # 이미 최대 상금일 때 ( 6번 케이스처럼 )
        if lst == answer:
            # 같은 원소가 있을 때 그것들끼리만 바꾸면 값에 아무런 영향이 없기 때문에 리스트 그대로 출력
            # 중복된 원소가 있다면 세트로 바꿨을 때와 현재 리스트의 원소 개수가 다르다.
            if len(set(lst)) != len(lst):
                print(f"#{tc} {''.join(lst)}")
                return
            # 중복된 원소가 없어 다른 원소들끼리 무조건 바꾸어야 할 때
            else:
                # 짝수라면 다시 현재 상태로 복구가 가능하니 현재 리스트 출력
                if x % 2 == 0:
                    print(f"#{tc} {''.join(lst)}")
                # 홀수라면 현재 상태에서 변화가 있을 수 밖에 없어 그래도 다음으로 큰 수가 되려면
                # 가장 끝에 작은 수 2개가 위치 하므로 그 두 숫자의 위치를 바꾸어 주면 된다.
                else:
                    lst[-1], lst[-2] = lst[-2], lst[-1]
                    print(f"#{tc} {''.join(lst)}")
                return


        # 아직 최대 상금과 다를 때 ( 보통의 경우 )
        else:
            # 개수를 편하게 세어주기 위해 원소 개수 l 설정 / 위에 1번 주석
            for i in range(l):
                # 최대한 적은 횟수로 가장 큰 수로 만드려면 가장 높은 자리수(가장 왼쪽 자리)를 바꿔주면 된다.
                # 따라서 가장 왼쪽 인덱스부터 미리 설정한 최댓값 answer와 비교하였을 때 다른 숫자가 먼저 나온 인덱스를 바꾼다.
                # i번째 인덱스의 원소가 다를 때
                if answer[i] != lst[i]:
                    # answer의 i번째 원소가 현재 lst에 몇 번째에 있는지 알아야하기 때문에 for문을 반복하여
                    for k in range(l - 1, i, -1):
                        # k 번째 원소가 answer의 i 번째 원소와 같을 때
                        if lst[k] == answer[i]:
                            # 서로 그 위치를 변경
                            lst[i], lst[k] = lst[k], lst[i]
                            # 제일 어려웠던 부분 ;;
                            # 이딴 식으로 하면 5번째 케이스가 답이 88832가 아닌 88823이 나와버린다.
                            # 변경 횟수가 1이라면 82883 이 나와 괜찮겠지만
                            # 변경 횟수가 2라서 2까지 변해야 하는 것을 감안해야 한다.
                            # 이게 888 처럼 같은 수의 몇 번째를 바꿔줘야 하는지 설정해야 할텐데
                            # 절대 그 방법 생각이 안나서
                            # 일단 바꿔주고 2 와 3의 위치를 자동적으로 바꿔주는 방법을 생각해봤다.
                            # 원소들 위치를 바꿔줄 때 마다 바꿔준 인덱스와 그 값을 따로 change_list에 넣어주었다. / 2번 주석
                            # 재귀 함수 모든 곳에 change_list는 통일 시켜야하니 global 사용
                            change_list.append((k, lst[i]))
                            # 과거 재귀함수에 의해 담겨진 change_list의 원소에 대해
                            for idx, pre in change_list:
                                # 그 원소의 값(인덱스 아님, 현재 8)에 대해 현재 바꿔준 값(8)이 같을 때
                                if pre == lst[i]:
                                    # 과거 바뀐 값(3)이 현재 바뀐 값(2)보다 클 때
                                    if lst[k] < lst[idx]:
                                        # 위치 변경
                                        lst[k], lst[idx] = lst[idx], lst[k]

                            break
                    # 위치 변경이 끝나고 최대 상금 되었을때
                    if lst == answer:
                        # 같은 원소 있을 때 - 아까 상황과 동일
                        if len(set(lst)) != len(lst):
                            print(f"#{tc} {''.join(lst)}")
                            return
                        else:
                            # 아직 cnt 값이 증가가 안되어 이번에는 홀수, 짝수가 뒤바뀐다.
                            if (x - cnt) % 2 == 1:
                                print(f"#{tc} {''.join(lst)}")
                            else:
                                lst[-1], lst[-2] = lst[-2], lst[-1]
                                print(f"#{tc} {''.join(lst)}")
                            return
                    # 위치 변경을 하였지만 최대 상금이 되지 못하였을 때
                    else:
                        # 다시 함수 반복 (cnt 증가시키고)
                        change(lst, cnt + 1)
                        return
                else:
                    continue


    change(prize, 0)
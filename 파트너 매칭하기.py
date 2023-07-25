
import random

class ClassHelper:
    def __init__(self, class_list):
        self.list = class_list #리스트 형식으로 받아주기

    def pick(self,n):
        pick_list = [] #n명을 뽑기 전 빈 리스트 만들어줘서 뽑을 때마다 추가해주기

        for i in range(n):
            pick_list.append(random.sample(self.list, k=1))

        return pick_list #뽑은 리스트 반환


    def match_pair(self):
        pair_list = []
        clone_list = []
        for i in self.list:
            clone_list.append(i) #self.list에 영향 안 받도록! clone_list에 복사

        # clone_list = self.list #이렇게 복사해주면 self.list에도 영향

        while True:
            if len(clone_list) == 3: #남은 인원이 3명일 때
                pair_list.append((clone_list[0],clone_list[1],clone_list[2]))
                break
            elif len(clone_list) == 2: #남은 인원이 2명일 때
                pair_list.append((clone_list[0],clone_list[1]))
                break
            else:
                ran1 = random.choice(clone_list) #1명 뽑고 뽑아야 할 리스트에서 그 1명 제거

                clone_list.remove(ran1)
                ran2 = random.choice(clone_list) #한 명 더 뽑고 뽑은 2명 튜플로 묶어서 짝 리스트에 넣어주기

                clone_list.remove(ran2)
                pair_list.append((ran1, ran2))
                # print(pair_list)
                # print(self.list)
        return pair_list #쌓인 짝 리스트 반환











ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
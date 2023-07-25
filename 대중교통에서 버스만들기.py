class PublicTransport:

    get_in_count = 0 #탑승자 수 확인
    get_off_count = 0 #내리는 탑승자 수 확인
    now_passenger = 0 #현재 탑승자 수
    total_fare = 0 #총 운임 비용

    def __init__(self, name, fare): #대중교통 별로 이름과 요금 설정
        self.name = name
        self.fare = fare

    def get_in(self, num): #각 대중교통을 탈 때 탑승자 수 증가, 현재 탑승자 수 증가, 운임 요금 증가
        PublicTransport.get_in_count += num
        PublicTransport.now_passenger += num
        PublicTransport.total_fare += num * self.fare

    def get_off(self, num): #각 대중교통을 내릴 때 내리는 탑승자 수 증가, 현재 탑승자 수 감소
        PublicTransport.get_off_count += num
        PublicTransport.now_passenger -= num

    @classmethod
    def check_passenger(cls): #현재 탑승자 수 출력
        print(PublicTransport.now_passenger)

    @classmethod
    def check_total_fare(cls): #현재 총 운임 비용 출력
        print(PublicTransport.total_fare)

class Bus(PublicTransport):
    limit_passenger = 25 #제한 인원 변수 설정

    def get_in(self, num):
        super().get_in(num) #상위 클래스 메서드에서 정보 가져오고
        if num > Bus.limit_passenger: #조건식만 따로 추가
            print("더 이상 탑승할 수 없습니다.")

bus = Bus("bus",5)

bus.get_in(24) #출력 안됨
bus.get_in(50) #더 이상 탑승할 수 없습니다. 출력
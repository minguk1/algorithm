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

one = PublicTransport("taxi", 5000)
two = PublicTransport("bus", 1000)
three = PublicTransport("subway", 2000)

one.get_in(10)
two.get_in(5)
one.get_off(5)
three.get_in(10)

PublicTransport.check_passenger()
PublicTransport.check_total_fare()
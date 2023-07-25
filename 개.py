class Doggy:


    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1

    def bark(self):
        return f"{self.name} 왈" #개의 이름과 같이 나오도록 설정.

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def get_status(self):
        print(f"태어난 개 : {Doggy.birth_of_dogs} 현재 개 : {Doggy.num_of_dogs}")


maltiz = Doggy("puppy", "maltiz")
buldog = Doggy("fire", "buldog")
maltiz = Doggy("zlzl", "fome")
buldog.get_status()
print(buldog.bark())

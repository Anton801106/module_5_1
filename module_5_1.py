# Домашняя работа по уроку "Атрибуты и методы объекта." Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 18)
h3 = House('Домик в деревне', 2)

h1.go_to(4)
print()
h2.go_to(20)
print()
h3.go_to(2)

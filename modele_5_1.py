class House:
  def __init__(self, name, number_of_floor):
    self.name =name
    self.number_of_floors = number_of_floor
  def go_to(self, new_floor):
    if 0 < new_floor <= self.number_of_floors:
      for floor in range(1, new_floor +1):
        print(floor)
      else:
        print('Нет такого этажа')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Парковка',0)
h1.go_to(5)
h2.go_to(10)
h3.go_to(0)

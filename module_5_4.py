class House ():
    house_history = []
    def __new__(cls, *args, **kwargs):
        House.house_history.append(args[0])
        #print(House.house_history)
        return object.__new__(cls)



    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors
    def go_to(self, new_floor):
        for i in range (1, new_floor + 1):
            if new_floor > self.number_of_floors:
                print('Такого этажа не существует.')
                break
            else:
                print (i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print ("Не можем сравнить объекты разных классов.")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print("Не можем сравнить объекты разных классов.")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print("Не можем сравнить объекты разных классов.")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print("Не можем сравнить объекты разных классов.")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print("Не можем сравнить объекты разных классов.")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print("Не можем сравнить объекты разных классов.")

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self

    def __sub__(self, other):
        if isinstance(other, int) and other < self.number_of_floors:
            self.number_of_floors = self.number_of_floors - other
            return self
        else:
            print ("В доме не может быть отрицательное количество этажей.")

    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors * other
            return self

    def __del__(self):
        return print(f'{self.name} снесен, но останется в истории.')

h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

del h2
del h4

print (House.house_history)
input()



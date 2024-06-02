class House():
    def __init__(self):
        self.number_of_floors = 0

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        print(self.number_of_floors)

Izumrud = House()
Izumrud.setNewNumberOfFloors(10)
print(Izumrud.number_of_floors)

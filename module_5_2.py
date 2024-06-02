class House():
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

Izumrud = House()
Izumrud.setNewNumberOfFloors(10)
print(Izumrud.numberOfFloors)

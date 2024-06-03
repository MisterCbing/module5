class Building():
    def __init__(self):
        self.numberOfFloors = 10
        self.buildingType = 'Монолитный МКД'

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors

Vega = Building()
Gamma = Building()
print(Vega == Gamma)
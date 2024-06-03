class Building():
    total = 0
    def __init__(self):
        Building.total += 1

a = [Building() for _ in range(40)]
print(a)
print(Building.total)

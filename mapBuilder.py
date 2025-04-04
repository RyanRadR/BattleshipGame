
mapSize = 10

board = [[0 for x in range(mapSize)] for y in range(mapSize)]



def loadPreparationMap():
    for i in range(mapSize):
        print("|---|---|---|---|---|---|---|---|---|---|")
        print("|   |   |   |   |   |   |   |   |   |   |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    print("", end="")


from src import constants

bulletList = []


class Bullet:
    @classmethod
    def rmOutOfScreen(cls) -> None:
        global bulletList
        tempList = []

        for point in bulletList:
            if point[0][1] > 0 or point[0][1] < constants.windowHeight:
                tempList.append(point)
        bulletList = tempList

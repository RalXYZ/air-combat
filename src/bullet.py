from src import constants

bulletList = []


class Bullet:
    shootSpeed = 0.2
    relativeSpeed = 0.05

    @classmethod
    def removeOutside(cls) -> None:
        global bulletList
        tempList = []

        for point in bulletList:
            if point[0][1] > 0 or point[0][1] < constants.windowHeight:
                tempList.append(point)
        bulletList = tempList

    @classmethod
    def fly(cls) -> None:
        global bulletList
        for point in bulletList:
            point[0][0] += point[1][0] * 0.05
            point[0][1] += point[1][1] * 0.05
            point[0][1] -= 0.2

    @classmethod
    def display(cls, screen, bulletImg) -> None:
        global bulletList
        for point in bulletList:
            screen.blit(bulletImg, (int(point[0][0]), int(point[0][1])))

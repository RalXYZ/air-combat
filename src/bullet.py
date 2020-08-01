bulletList = []


class Bullet:
    @classmethod
    def rmOutOfScreen(cls) -> None:
        global bulletList
        tempList = []

        for point in bulletList:
            if point[1] > 100:
                tempList.append(point)
            else:
                pass;
        bulletList = tempList

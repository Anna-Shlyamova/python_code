class HouseScheme:
    def __init__(self, rooms, livearea, wc):
        if livearea < 0 or type(livearea) != int or type(rooms) != int or type(wc) != bool:
            raise ValueError("Invalid value")
        self.rooms = rooms
        self.livearea = livearea
        self.wc = wc


class CountryHouse(HouseScheme):
    def __init__(self, rooms, livearea, wc, floors, landarea):
        if landarea < 0 or type(landarea) != int or type(floors) != int:
            raise ValueError("Invalid value")
        super().__init__(rooms, livearea, wc)
        self.floors = floors
        self.landarea = landarea

    def __str__(self):
        return "Country House: " + "Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество этажей {}, Площадь участка {}.".format(self.rooms, self.livearea, self.wc, self.floors, self.landarea)

    def __eq__(self, add):
        if self.livearea != add.livearea:
            return False
        if self.landarea != add.landarea:
            return False
        if add.floors < self.floors - 1 or add.floors > self.floors + 1:
            return False
        return True


class Apartment(HouseScheme):
    def __init__(self, rooms, livearea, wc, floors, windows):
        if floors < 1 or floors > 15:
            raise ValueError("Invalid value")
        if windows not in "NSWE":
            raise ValueError("Invalid value")
        self.floors = floors
        self.windows = windows
        super(Apartment, self).__init__(rooms, livearea, wc)

    def __str__(self):
        return "Apartment: " + "Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, Окна выходят на {}.".format(self.rooms, self.livearea, self.wc, self.floors, self.windows)


class CountryHouseList(list):

    def __init__(self, name):
        self.name = name
        super(CountryHouseList, self).__init__()

    def append(self, p_object):
        if type(p_object) == CountryHouse:
            super(CountryHouseList, self).append(p_object)
        else:
            raise TypeError("Invalid type " + str(type(p_object)))

    def total_square(self):
        sum = 0
        for i in self:
            sum += i.livearea
        return sum


class ApartmentList(list):
    def __init__(self, name):
        self.name = name
        super(ApartmentList, self).__init__()

    def extend(self, iterable):
        for i in iterable:
            if type(i) == Apartment:
                super(ApartmentList, self).append(i)

    def floor_view(self, floors, directions):
        infloor = lambda objFloors, floor: objFloors.floors in range(floor[0], floor[1] + 1)
        inside = lambda objDirect, direct: objDirect.windows in direct
        filtred = list(filter(lambda obj: infloor(obj, floors) and inside(obj, directions), self))
        for i in filtred:
            print(i.windows, i.floors, sep=": ")
class Transport:
    def __init__(self, mode, name, color, position):
        self.mode = mode
        self.name = name
        self.color = color
        self.position = position

    def motion(self, value_km):
        self.position += value_km
        return self.position


class AirPlane(Transport):

    def __init__(self, name='airplane', mode='air', color='white', position=1, wheels=6, environment='land'):
        super().__init__(mode, name, color, position)
        self.wheels = wheels
        self.environment = environment

    def __str__(self):
        return 'name = {}, environment= {} , mode= {} , color = {}, position= {} km' \
            .format(self.name, self.environment, self.mode, self.color, self.position)

    def landing(self):
        if self.environment == 'air':
            self.environment = 'land'
            return f"airplane are on {self.environment}"
        else:
            return "airplane has already landed"


class Train(Transport):

    def __init__(self, name='train', mode='land', color='black', position=1, number_of_cars=14):
        super().__init__(mode, name, color, position)
        self.number_of_cars = number_of_cars

    def __str__(self):
        return 'name = {}, number_of_cars= {} , mode= {} , color = {}, position= {} km)' \
            .format(self.name, self.number_of_cars, self.mode, self.color, self.position)

    def unhook_cars(self, quantity):
        self.number_of_cars -= quantity
        return self.number_of_cars


air_plane = AirPlane()
train = Train()

print(air_plane.landing())
print(air_plane)
air_plane.motion(150)
print(air_plane)
print(train)
train.unhook_cars(4)
train.motion(27)
print(train)

class Car(object):
    def car(self):
        raise NotImplementedError()


class German(Car):
    def car(self):
        print ('BMW')


class Japan(Car):
    def car(self):
        print ('Toyota')


class CreateCar(object):
    def create_car(self, type_):
        raise NotImplementedError()


class MyCreateCar(CreateCar):
    def create_car(self, type_):
        if type_ == 'German':
            return German()
        elif type_ == 'Japan':
            return Japan()
        else:
            return Car()


car1 = MyCreateCar()
car1.create_car('German').car()
car1.create_car('Japan').car()
try:
    car1.create_car('Russian').car()
except:
    print("NotImplementedError")

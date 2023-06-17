class Cup:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self._name

class Teapot:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self._name

class KeramicCup(Cup):
    def method_1(self):
        print(f"Keramic cup ({self.name})")

class KeramicTeapot(Teapot):
    def method_1(self):
        print(f"Keramic teapot ({self.name})")

class GlassCup(Cup):
    def method_1(self):
        print(f"Glass cup ({self.name})")

class GlassTeapot(Teapot):
    def method_1(self):
        print(f"Glass teapot ({self.name})")

class FurnitureFactory:
    
    def create_cup(self):
        pass

    def create_teapot(self):
        pass

class KeramicFurnitureFactory(FurnitureFactory):
    
    def create_cup(self, name):
        return KeramicCup(name)

    def create_teapot(self, name):
        return KeramicTeapot(name)

class GlassFurnitureFactory(FurnitureFactory):
    
    def create_cup(self, name):
        return GlassCup(name)

    def create_reapot(self, name):
        return GlassTeapot(name)


keramic_factory = KeramicFurnitureFactory()
keramic_cup = keramic_factory.create_cup("Cup 'HUG'-k")
keramic_teapot = keramic_factory.create_teapot("Keramic teapot")
keramic_cup.method_1()  
keramic_teapot.method_1()

glass_factory = GlassFurnitureFactory()
glass_cup = glass_factory.create_cup("Cup 'HUG'-g")
glass_teapot = glass_factory.create_teapot("Glass teapot")
glass_cup.method_1()  
glass_teapot.method_1()
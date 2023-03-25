import math

print(math.pi)

class Cylinder():
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius

    def get_surface_area(self):
        self.surface_area = 2 * math.pi * self.radius * (self.height + self.radius)
        return round(self.surface_area, 2)
    
    def get_volume(self):
        self.volume = math.pi * self.radius**2 * self.height
        return round(self.volume, 2)


cylinder_1 = Cylinder(5, 3)

print("Surface area: ", cylinder_1.get_surface_area())
print("Volume: ", cylinder_1.get_volume())

#%%



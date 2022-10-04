class Car:
    
    def __init__(self, **kwargs):
        self.brand = kwargs.get('brand')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')
        

car = Car(brand='Nissan', model='Skyline', seats=10, color='Black')
print(car.brand, car.model, car.color, car.seats)
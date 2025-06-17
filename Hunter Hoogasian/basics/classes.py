class Vehicle:

    # constructor
    def __init__(self, wheel_count, vehicle_seat_count):
        self.num_wheels = wheel_count
        self.num_tires = wheel_count
        self.num_seats = vehicle_seat_count

class Car(Vehicle):

    # constructor
    def __init__(self, car_seat_count):
        super().__init__(wheel_count=4, vehicle_seat_count=car_seat_count)

class Sedan(Car):

    # constructor
    def __init__(self):
        super().__init__(car_seat_count=5)
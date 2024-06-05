from car import Car
import random


class RandomCars:
    def __init__(self):
        self.random_cars = []
        self.i = 0

    def move(self):
        if self.i == 5:
            self.generate_new_cars()
            self.i = 0
        for car in self.random_cars:
            car.forward(10)
        self.i += 1

    def generate_new_cars(self):
        c = Car()
        c.goto(x=random.randint(300, 350), y=random.choice(range(-243, 265, 30)))
        self.random_cars.append(c)

    def reset(self):
        for car in self.random_cars:
            car.reset()

        self.random_cars = []

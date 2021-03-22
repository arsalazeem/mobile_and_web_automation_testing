import json
import pdb


class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin




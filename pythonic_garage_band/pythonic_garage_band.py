#!/usr/bin/env python3
class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    name = ["Joan Jett", "Jimi Hendrix", "Meshell Ndegeocello", "Sheila E."]

    instruments = []
    # def get_instrument(self):
    #     return instruments

class Guitarist(Musician):
    def __init__(self, name, instruments=[]):
        self.name = name
        self.instruments = instruments

    def __str__(self):
        return f'My name is {self.name} and I play {self.instruments}'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return f"guitar"

class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

class Drummer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


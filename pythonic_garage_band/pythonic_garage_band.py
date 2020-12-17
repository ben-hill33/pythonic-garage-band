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
    def __init__(self, name, instrument, instance):
        self.name = name
        self.instrument = instrument
        self.instance = instance

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f"{self.instance} instance. Name = {self.name}"

    def get_instrument(self):
        return f'{self.instrument}'



class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitar', 'Guitarist')




class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'bass', 'Bassist')


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drums', 'Drummer')

# if __name__ == "__main__":

# Lab: 04 - Classes and Fixtures

## Project: Garage Band with OOP

### Author: Ben Hill

### Links and Resources

- [Pull Request URL](https://github.com/ben-hill33/pythonic-garage-band/pull/1)
- [Supercharge your Classes with Python super()](https://realpython.com/python-super/)
  - Inspiration for extending the Musician class so that Guitar, Bass, and Drums will inherit all the things

### Setup

This program uses python-poetry for dependency package manager. In order to create this project, follow the python-poetry link in the Links and Resources section above and install poetry.

How to initialize/run your application
Now that your program is scaffolded you can run poetry virtual environment. To initialize, run this command in CLI: ```$ poetry shell``` To check output: ```$ python example_name.py```

### Feature Tasks and Requirements

Use Python classes to model a Band made up of different kinds of musicians.

Start with Guitarist,Bassist, and Drummer.

Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

### User Acceptance Tests

- Unit tests will be supplied for this lab. Your job is to make them pass. Do NOT modify the supplied tests (except to enable for stretch goals.)

### Band Tests

- [ ] A Band instance should have a name attribute which is a string.
- [ ] A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
- [ ] A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
- [ ] A Band instance should have appropriate __str__ and __repr__ methods.
- [ ] A Band should have a class method to_list which returns a list of previously created Band instances

### Musician Subclass Tests

- [x] Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
- [x] Each kind of Musician instance should have a get_instrument method that returns string.
- [ ] Each kind of Musician instance should have a play_solo method that returns string.

#### Stretch

See tests marked “stretch” in supplied test suite.
Make Musician “abstract” - aka an Abstract Base Class
Add your own tests.

### Tests

Tests were pre-written by Code Fellows faculty. The goal of this assignment was write code based on the error output of each test ran individually.

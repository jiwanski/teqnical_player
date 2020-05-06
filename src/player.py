from random import randint
from src.exceptions import ClubNotSetException


class Player:

    def __init__(self, name: str, position: str, age: int):
        self._age = age
        self._position = position
        self._name = name
        self._field_number = 0
        self._goals = 0
        self._club = None
        self._cards = 0

    def get_goals(self):
        return self._goals

    def get_club(self):
        return self._club

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_field_number(self):
        return self._field_number

    def set_field_number(self, number):
        self._field_number = number

    def get_cards(self):
        return self._cards

    def get_position(self):
        return self._position

    def score(self):
        if self._club is not None:
            self._goals += 1
        else:
            raise ClubNotSetException("choose your club!")

    def change_position(self, position):
        self._position = position
        self._age += 2

    def foul(self):
        if randint(0, 1):
            print("got a card!")
            self._cards += 1

    def transfer(self, club):
        self._club = club
        self._goals = 0

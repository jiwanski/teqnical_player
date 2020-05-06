import pytest
import pytest_check as check
from src.player import Player

params = [
    (Player("Ronaldinho", "attacker", 23), {"age": 23, "goals": 0, "cards": 0,
                                            "position": "attacker", "name": "Ronaldinho",
                                            "club": None, "field_number": 0}),
    (Player("Pele", "defender", 20), {"age": 20, "goals": 0, "cards": 0,
                                      "position": "defender", "name": "Pele",
                                      "club": None, "field_number": 0}),
    (Player("Garrincha", "goalkeeper", 19), {"age": 19, "goals": 0, "cards": 0,
                                             "position": "goalkeeper", "name": "Garrincha",
                                             "club": None, "field_number": 0})
]


@pytest.mark.parametrize("data, expected", params)
def test_params(data, expected):
    check.equal(data.get_age(), expected["age"])
    check.equal(data.get_goals(), expected["goals"])
    check.equal(data.get_cards(), expected["cards"])
    check.equal(data.get_position(), expected["position"])
    check.equal(data.get_name(), expected["name"])
    check.is_none(data.get_club())
    check.equal(data.get_field_number(), expected["field_number"])

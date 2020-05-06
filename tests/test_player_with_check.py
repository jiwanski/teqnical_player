import pytest_check as check
from src.player import Player


def test_initial_values_for_user():
    p = Player("Ronaldinho", "attacker", 23)
    check.equal(p.get_age(), 23)
    check.equal(p.get_goals(), 0)
    check.equal(p.get_cards(), 0)
    check.equal(p.get_position(), "attacker")
    check.equal(p.get_name(), "Ronaldinho")
    check.is_none(p.get_club())
    check.equal(p.get_field_number(), 0)

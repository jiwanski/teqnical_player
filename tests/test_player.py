import pytest
from src.exceptions import ClubNotSetException
from src.player import Player


@pytest.fixture()
def p():
    return Player("Ronaldinho", "attacker", 23)


def test_new_player_age(p):
    assert p.get_age() == 23


def test_new_player_goals(p):
    assert p.get_goals() == 0


def test_score_with_club(p):
    p.transfer("Barcelona")
    p.score()
    assert p.get_goals() == 1


def test_score_without_club(p):
    with pytest.raises(ClubNotSetException, match=r"^choose your club!$"):
        p.score()
    assert p.get_goals() == 0


def test_change_position(p):
    age = p.get_age()
    p.change_position("superstar")
    assert p.get_position() == "superstar"
    assert p.get_age() - age == 2


def test_transfer(p):
    p.transfer("Monaco")
    assert p.get_club() == 'Monaco'
    for _ in range(10):
        p.score()
    assert p.get_goals() > 0
    p.transfer("Fiorentina")
    assert p.get_club() == 'Fiorentina'
    assert p.get_goals() == 0


def test_transfer_same_club(p):
    assert p.get_club() is None
    p.transfer("Fiorentina")
    p.transfer("Fiorentina")
    assert p.get_club() == 'Fiorentina'


def test_transfer_empty_club(p):
    assert p.get_club() is None
    p.transfer("")
    assert p.get_club() == ''


def test_foul(p, capsys):
    for _ in range(10):
        cards = p.get_cards()
        p.foul()
        assert p.get_cards() - cards in (0, 1)
        captured = capsys.readouterr()
        assert captured.out in ('got a card!\n', '')

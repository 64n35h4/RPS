from models.player import PlayerEnum


def test_entity():
    player = PlayerEnum
    assert player.USER.value == 0
    assert player.COMPUTER.value == 1
    assert player.TIE.value == -1

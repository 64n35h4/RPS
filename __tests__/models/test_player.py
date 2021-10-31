from models.entity import EntityEnum


def test_entity():
    entity = EntityEnum
    assert entity.ROCK.value == 0
    assert entity.PAPER.value == 1
    assert entity.SCISSORS.value == 2

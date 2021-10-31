from enum import Enum


class TEntity(Enum):

    @classmethod
    def get_values(cls):
        return [x.value for x in cls]

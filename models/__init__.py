from enum import Enum


class TEntity(Enum):

    @staticmethod
    def get_values():
        return [x.value for x in TEntity]
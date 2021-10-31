
class Rules:

    @staticmethod
    def build_winning_matrix():
        return [
            [-1, 1, 0],
            [1, -1, 2],
            [0, 2, -1]
        ]

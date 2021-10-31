from actions.rules import Rules


def test_build_winning_matrix():
    winning_matrix = Rules.build_winning_matrix()
    assert winning_matrix == [
            [-1, 1, 0],
            [1, -1, 2],
            [0, 2, -1]
        ]

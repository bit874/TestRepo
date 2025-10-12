import pytest
from streak import longest_positive_streak

@pytest.mark.parametrize("nums,expected", [
    ([], 0),                         # empty
    ([1, 1, 1], 3),                  # single streak
    ([2, 3, -1, 5, 6, 7, 0, 4], 3),  # multiple streaks; longest=3
    ([0, -1, 2, 2, 0, 3, 3, 3], 3),  # zeros/negatives break
    ([-5, -1, 0], 0),                # all non-positive
    ([1, 0, 1, 1, 0, 1, 1, 1], 3),   # scattered
])
def test_longest_positive_streak(nums, expected):
    assert longest_positive_streak(nums) == expected

import pandas as pd

from src.features import add_rush_flag


def test_add_rush_flag():
    # YOUR CODE: build a small DataFrame with hours 17, 18, 20 and 21 (just outside and exactly on the edges),
    # call add_rush_flag on it, and assert that the `rush` column equals the answer YOU worked out by hand.
    raise NotImplementedError


def test_add_rush_flag_does_not_change_the_input():
    df = pd.DataFrame({"hour": [17, 19]})
    add_rush_flag(df)
    assert list(df.columns) == ["hour"]          # the original table is untouched

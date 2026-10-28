import glob

import pandas as pd
from conftest import LAB

from src.checks import COLUMNS, RESTAURANTS, problems


def test_base_data_schema_and_ranges(base):
    df = base
    assert list(df.columns) == COLUMNS
    assert not df.isna().any().any()
    # YOUR CODE (gap 1): every distance_km is between 0.1 and 50
    # YOUR CODE (gap 2): every restaurant is one of RESTAURANTS
    # YOUR CODE (gap 3): the late rate (the mean of `late`) is between 0.05 and 0.40
    raise NotImplementedError


def test_incoming_batches_pass_the_data_checks():
    """Any new file placed in data/incoming/ must pass the same checks before we train on it."""
    for path in sorted(glob.glob(str(LAB / "data" / "incoming" / "*.csv"))):
        found = problems(pd.read_csv(path))
        assert found == [], f"{path}: {found}"

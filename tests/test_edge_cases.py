# Small sanity tests—keep these lightweight and readable.

import pandas as pd

def test_zero_ab_is_nasafe():
    df = pd.DataFrame({"AB":[0],"H":[0],"2B":[0],"3B":[0],"HR":[0],"BB":[0],"HBP":[0],"SF":[0],"player":["X"]})
    ab = df["AB"].replace(0, pd.NA)
    assert ab.isna().iloc[0]


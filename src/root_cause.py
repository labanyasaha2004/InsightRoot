import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


def analyze_dimension(df, dimension, before_month=4, after_month=5):

    before = df[df["date"].dt.month == before_month]
    after = df[df["date"].dt.month == after_month]

    result = pd.DataFrame({
        "revenue_before": before.groupby(dimension)["revenue"].sum(),
        "revenue_after": after.groupby(dimension)["revenue"].sum(),

        "units_before": before.groupby(dimension)["units_sold"].sum(),
        "units_after": after.groupby(dimension)["units_sold"].sum(),

        "visits_before": before.groupby(dimension)["website_visits"].sum(),
        "visits_after": after.groupby(dimension)["website_visits"].sum(),

        "conversion_before": before.groupby(dimension)["conversion_rate"].mean(),
        "conversion_after": after.groupby(dimension)["conversion_rate"].mean()
    })

    result["revenue_change_%"] = (
        (result["revenue_after"] - result["revenue_before"])
        / result["revenue_before"] * 100
    )

    result["units_change_%"] = (
        (result["units_after"] - result["units_before"])
        / result["units_before"] * 100
    )

    result["visits_change_%"] = (
        (result["visits_after"] - result["visits_before"])
        / result["visits_before"] * 100
    )

    result["conversion_change_%"] = (
        (result["conversion_after"] - result["conversion_before"])
        / result["conversion_before"] * 100
    )

    return result
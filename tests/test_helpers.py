import pandas as pd
from src.data import to_long_format, merge_indicators, filter_years
from src.modeling import prepare_features, regression_metrics


def test_reshape_merge():
    source = pd.DataFrame({"Country Name": ["A"], "Country Code": ["AAA"], "2001": [10.0], "2002": [20.0]})
    assert to_long_format(source)["year"].tolist() == [2001, 2002]
    joined = merge_indicators({"gdp_per_capita": source, "life_expectancy": source})
    assert len(joined) == 2
    assert len(filter_years(joined, 2002, 2002)) == 1


def test_feature_transform():
    source = pd.DataFrame({"country_name": ["A"], "country_code": ["AAA"], "year": [2020], "gdp_per_capita": [100.0], "population": [1000.0], "life_expectancy": [72.0]})
    result = prepare_features(source)
    assert "log_gdp_per_capita" in result
    assert regression_metrics([72, 74], [72, 74])["mae"] == 0

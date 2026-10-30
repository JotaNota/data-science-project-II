"""World Bank indicator preparation helpers."""
import pandas as pd

KEYS = ["country_name", "country_code", "year"]


def to_long_format(df: pd.DataFrame) -> pd.DataFrame:
    """Convert World Bank year columns into country-year rows."""
    years = [c for c in df.columns if isinstance(c, str) and c.isdigit()]
    if not years:
        raise ValueError("No year columns were found")
    return (df.melt(id_vars=["Country Name", "Country Code"], value_vars=years,
                    var_name="year", value_name="value")
              .rename(columns={"Country Name": "country_name", "Country Code": "country_code"})
              .assign(year=lambda d: d["year"].astype(int)))


def merge_indicators(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Outer-join wide-form World Bank indicator tables."""
    if not tables:
        raise ValueError("Provide at least one indicator")
    result = None
    for name, table in tables.items():
        values = to_long_format(table).rename(columns={"value": name})
        result = values if result is None else result.merge(values, on=KEYS, how="outer", validate="one_to_one")
    return result


def filter_years(df: pd.DataFrame, start: int = 2001, end: int = 2024) -> pd.DataFrame:
    return df.loc[df["year"].between(start, end)].copy()

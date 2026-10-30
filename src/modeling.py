"""Feature engineering and regression metrics."""
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

FEATURES = ["log_gdp_per_capita", "log_population", "year"]
TARGET = "life_expectancy"


def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """Produce the feature columns from the notebook's cleaned country-year data."""
    result = df.copy()
    result["log_gdp_per_capita"] = np.log1p(result["gdp_per_capita"])
    result["log_population"] = np.log1p(result["population"])
    columns = ["country_name", "country_code", "year", "gdp_per_capita",
               "population", *FEATURES[:2], TARGET]
    return result[columns].dropna().copy()


def regression_metrics(y_true, y_pred) -> dict[str, float]:
    """Calculate the notebook's regression evaluation metrics."""
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "r2": float(r2_score(y_true, y_pred)),
    }

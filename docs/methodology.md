# Methods and limitations

## Study design

The original Coderhouse notebook analyzes World Bank country-year observations for GDP per capita (PPP), life expectancy, population, and literacy (during data preparation). It transforms wide-form indicator tables, merges indicators, explores relationships, and evaluates regression models.

The `src/` helpers extract selected transformations for reuse. They are **not wired into the original notebook**; the notebook remains an unchanged course submission.

## Evaluation limits

The notebook uses random training/test splits of country-year rows. Observations for the same country across years can therefore appear in both datasets. The reported test errors should not be interpreted as validated performance on completely new countries or on future years. Country-grouped and time-ordered validation would be useful improvements.

An observational association between GDP and life expectancy does not establish causation. Missing data and differences in indicator coverage can affect the sample. Aggregate-region exclusion should also be rechecked using official World Bank country metadata.

## Reproducibility

The original notebook retrieves source CSVs using personal Drive URLs embedded in its code. Those links may need accessible replacements before the analysis can be reproduced by third parties. The extracted helpers have unit tests, but no standalone end-to-end execution entry point yet.

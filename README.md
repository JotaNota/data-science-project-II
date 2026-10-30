# Economic Development and Life Expectancy | World Bank Data

**Author:** Juan Díaz  
**Project:** Data Science II — Coderhouse (2026)  
**[Open the notebook in Google Colab](https://colab.research.google.com/drive/1N3rm2gzG9-hM8SBQndbO89il0SeA3Dt-)**

## Research question

How is GDP per capita associated with life expectancy across countries, and how well can economic, demographic, and temporal variables predict life expectancy?

## Dataset

Public World Bank indicators:
- GDP per capita (PPP)
- Life expectancy
- Population
- Literacy (examined during data preparation)

## Methods

Python, pandas, NumPy, matplotlib, and scikit-learn.

The notebook covers data preparation and merging, exploratory analysis, visualization, regression models, model comparison, cross-validation, and hyperparameter tuning.

## Reported model performance

| Model | Test MAE (years) |
| --- | ---: |
| Linear Regression | 3.52 |
| Random Forest | 1.95 |
| Tuned Random Forest | 1.93 |

These results are from the notebook's evaluation setup, and are not guarantees of accuracy on unseen countries or later years.

## Limitations

- The analysis is observational; associations do not establish causation.
- Multiple observations for each country across years can appear in randomly split training and test sets. Grouped country-based and time-based evaluation should be tested.
- Coverage and missingness vary by indicator and country.
- The original notebook downloads input CSVs from Google Drive; execution depends on continued access to those files.

## How to run

Open `world_bank_life_expectancy.ipynb` in Jupyter or Google Colab and run the cells in order.

## Source

World Bank, World Development Indicators. See the notebook for data processing and analysis.

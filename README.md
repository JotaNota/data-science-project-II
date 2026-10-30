# Economic Development and Life Expectancy | World Bank Data

**Author:** Juan Díaz  
**Course:** Data Science II — Coderhouse (2026)

## Research question

How is GDP per capita associated with life expectancy, and how well can economic, demographic, and temporal indicators predict life expectancy across countries?

## Project links

- **[View the notebook on GitHub](world_bank_life_expectancy.ipynb)** — visitors can read it without editing.
- **[Open the read-only Colab copy](https://colab.research.google.com/drive/1V4OqpheECEK47VhAJdFNf3ScyUok_inj)** — access verified as “anyone with the link: reader” on October 30, 2026.

## Data and analysis

Source: World Bank, World Development Indicators. Indicators include GDP per capita (PPP), life expectancy, population, and literacy (examined during preparation).

The notebook uses Python (pandas, NumPy, matplotlib, scikit-learn) for data preparation, exploratory data analysis, visualizations, regression modeling, cross-validation, and Random Forest hyperparameter tuning.

## Reported results

| Model | Test MAE (years) |
| --- | ---: |
| Linear Regression | 3.52 |
| Random Forest | 1.95 |
| Tuned Random Forest | 1.93 |

These figures come from the course notebook. They do not establish causality or guarantee generalization to new countries or future years.

## Repository layout

- `world_bank_life_expectancy.ipynb`: course notebook (identical to the read-only Colab copy).
- `src/data.py`: wide-to-long reshaping, indicator merging and year filtering.
- `src/modeling.py`: feature engineering and regression evaluation.
- `tests/`: small tests for the extracted helpers.
- `docs/methodology.md`: limitations and reproducibility notes.
- `requirements.txt`: dependencies.

## Running the project

Open the notebook in Google Colab or Jupyter. Its source CSVs are fetched from Drive links within the notebook and must be accessible to reproduce its analysis.

To run the extracted modules' tests from the repository root:

```bash
pip install -r requirements.txt
python -m pytest
```

The extracted helpers are standalone utilities and the notebook has not been refactored to import them. See [methodology and limitations](docs/methodology.md).

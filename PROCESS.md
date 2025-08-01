# 🏌️ golf-performance-analysis - Project Development Log

## 🔧 Setup Steps

1. Installed Poetry and set up project dependencies via `pyproject.toml`.
2. Initialized local Git repository and connected to remote (GitHub).
3. Downloaded PGA Tour dataset from Kaggle and placed it in `data/raw/`.

## 📈 Project Pipeline Overview

[1] Data Ingestion  → `src/data_io.py`
    • `load_golf_data()`        → Loads and filters raw tournament-level CSV data.
    • Handles column selection and datetime parsing.

[2] Data Cleaning  → `src/preprocessing.py`
    • `clean_data(df)`          → Drops duplicates, handles nulls, ensures correct datatypes.

[3] Metrics Computation  → `src/metrics.py`
    • `average_strokes(df)`     → Computes average number of strokes.
    • `sg_category_means(df)`   → Averages strokes gained per skill category.

[4] Statistical Analysis  → `src/statistics.py`
    • `compute_correlations(df)` → Computes Pearson correlation matrix.
    • `simple_linear_regression(df)` → Fits linear model (e.g., SG Total → Strokes).
    • `plot_correlation_heatmap(df)` → Seaborn heatmap of correlation matrix.

[5] Data Visualization  → `src/visualization.py`
    • `plot_and_save_correlation_heatmap()` → Saves correlation matrix as PNG.
    • `save_linear_regression_plot()`       → Saves regression chart (X vs Y).

[6] Testing & Validation  → `tests/`
    • Unit tests for cleaning and metrics functions.
    • Run with `pytest`.

[7] Future Steps – Web Dashboard
    • Streamlit app or CLI interface to upload data and view interactive charts.

[8] Packaging & Deployment
    • Optional: containerize with Docker, deploy via Streamlit Cloud or Heroku.

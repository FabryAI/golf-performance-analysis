![Correlation Heatmap](assets/presentation_image.png)

# ⛳ Golf Performance Analysis

**Exploratory Data Analysis (EDA)** and visualization on professional golf data using Python and modern data tools.

This project explores strokes gained metrics from PGA Tour tournaments and analyzes performance trends using statistical methods and visualizations.

---

## 📊 Example Visualizations

### Correlation Heatmap  
Shows how strokes gained metrics relate to each other and to total strokes:

![Correlation Heatmap](assets/correlation_heatmap.png)

### Linear Regression  
Simple regression between `SG Total` and `Strokes`:

![Linear Regression](assets/linear_regression_sg_total_vs_strokes.png)

---

## 🚀 Features

- Load and clean raw golf tournament data (PGA Tour level)
- Compute key performance metrics: average strokes, strokes gained breakdowns
- Statistical analysis: correlation matrix, linear regression
- Visualization: heatmaps and regression plots
- Organized in a modular, testable codebase using **Poetry**

---

## 📁 Project Structure

- `data/raw/` – Original CSV file
- `outputs/plots/` – Saved visualizations
- `src/`
  - `data_io.py` – Load and filter raw data
  - `preprocessing.py` – Data cleaning
  - `metrics.py` – Compute statistics
  - `statistics.py` – Correlations & regression
  - `visualization.py` – Save plots to disk
- `tests/` – Unit tests (optional)
- `main.py` – Main pipeline script
- `pyproject.toml` – Poetry configuration



---

## 🛠️ Technologies Used

- Python 3.11
- pandas
- seaborn
- matplotlib
- scikit-learn
- Poetry for dependency management

---

## 📦 Setup & Usage
Clone the repo
git clone https://github.com/your-username/golf-performance-analysis.git
cd golf-performance-analysis

Install dependencies with Poetry
poetry install

Run the analysis
poetry run python main.py

## 📈 Dataset
Dataset downloaded from Kaggle: All PGA Tour Data (Tourn Level)

Fields include:

Player names, dates, tournament info

Strokes Gained metrics (SG: OTT, SG: APP, etc.)

Round-by-round and tournament scores

## 🤝 License
This project is for educational purposes and open to collaboration.


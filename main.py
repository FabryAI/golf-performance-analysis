from pathlib import Path
from src.data_io import load_golf_data

# Percorso al file CSV
csv_path = Path("data/raw/ASA All PGA Raw Data - Tourn Level.csv")

# Caricamento
df_raw = load_golf_data(csv_path)

# Controllo
print(df_raw.head())
print(df_raw.dtypes)

#----------------------------------------------------------------------------

from src.preprocessing import clean_data

df_clean = clean_data(df_raw)

print("✅ Dati dopo la pulizia:")
print(df_clean.head())
print(df_clean.describe())

#----------------------------------------------------------------------------

from src.metrics import average_strokes, strokes_over_time, sg_category_means

print("📊 Media colpi totali:", average_strokes(df_clean))
print("📈 SG medi per categoria:\n", sg_category_means(df_clean))

#----------------------------------------------------------------------------

from src.statistics import compute_correlations, plot_correlation_heatmap, simple_linear_regression

# 🔗 Matrice di correlazione
compute_correlations(df_clean)

# 🔥 Heatmap
plot_correlation_heatmap(df_clean)

# 📈 Regressione lineare: SG totale → Strokes
simple_linear_regression(df_clean, x_col="sg_total", y_col="strokes")

#----------------------------------------------------------------------------

from src.visualization import plot_and_save_correlation_heatmap, save_linear_regression_plot

plot_and_save_correlation_heatmap(df_clean, "outputs/plots/correlation_heatmap.png")
save_linear_regression_plot(df_clean, "sg_total", "strokes", "outputs/plots/linear_regression_sg_total_vs_strokes.png")

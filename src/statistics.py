import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

def compute_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola la matrice di correlazione tra variabili numeriche.
    """
    corr = df.select_dtypes(include="number").corr()
    print("Correlazioni tra variabili numeriche:\n", corr)
    return corr


def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Mostra una heatmap delle correlazioni.
    """
    corr = df.select_dtypes(include="number").corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("📊 Correlazione tra variabili numeriche")
    plt.tight_layout()
    plt.show()


def simple_linear_regression(df: pd.DataFrame, x_col: str, y_col: str):
    """
    Esegue una regressione lineare semplice tra due variabili numeriche.

    Parameters:
        x_col (str): variabile indipendente (es. sg_total)
        y_col (str): variabile dipendente (es. strokes)
    """
    # Rimuovi righe con valori mancanti
    df = df[[x_col, y_col]].dropna()

    # Prepara X e y per sklearn
    X = df[[x_col]]
    y = df[y_col]

    # Crea e allena il modello
    model = LinearRegression()
    model.fit(X, y)

    # Parametri della retta
    slope = model.coef_[0]
    intercept = model.intercept_
    print(f"📈 Regressione: {y_col} = {slope:.2f} * {x_col} + {intercept:.2f}")

    # Grafico della retta
    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, alpha=0.5, label='Dati')
    plt.plot(X, model.predict(X), color='red', label='Regressione')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Regressione lineare: {y_col} vs {x_col}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return model

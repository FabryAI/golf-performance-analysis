import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


def plot_and_save_correlation_heatmap(df: pd.DataFrame, output_path: str):
    """
    Calcola e salva una heatmap di correlazione tra variabili numeriche.

    Parameters:
        df (pd.DataFrame): Dataset pulito da analizzare
        output_path (str): Percorso dove salvare l'immagine (formato PNG)
    """
    # Calcolo della matrice di correlazione
    correlation_matrix = df.corr(numeric_only=True)

    # Setup della figura
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Matrice di Correlazione")
    plt.tight_layout()

    # Salvataggio della figura
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def save_linear_regression_plot(df: pd.DataFrame, x_col: str, y_col: str, output_path: str):
    """
    Crea e salva un grafico con regressione lineare tra due colonne numeriche.

    Parameters:
        df (pd.DataFrame): Dataset
        x_col (str): Nome della colonna X
        y_col (str): Nome della colonna Y
        output_path (str): Percorso dove salvare l'immagine
    """
    # Rimuove righe con valori nulli nelle colonne scelte
    df_plot = df[[x_col, y_col]].dropna()

    X = df_plot[[x_col]]
    y = df_plot[y_col]

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)

    # Setup del grafico
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.4, label="Dati reali")
    plt.plot(X, y_pred, color="red", label="Regr. Lineare")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Regressione: {y_col} vs {x_col}")
    plt.legend()
    plt.tight_layout()

    # Salvataggio
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

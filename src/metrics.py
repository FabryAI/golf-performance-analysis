import pandas as pd

def average_strokes(df: pd.DataFrame) -> float:
    """
    Calcola la media dei colpi totali nel dataset.

    Parameters:
        df (DataFrame): dati puliti

    Returns:
        float: media dei colpi ("strokes")
    """
    return df["strokes"].mean()


def strokes_over_time(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola l'andamento della media dei colpi nel tempo.

    Returns:
        DataFrame: date + media dei colpi (utile per grafici)
    """
    df_sorted = df.sort_values("date")
    trend = df_sorted.groupby("date")["strokes"].mean().reset_index()
    return trend


def sg_category_means(df: pd.DataFrame) -> pd.Series:
    """
    Calcola la media delle statistiche SG (Strokes Gained).

    Returns:
        Series: media per ogni colonna SG
    """
    sg_cols = ["sg_putt", "sg_arg", "sg_app", "sg_ott", "sg_t2g", "sg_total"]
    return df[sg_cols].mean()


def best_courses(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """
    Ritorna i campi dove si sono ottenuti i migliori punteggi medi.

    Parameters:
        top_n (int): numero di campi da mostrare

    Returns:
        DataFrame: top N campi con punteggio medio più basso
    """
    course_scores = df.groupby("course")["strokes"].mean().sort_values()
    return course_scores.head(top_n).reset_index()


def performance_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analizza la media dei colpi per anno.

    Returns:
        DataFrame: anni + media colpi
    """
    df["year"] = df["date"].dt.year
    return df.groupby("year")["strokes"].mean().reset_index()

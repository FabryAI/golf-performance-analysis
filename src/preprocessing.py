import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pulisce il dataset rimuovendo dati inutili o inconsistenti.
    
    Passaggi eseguiti:
    1. Rimozione dei duplicati
    2. Gestione dei valori mancanti essenziali
    3. Conversione dei tipi numerici
    4. Filtro su valori anomali di punteggio
    5. Pulizia stringhe (facoltativa)
    """

    # 1. Rimuove righe duplicate
    df = df.drop_duplicates()

    # 2. Rimuove righe con date, strokes o sg_total mancanti
    df = df.dropna(subset=["date", "strokes", "sg_total"])

    # 3. Converte colonne numeriche (può correggere errori di formato)
    numeric_cols = [
        "strokes", "hole_par", "n_rounds",
        "sg_putt", "sg_arg", "sg_app", "sg_ott", "sg_t2g", "sg_total"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 4. Rimuove righe con valori anomali nei punteggi
    #    (es. meno di 50 o più di 200 colpi totali)
    df = df[(df["strokes"] > 50) & (df["strokes"] < 200)]

    # 5. (Facoltativo) Pulisce nomi dei giocatori da spazi
    if "player" in df.columns:
        df["player"] = df["player"].str.strip()

    return df
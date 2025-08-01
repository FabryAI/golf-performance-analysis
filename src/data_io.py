# Importiamo Path da pathlib per lavorare con i percorsi in modo sicuro (Windows/Linux/Mac)
from pathlib import Path

# Importiamo pandas, la libreria principale per lavorare con dati tabellari (es. CSV)
import pandas as pd

# Definiamo una lista di colonne che vogliamo tenere nel nostro dataset
# Questo evita di caricare colonne inutili o non rilevanti per l’analisi
COLUMNS_TO_KEEP = [
    "date",              # Data del torneo
    "player",            # Nome del giocatore
    "tournament name",   # Nome del torneo
    "course",            # Campo da golf
    "strokes",           # Numero di colpi totali
    "hole_par",          # Somma dei par previsti per il round
    "n_rounds",          # Numero di round giocati nel torneo
    "sg_putt",           # Strokes Gained - putting
    "sg_arg",            # Strokes Gained - around the green
    "sg_app",            # Strokes Gained - approach
    "sg_ott",            # Strokes Gained - off the tee
    "sg_t2g",            # Strokes Gained - tee to green
    "sg_total",          # Strokes Gained totale
    "Finish"             # Posizione finale del giocatore (es. T12, CUT, ecc.)
]

# Funzione per caricare e filtrare il file CSV dei dati golf
def load_golf_data(csv_path: Path) -> pd.DataFrame:
    """
    Carica e filtra i dati di golf da un file CSV.

    Parametri:
        csv_path (Path): percorso al file CSV da leggere

    Restituisce:
        DataFrame: tabella con solo le colonne necessarie, e la data in formato datetime
    """

    # Legge il file CSV con pandas
    # encoding='utf-8' garantisce compatibilità, e on_bad_lines='skip' evita crash su righe corrotte
    df = pd.read_csv(csv_path, encoding='utf-8', on_bad_lines='skip')

    # Selezioniamo solo le colonne che abbiamo definito in COLUMNS_TO_KEEP
    # .copy() crea una copia indipendente (buona pratica per evitare effetti collaterali)
    df = df[COLUMNS_TO_KEEP].copy()

    # Converte la colonna "date" in formato datetime, utile per analisi temporali
    # errors='coerce' trasforma eventuali date non valide in NaT (null date)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Ritorna il DataFrame filtrato e con la colonna "date" convertita
    return df

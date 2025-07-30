from pathlib import Path
import pandas as pd


def load_scores(path: Path) -> pd.DataFrame:
    """
    Carica un singolo file CSV di scorecard.

    Parametri:
        path (Path): percorso al file CSV da caricare.

    Restituisce:
        DataFrame: dati con colonna 'date' convertita in datetime.
    """
    df = pd.read_csv(path, parse_dates=['date'], dayfirst=True)
    return df


def save_processed(df: pd.DataFrame, path: Path):
    """
    Salva un DataFrame pulito o arricchito in un file CSV.

    Parametri:
        df (DataFrame): DataFrame da salvare.
        path (Path): percorso di destinazione per il CSV.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def load_all_scores(raw_dir: Path) -> pd.DataFrame:
    """
    Legge tutti i CSV nella cartella raw_dir e li unisce in un unico DataFrame.

    Parametri:
        raw_dir (Path): directory contenente i file CSV raw.

    Restituisce:
        DataFrame: concatenazione di tutti i CSV trovati.
        Se non ci sono file, restituisce DataFrame vuoto con colonne standard.
    """
    files = list(raw_dir.glob('*.csv'))
    if not files:
        cols = ['date','course','score','putts','fairways_hit','greens_in_reg']
        return pd.DataFrame(columns=cols)

    dfs = []
    for f in files:
        df = pd.read_csv(f, parse_dates=['date'], dayfirst=True)
        dfs.append(df)
    combined = pd.concat(dfs, ignore_index=True)
    return combined

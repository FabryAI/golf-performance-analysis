import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Rimuovi duplicati
    df = df.drop_duplicates()
    # 2. Converte colonne numeriche
    for col in ['score','putts','fairways_hit','greens_in_reg']:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    # 3. Elimina righe senza data o score
    df = df.dropna(subset=['date','score'])
    return df

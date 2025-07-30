import pytest
import pandas as pd
import numpy as np

from src.preprocessing import clean_data, add_features


def make_raw_df():
    # DataFrame di esempio con duplicati, stringhe e NaN
    return pd.DataFrame({
        'date': ['2025-07-01','2025-07-01','2025-07-02', None],
        'score': ['72','72','68','70'],
        'putts': ['32','32', np.nan,'30'],
        'fairways_hit': ['10','10','11','11'],
        'greens_in_reg': ['12','12','14','14']
    })


def test_clean_data_removes_duplicates_and_nans():
    df = make_raw_df()
    # Converte le date in datetime; valori non validi diventano NaT
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    cleaned = clean_data(df)

    # 1. Righe duplicate rimosse (da 4 a 2)
    assert cleaned.shape[0] == 2
    # 2. Non contiene più righe con date NaT
    assert cleaned['date'].isna().sum() == 0
    # 3. Tutti i campi score sono numerici
    assert pd.api.types.is_numeric_dtype(cleaned['score'])


def test_add_features_computes_correctly():
    # partiamo da un df pulito
    df = pd.DataFrame({
        'date': pd.to_datetime(['2025-07-01','2025-07-02','2025-07-03','2025-07-04','2025-07-05']),
        'score': [72, 70, 68, 74, 71],
        'putts': [32, 30, 28, 34, 31],
        'fairways_hit': [10,11,12,9,10],
        'greens_in_reg': [12,14,13,11,12]
    })
    feat = add_features(df)

    # 1. putt_per_hole = putts/18
    assert feat['putt_per_hole'].iloc[0] == pytest.approx(32/18)
    # 2. rolling_score_5 su 5 elementi = media di tutti e 5
    assert feat['rolling_score_5'].iloc[-1] == pytest.approx(sum([72,70,68,74,71])/5)
    # 3. pct_fairways in [0,100]
    assert feat['pct_fairways'].between(0,100).all()
    # 4. pct_gir in [0,100]
    assert feat['pct_gir'].between(0,100).all()

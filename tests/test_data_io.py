import pandas as pd
from pathlib import Path
import tempfile

from src.data_io import load_scores, save_processed, load_all_scores

def test_load_and_save_scores(tmp_path):
    # prepara un CSV di prova
    df0 = pd.DataFrame({
        'date': ['2025-07-01','2025-07-02'],
        'score': [70, 71],
        'putts': [32, 31]
    })
    csv = tmp_path / "raw.csv"
    df0.to_csv(csv, index=False)
    
    # load_scores
    df1 = load_scores(csv)
    assert 'date' in df1.columns
    assert df1['date'].dtype == 'datetime64[ns]'
    
    # save_processed
    out = tmp_path / "out.csv"
    save_processed(df1, out)
    df2 = pd.read_csv(out, parse_dates=['date'])
    pd.testing.assert_frame_equal(df1, df2)

def test_load_all_scores_empty(tmp_path):
    # cartella vuota → DataFrame solo colonne
    empty = load_all_scores(tmp_path)
    expected_cols = ['date','course','score','putts','fairways_hit','greens_in_reg']
    assert list(empty.columns) == expected_cols
    assert empty.shape[0] == 0

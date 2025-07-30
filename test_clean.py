# test_clean.py
'''“Pulire” significa trasformare il tuo DataFrame grezzo in una versione pronta per l’analisi, togliendo o correggendo tutto ciò che può disturbare i calcoli:
Rimuovere duplicati: se hai importato più volte lo stesso round, elimini le righe doppie.
Convertire i tipi: trasformi colonne che contengono numeri (es. score, putts) da stringhe a int/float.
Gestire valori mancanti: togli le righe in cui mancano campi fondamentali come date o score, così non generi errori o bias.'''

from pathlib import Path
from src.data_io import load_all_scores
from src.preprocessing import clean_data

# 1. Carica i dati grezzi
df       = load_all_scores(Path('data/raw'))
# 2. Applica il cleaning
df_clean = clean_data(df)

print("Righe prima del cleaning:", df.shape[0])
print("Righe dopo  del cleaning:", df_clean.shape[0])

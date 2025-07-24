# Lavoro

## Calcolatore di Esterificazione - Produzione di Acqua

Questo repository contiene un generatore Python per creare un file Excel (.xlsx) che calcola automaticamente la quantità di acqua prodotta in reazioni di esterificazione.

### Caratteristiche

Il file Excel generato include:

1. **Database dei Composti** con pesi molecolari di:
   - Acidi grassi saturi (C12:0 - C20:0)
   - Acidi grassi insaturi (C18:1, C18:2, C18:3, C20:4)
   - Alcol due etil esilico (2-etilesanolo)
   - Glicerina
   - Acido adipico

2. **Calcolatore Automatico** che:
   - Converte automaticamente i pesi (kg) in moli
   - Calcola la quantità di acqua prodotta nella reazione
   - Identifica il reagente limitante
   - Verifica il bilancio di massa

3. **Istruzioni d'uso** complete

### Uso

1. **Genera il file Excel:**
   ```bash
   python3 esterification_calculator.py
   ```

2. **Apri il file generato:** `Calcolatore_Esterificazione.xlsx`

3. **Inserisci i dati:**
   - Vai al foglio "Calcolatore Esterificazione"
   - Inserisci i pesi dei reagenti in kg nelle celle grigie (colonna B)
   - I calcoli si aggiorneranno automaticamente

4. **Verifica i risultati:**
   - Controlla la quantità di acqua prodotta
   - Verifica il bilancio di massa per la coerenza dei dati

### Reazione di Esterificazione

La reazione generale considerata è:
```
R-COOH + R'-OH → R-COO-R' + H₂O
(Acido) + (Alcol) → (Estere) + (Acqua)
```

Ogni mole di acido che reagisce con una mole di alcol produce una mole di acqua.

### Test

Per testare il file Excel generato:
```bash
python3 test_excel.py
```

### Requisiti

- Python 3.x
- openpyxl
- xlsxwriter

```bash
pip3 install openpyxl xlsxwriter
```
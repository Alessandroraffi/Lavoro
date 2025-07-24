# Documentazione Scientifica - Calcolatore di Esterificazione

## Base Teorica

### Reazione di Esterificazione
La reazione di esterificazione è una reazione di condensazione tra un acido carbossilico e un alcol che produce un estere e acqua:

```
R-COOH + R'-OH → R-COO-R' + H₂O
```

Dove:
- R-COOH = acido carbossilico (acidi grassi)
- R'-OH = alcol (alcol due etil esilico, glicerina)
- R-COO-R' = estere (prodotto principale)
- H₂O = acqua (sottoprodotto)

### Stechiometria
- **Rapporto 1:1**: Ogni mole di acido reagisce con una mole di alcol
- **Produzione acqua**: Si produce una mole di acqua per ogni legame estereo formato
- **Reagente limitante**: Determina la quantità massima di prodotto ottenibile

## Composti Supportati

### Acidi Grassi Saturi
| Composto | Formula | PM (g/mol) | Carboni |
|----------|---------|------------|---------|
| Acido laurico | C₁₂H₂₄O₂ | 200.32 | C12:0 |
| Acido miristico | C₁₄H₂₈O₂ | 228.37 | C14:0 |
| Acido palmitico | C₁₆H₃₂O₂ | 256.42 | C16:0 |
| Acido stearico | C₁₈H₃₆O₂ | 284.48 | C18:0 |
| Acido arachidico | C₂₀H₄₀O₂ | 312.53 | C20:0 |

### Acidi Grassi Insaturi
| Composto | Formula | PM (g/mol) | Carboni |
|----------|---------|------------|---------|
| Acido oleico | C₁₈H₃₄O₂ | 282.46 | C18:1 |
| Acido linoleico | C₁₈H₃₂O₂ | 280.45 | C18:2 |
| Acido linolenico | C₁₈H₃₀O₂ | 278.43 | C18:3 |
| Acido arachididonico | C₂₀H₃₂O₂ | 304.47 | C20:4 |

### Altri Composti
| Composto | Formula | PM (g/mol) | Funzione |
|----------|---------|------------|----------|
| Alcol due etil esilico | C₈H₁₈O | 130.23 | Alcol primario |
| Glicerina | C₃H₈O₃ | 92.09 | Triolo |
| Acido adipico | C₆H₁₀O₄ | 146.14 | Acido dicarbossilico |
| Acqua | H₂O | 18.015 | Prodotto |

## Calcoli Implementati

### 1. Conversione Massa-Moli
```
Moli = (Peso in kg × 1000) / Peso Molecolare (g/mol)
```

### 2. Bilancio Stechiometrico
```
Moli_acidi_totali = Σ(moli di ogni acido)
Moli_alcoli_totali = Σ(moli di ogni alcol)
Reagente_limitante = MIN(Moli_acidi_totali, Moli_alcoli_totali)
```

### 3. Produzione di Acqua
```
Moli_acqua = Reagente_limitante
Massa_acqua (g) = Moli_acqua × 18.015
Massa_acqua (kg) = Massa_acqua (g) / 1000
```

### 4. Controllo Bilancio di Massa
```
Differenza_% = |Massa_reagenti - Massa_prodotti| / Massa_reagenti × 100
```

## Validazione dei Risultati

### Controlli di Coerenza
1. **Bilancio di massa**: La somma delle masse dei prodotti dovrebbe essere circa uguale alla massa dei reagenti
2. **Rapporti stechiometrici**: Il reagente limitante determina la conversione massima
3. **Ordini di grandezza**: La produzione di acqua dovrebbe essere del 3-5% della massa totale dei reagenti

### Limitazioni del Modello
- Assume conversione completa (100%)
- Non considera reazioni collaterali
- Non tiene conto di perdite per evaporazione
- Modello ideale senza considerazioni cinetiche

## Esempio Pratico

Con i valori del demo:
- **Reagenti**: 7.70 kg totali
- **Acidi totali**: 16.61 moli
- **Alcoli totali**: 25.21 moli
- **Reagente limitante**: 16.61 moli (acidi)
- **Acqua prodotta**: 0.299 kg (3.89% dei reagenti)

Questo risultato è coerente con le aspettative teoriche per una reazione di esterificazione industriale.
"""
Simulazione dei calcoli che Excel eseguirà automaticamente
"""

def simulate_excel_calculations():
    """Simula i calcoli che Excel eseguirà con i valori del demo"""
    
    print("=== SIMULAZIONE CALCOLI EXCEL ===")
    print()
    
    # Dati inseriti nel demo
    reagents = {
        'Acido palmitico (C16:0)': {'peso_kg': 2.0, 'pm': 256.42},
        'Acido stearico (C18:0)': {'peso_kg': 1.5, 'pm': 284.48},
        'Acido oleico (C18:1)': {'peso_kg': 1.0, 'pm': 282.46},
        'Alcol due etil esilico': {'peso_kg': 3.0, 'pm': 130.23},
        'Glicerina': {'peso_kg': 0.2, 'pm': 92.09},
        'Acido adipico': {'peso_kg': 0.0, 'pm': 146.14}
    }
    
    print("CALCOLI DELLE MOLI:")
    moli_acidi = 0
    moli_alcoli = 0
    
    for nome, dati in reagents.items():
        peso_g = dati['peso_kg'] * 1000  # Conversione kg -> g
        moli = peso_g / dati['pm']
        print(f"- {nome}: {dati['peso_kg']} kg = {peso_g} g / {dati['pm']} g/mol = {moli:.4f} mol")
        
        if 'Acido' in nome and 'adipico' not in nome:
            moli_acidi += moli
        elif 'Alcol' in nome or 'Glicerina' in nome:
            moli_alcoli += moli
    
    print()
    print("CALCOLI STECHIOMETRICI:")
    print(f"- Moli acidi totali: {moli_acidi:.4f} mol")
    print(f"- Moli alcoli totali: {moli_alcoli:.4f} mol")
    
    reagente_limitante = min(moli_acidi, moli_alcoli)
    print(f"- Reagente limitante: {reagente_limitante:.4f} mol")
    
    print()
    print("PRODUZIONE ACQUA:")
    moli_acqua = reagente_limitante
    massa_acqua_g = moli_acqua * 18.015  # PM acqua
    massa_acqua_kg = massa_acqua_g / 1000
    
    print(f"- Moli di acqua prodotta: {moli_acqua:.4f} mol")
    print(f"- Massa acqua prodotta: {massa_acqua_g:.2f} g")
    print(f"- Massa acqua prodotta: {massa_acqua_kg:.4f} kg")
    
    print()
    print("BILANCIO DI MASSA:")
    massa_totale_reagenti = sum(dati['peso_kg'] for dati in reagents.values())
    print(f"- Massa totale reagenti: {massa_totale_reagenti:.2f} kg")
    print(f"- Massa acqua prodotta: {massa_acqua_kg:.4f} kg")
    print(f"- Massa prodotti stimata: {massa_totale_reagenti - massa_acqua_kg:.4f} kg")
    differenza_percentuale = (massa_acqua_kg / massa_totale_reagenti) * 100
    print(f"- Acqua come % dei reagenti: {differenza_percentuale:.2f}%")

if __name__ == "__main__":
    simulate_excel_calculations()
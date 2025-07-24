"""
Crea un file Excel di esempio con valori dimostrativi
"""

import openpyxl
from esterification_calculator import EsterificationCalculator

def create_demo_file():
    """Crea un file di dimostrazione con valori di esempio"""
    # Genera il file base
    calculator = EsterificationCalculator()
    filepath = calculator.generate_excel_file("Demo_Calcolatore_Esterificazione.xlsx")
    
    # Apri il file e inserisci valori di esempio
    wb = openpyxl.load_workbook(filepath)
    calc_sheet = wb["Calcolatore Esterificazione"]
    
    # Valori di esempio per una reazione tipica
    # Acido palmitico: 2.0 kg (row 6)
    calc_sheet['B6'].value = 2.0
    
    # Acido stearico: 1.5 kg (row 7)
    calc_sheet['B7'].value = 1.5
    
    # Acido oleico: 1.0 kg (row 8)
    calc_sheet['B8'].value = 1.0
    
    # Alcol due etil esilico: 3.0 kg (row 9)
    calc_sheet['B9'].value = 3.0
    
    # Glicerina: 0.2 kg (row 10)
    calc_sheet['B10'].value = 0.2
    
    # Acido adipico: 0.0 kg (row 11) - non usato in questo esempio
    calc_sheet['B11'].value = 0.0
    
    # Salva il file demo
    wb.save(filepath)
    wb.close()
    
    print(f"File demo creato: {filepath}")
    print("\nValori di esempio inseriti:")
    print("- Acido palmitico: 2.0 kg")
    print("- Acido stearico: 1.5 kg") 
    print("- Acido oleico: 1.0 kg")
    print("- Alcol due etil esilico: 3.0 kg")
    print("- Glicerina: 0.2 kg")
    print("- Acido adipico: 0.0 kg")
    
    return filepath

if __name__ == "__main__":
    create_demo_file()
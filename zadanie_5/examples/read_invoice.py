"""
Odczyt i analiza faktury PDF z użyciem biblioteki pdfplumber.
Celem jest:
- wyodrębnienie tekstu i tabeli z faktury (np. lista produktów),
- zapis wykrytej tabeli do pliku CSV (jeśli istnieje).

Biblioteka pdfplumber pozwala pracować ze stronami PDF
i wydobywać dane tekstowe oraz struktury tabelaryczne.
"""

import pdfplumber
import pandas as pd
import os

# Ścieżka do pliku PDF 
pdf_path = "faktura_arial.pdf"
csv_output_path = "wydobyta_tabela.csv"

# Sprawdzenie czy plik istnieje
if not os.path.exists(pdf_path):
    print(f"Plik PDF nie został znaleziony: {pdf_path}")
    exit()

# Otwieranie PDF i analiza pierwszej strony
with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]

    # === 1. Odczyt tekstu ===
    print("Tekst zawarty w fakturze:\n")
    text = page.extract_text()
    print(text)

    # === 2. Wydobycie tabeli ===
    print("\nTabela z faktury (jeśli wykryta):\n")
    table = page.extract_table()

    if table:
        for row in table:
            print(" | ".join(row))
        
        # === 3. Zapis do pliku CSV ===
        headers = table[0]
        rows = table[1:]

        df = pd.DataFrame(rows, columns=headers)
        df.to_csv(csv_output_path, index=False, encoding='utf-8-sig')

        print(f"\nTabela została zapisana do pliku CSV:\n{csv_output_path}")
    else:
        print("Nie wykryto tabeli w PDF – może być graficzna lub niestandardowa.")

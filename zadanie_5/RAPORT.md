# 📄 RAPORT – Biblioteki PDF w Pythonie (zadanie 5)

W ramach zadania zaprezentowano dwie biblioteki Pythona służące do pracy z dokumentami PDF: **ReportLab** oraz **pdfplumber**. Obie zostały użyte w praktycznych przykładach tworzenia i odczytu faktur w formacie PDF.

---

## 🧰 1. ReportLab

### 🔎 Opis
**ReportLab** to biblioteka do **generowania dokumentów PDF w Pythonie**. Umożliwia zarówno niskopoziomowe rysowanie (tekst, linie, obrazy), jak i wysokopoziomowe tworzenie układów (np. z użyciem `platypus`).

### ✨ Główne funkcje
- Rysowanie tekstu, kształtów, linii, obrazów na stronie (`canvas`)
- Obsługa stylów, czcionek TrueType, kolorów, warstw
- Generowanie tabel, paragrafów, layoutów (`platypus`)
- Tworzenie interaktywnych formularzy PDF (`acroForm`)
- Eksport do formatu A4, listowego, własnego

### ✅ Zalety
- Bardzo rozbudowane możliwości typograficzne
- Obsługa polskich znaków przy użyciu czcionek TTF (np. Arial)
- Możliwość tworzenia formularzy PDF z polami do wypełnienia
- Obsługa wielu stron, stylów i formatów

### ⚠️ Ograniczenia
- Wysoka elastyczność kosztem złożoności
- Brak możliwości edycji istniejących PDF-ów (tylko generowanie)

### 🔗 Dokumentacja
- https://www.reportlab.com/documentation/
- https://pypi.org/project/reportlab/

---

## 🔍 2. pdfplumber

### 🔎 Opis
**pdfplumber** to biblioteka do **odczytu zawartości plików PDF**, w tym tekstu, tabel, współrzędnych elementów oraz metadanych.

### ✨ Główne funkcje
- Odczyt tekstu ze stron (`extract_text`)
- Wydobywanie danych tabelarycznych (`extract_table`)
- Praca z pozycją tekstu i grafik (`page.chars`, `page.rects`)
- Eksport danych do CSV, JSON lub pandas DataFrame

### ✅ Zalety
- Bardzo szybki i prosty w użyciu
- Zaskakująco skuteczna detekcja tekstu i tabel
- Działa z wieloma typami PDF generowanymi z programów biurowych

### ⚠️ Ograniczenia
- Nie działa z graficznymi (zeskanowanymi) PDF-ami bez OCR
- Brak możliwości edycji ani tworzenia PDF — tylko odczyt
- Tabele muszą mieć wyraźny układ tekstowy (nie graficzny)

### 🔗 Dokumentacja
- https://github.com/jsvine/pdfplumber
- https://pypi.org/project/pdfplumber/

---

## 📁 Zastosowanie w zadaniu

W zadaniu 5 przygotowano następujące pliki:

| Plik                            | Opis                                                                              |
|---------------------------------|-----------------------------------------------------------------------------------|
| `create_invoice_pdf.py`         | Generuje fakturę PDF z tabelą produktów, logo, stopką i kwotą słownie (ReportLab) |
| `create_form_pdf.py`            | Tworzy interaktywny formularz PDF z polami do uzupełnienia (ReportLab)            |
| `read_invoice.py`               | Odczytuje zawartość tekstową i tabelaryczną z pliku PDF (pdfplumber)              |

---

## ✅ Podsumowanie porównawcze

| Biblioteka    | Generowanie PDF  | Odczyt PDF | Formularze PDF | Obsługa tabel  | Edycja istniejących PDF |
|---------------|------------------|------------|----------------|----------------|-------------------------|
| ReportLab     |       ✅         |    ❌     |      ✅        | ✅ (tworzenie)|          ❌             |
| pdfplumber    |       ❌         |    ✅     |      ❌        | ✅ (odczyt)   |          ❌             |

---

Obie biblioteki zostały skutecznie zastosowane:
- **ReportLab** posłużył do stworzenia estetycznej faktury PDF oraz interaktywnego formularza.
- **pdfplumber** pozwolił na odczyt danych faktury i eksport tabeli do pliku `.csv`.


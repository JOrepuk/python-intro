"""
Tworzenie formularza w formacie PDF z wykorzystaniem biblioteki ReportLab.

Biblioteka ReportLab umożliwia programistyczne generowanie dokumentów PDF
w Pythonie poprzez:
- niskopoziomowe rysowanie elementów na stronie (tekst, pola, figury) z użyciem `canvas`,
- obsługę interaktywnych formularzy (pól tekstowych, checkboxów, list rozwijanych) przez `AcroForm`,
- wsparcie dla czcionek TrueType (np. Arial) umożliwiających poprawne wyświetlanie polskich znaków.

W tym przykładzie wykorzystujemy bezpośrednio obiekt `canvas`:
- `drawString` — rysuje tekst na stronie,
- `acroForm.textfield`, `acroForm.checkbox`, `acroForm.choice` — dodają interaktywne pola formularza,
- `save()` — zapisuje gotowy plik PDF.

Formularz zawiera pola do uzupełnienia: imię i nazwisko, checkbox akceptacji oraz listę wyboru roli.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Rejestracja czcionek
pdfmetrics.registerFont(TTFont("Arial", "ARIAL.TTF"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "ARIALBD.TTF"))

# Utworzenie dokumentu
c = canvas.Canvas("form_example.pdf", pagesize=A4)

# Tytuł formularza
c.setFont("Arial-Bold", 16)
c.drawString(100, 800, "Formularz zgłoszeniowy")

# Tworzenie formularza
form = c.acroForm

# === Pole 1: Imię i nazwisko ===
y = 750
c.setFont("Arial", 12)
c.drawString(100, y, "Imię i nazwisko:")
form.textfield(
    name='name_field',
    tooltip='Wpisz imię i nazwisko',
    x=100, y=y - 25,
    width=300, height=20,
    borderStyle='inset',
    forceBorder=True
)

# === Pole 2: Akceptacja regulaminu ===
y = y - 70
c.drawString(100, y, "Akceptuję regulamin:")
form.checkbox(
    name='accept_terms',
    tooltip='Zaznacz jeśli akceptujesz',
    x=100, y=y - 25,
    buttonStyle='check',
    borderStyle='solid',
    size=15
)

# === Pole 3: Rola użytkownika ===
y = y - 70
c.drawString(100, y, "Rola:")
form.choice(
    name='user_role',
    tooltip='Wybierz rolę',
    x=100, y=y - 25,
    width=200, height=20,
    options=['Student', 'Developer', 'Manager'],
    value='Student'
)

# Stopka
c.setFont("Arial", 10)
c.drawString(100, 100, "Uzupełnij formularz i zapisz PDF.")

# Zapisz PDF
c.save()

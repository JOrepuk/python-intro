"""
Tworzenie faktury VAT w formacie PDF z wykorzystaniem biblioteki ReportLab.

Biblioteka ReportLab umożliwia programistyczne generowanie dokumentów PDF
w Pythonie poprzez:
- rysowanie tekstu, kształtów i obrazów (niski poziom: canvas),
- użycie gotowych komponentów i układów (wysoki poziom: platypus),
- wsparcie dla tabel, stylów, czcionek i layoutów.

W tym przykładzie wykorzystujemy system układów `platypus`:
- `SimpleDocTemplate` — tworzy dokument i obsługuje marginesy
- `Paragraph`, `Table`, `Spacer` — elementy treści
- `Canvas` — niskopoziomowe rysowanie (np. nagłówek jako "logo")

Dodatkowo używamy czcionek TTF (Arial), aby obsłużyć polskie znaki.
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from num2words import num2words

# Rejestrujemy czcionki z plików TTF, by obsłużyć polskie znaki (ą, ś, ź itd.)
pdfmetrics.registerFont(TTFont("Arial", "ARIAL.TTF"))         # zwykła czcionka
pdfmetrics.registerFont(TTFont("Arial-Bold", "ARIALBD.TTF"))  # wersja pogrubiona

# Tworzymy zestaw stylów do użycia w paragrafach i tabelach
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="NormalArial", fontName="Arial", fontSize=10, leading=12))
styles.add(ParagraphStyle(name="BoldArial", fontName="Arial-Bold", fontSize=12))

# Inicjalizacja dokumentu PDF z marginesami i formatem strony A4
doc = SimpleDocTemplate("faktura_arial.pdf", pagesize=A4,
                        rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)

elements = []  # lista komponentów do umieszczenia w dokumencie (tabele, teksty itd.)

def draw_logo(canvas: Canvas, doc):
    """
    Funkcja wywoływana przy generowaniu pierwszej strony PDF.
    Wykorzystuje niskopoziomowy obiekt `canvas` do narysowania logo i danych faktury.
    """
    canvas.setFillColorRGB(0.1, 0.3, 0.8)
    canvas.rect(30, 780, 200, 30, fill=1)

    canvas.setFillColor(colors.white)
    canvas.setFont("Arial-Bold", 14)
    canvas.drawString(40, 790, "Firma XYZ Sp. z o.o.")

    # Dane faktury (nr, daty)
    canvas.setFillColor(colors.black)
    canvas.setFont("Arial", 9)
    canvas.drawString(400, 800, "Faktura nr FV/2025/05")
    canvas.drawString(400, 790, "Data wystawienia: 2025-05-05")
    canvas.drawString(400, 780, "Data sprzedaży: 2025-05-03")

# Sekcja z danymi wystawcy i nabywcy (wstawiona jako tabela 2-kolumnowa)
seller = """<b>Sprzedawca:</b><br/>
Firma XYZ Sp. z o.o.<br/>
ul. Uliczna 1<br/>
00-000 Warszawa<br/>
NIP: 111-111-11-11<br/>
Tel: 123 456 789<br/>
E-mail: biuro@firma.pl<br/>"""

buyer = """<b>Nabywca:</b><br/>
Jan Kowalski<br/>
ul. Klientowska 45<br/>
00-001 Kraków<br/>
NIP: 222-222-22-22<br/>
Tel: 987 654 321<br/>
E-mail: jan@example.com<br/>"""

data = [[Paragraph(seller, styles["NormalArial"]), Paragraph(buyer, styles["NormalArial"])]]
table = Table(data, colWidths=[270, 270])
table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))  # tekst u góry komórek

elements.append(Spacer(1, 40))
elements.append(table)
elements.append(Spacer(1, 20))

# Lista pozycji na fakturze: lp, nazwa, ilość, jm, cena, VAT, netto, brutto
products = [
    ["1", "Produkt A – opis", "2", "szt.", "123.00", "23%", "246.00", "302.58"],
    ["2", "Usługa specjalistyczna", "1", "usł.", "320.00", "8%", "320.00", "345.60"],
    ["3", "Produkt B – zestaw kabli", "5", "szt.", "45.00", "23%", "225.00", "276.75"],
    ["4", "Usługa doradcza", "2", "usł.", "200.00", "8%", "400.00", "432.00"],
    ["5", "Produkt C – router WiFi", "1", "szt.", "290.00", "23%", "290.00", "356.70"],
    ["6", "Produkt D – pakiet tonerów", "3", "szt.", "99.00", "23%", "297.00", "365.31"],
    ["7", "Usługa instalacji", "1", "usł.", "150.00", "8%", "150.00", "162.00"],
    ["8", "Produkt E – kamera IP", "2", "szt.", "180.00", "23%", "360.00", "442.80"],
    ["9", "Produkt F – akcesoria komputerowe", "4", "szt.", "75.00", "23%", "300.00", "369.00"],
    ["10", "Usługa konfiguracji sieci", "1", "usł.", "250.00", "8%", "250.00", "270.00"],
    ["11", "Produkt G – monitor 24\"", "2", "szt.", "450.00", "23%", "900.00", "1107.00"],
    ["12", "Produkt H – obudowa ATX", "1", "szt.", "220.00", "23%", "220.00", "270.60"],
    ["13", "Usługa wsparcia technicznego", "1", "usł.", "180.00", "8%", "180.00", "194.40"],
    ["14", "Produkt I – klawiatura mechaniczna", "3", "szt.", "160.00", "23%", "480.00", "590.40"],
    ["15", "Produkt J – oprogramowanie licencyjne", "1", "szt.", "500.00", "0%", "500.00", "500.00"]
]
header = ["Lp", "Nazwa", "Ilość", "Jm", "Cena netto", "VAT", "Netto", "Brutto"]
products.insert(0, header)

# Tabela pozycji z odpowiednim formatowaniem
table = Table(products, colWidths=[25, 190, 40, 40, 70, 40, 70, 70])
table.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),  # nagłówek
    ("FONTNAME", (0, 1), (-1, -1), "Arial"),      # dane
    ("ALIGN", (2, 1), (-1, -1), "CENTER"),
]))
elements.append(table)
elements.append(Spacer(1, 20))

# Kwota końcowa i słownie (z wykorzystaniem num2words)
total_amount = 5804.14
elements.append(Paragraph(f"<b>Razem do zapłaty: {total_amount:.2f} PLN</b>", styles["NormalArial"]))

# Konwersja liczby na słowa
kwota_slownie = num2words(total_amount, lang='pl').replace("przecinek", "zł i").replace("zero", "") + " gr"
elements.append(Paragraph(f"Słownie: <i>{kwota_slownie.capitalize()}</i>", styles["NormalArial"]))
elements.append(Spacer(1, 20))

# Podpisy do druku
signatures = Table([
    ["........................................", "........................................"],
    ["Osoba upoważniona do odbioru", "Osoba upoważniona do wystawienia"]
], colWidths=[270, 270])
signatures.setStyle(TableStyle([
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, -1), "Arial"),
]))
elements.append(signatures)

# Generowanie PDF
doc.build(elements, onFirstPage=draw_logo)

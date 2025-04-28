# Programowanie Zaawansowane – Laboratoria

Repozytorium zawiera rozwiązania zadań laboratoryjnych z przedmiotu **Programowanie Zaawansowane** w Pythonie.

## Struktura projektu

- `zadanie_1/`  
  Wprowadzenie do pracy z Pythonem i GitHubem:
  - Organizacja środowiska programistycznego.
  - Wyszukiwanie informacji w dokumentacji Pythona.
  - Przykładowy program w Pythonie:
    - Tworzenie i łączenie list (`zip()`).
    - Wykorzystanie funkcji z modułu standardowego (`random.choice()`).
    - Obsługa wyjątków (`IndexError`, `ZeroDivisionError`).
    - Komentarze z linkami do dokumentacji.
  - Publikacja kodu na GitHub.

- `zadanie_2/`  
  Test-Driven Development (TDD) i testy jednostkowe:
  - Implementacja pięciu funkcji o różnych zastosowaniach:
    - Walidacja e-maila.
    - Obliczanie pola prostokąta.
    - Filtrowanie liczb parzystych z listy.
    - Konwersja formatu daty.
    - Sprawdzanie, czy tekst jest palindromem.
  - Testy jednostkowe napisane w podejściu Test-Driven Development (`unittest`).
  - Testy uwzględniają typowe przypadki, przypadki brzegowe i obsługę błędów.
  - Testy parametryzowane (`subTest`).
  - Pokrycie kodu testami zmierzone za pomocą `coverage.py`: **100%**.

## Technologie

- Python 3.13
- Moduły standardowe: `random`, `unittest`
- Narzędzia dodatkowe: `coverage.py`

## Uruchamianie testów (Zadanie 2)

Aby uruchomić testy jednostkowe i zmierzyć pokrycie kodu:

```bash
cd zadanie_2
python -m coverage run --source=app -m unittest test_app.py
python -m coverage report -m
```

## Pokrycie kodu

- Testy jednostkowe zapewniają **100% pokrycia kodu** (`coverage.py report`).

## Autor

Jakub Orepuk – 2025
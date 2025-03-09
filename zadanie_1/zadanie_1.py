import random  # Import modułu random (https://docs.python.org/3/library/random.html)

# Tworzenie dwóch list
names = ["Ala", "Bartek", "Celina"]
ages = [23, 30, 27]

# Łączenie list za pomocą funkcji zip() (https://docs.python.org/3/library/functions.html#zip)
paired = list(zip(names, ages))
print("Połączone listy:", paired)

# Wybieranie losowego elementu z listy używając random.choice()
try:
    random_person = random.choice(paired)  # https://docs.python.org/3/library/random.html#random.choice
    print("Wylosowana osoba:", random_person)
except IndexError:  # Obsługa potencjalnego wyjątku, gdyby lista była pusta (https://docs.python.org/3/library/exceptions.html#IndexError)
    print("Lista jest pusta!")

# Obsługa wyjątku ZeroDivisionError
try:
    result = 10 / 0  # Spowoduje błąd ZeroDivisionError
except ZeroDivisionError as e:  # https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
    print("Błąd: Dzielenie przez zero!", e)

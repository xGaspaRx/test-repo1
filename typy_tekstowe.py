# str (string)
# Typ prosty / prymitywny

miasto = "Katowice"
nazwisko = 'Kowalski'

sprawdz_typ = type(nazwisko)
fraza = "John's"

# Konkatenacja
jezyk = "Python"
typ_jezyka = "backendowy"

zdanie = jezyk + " to popularny język programowania"
zdanie2 = "Mój ulubiony język to " + jezyk + ". Jest on " + typ_jezyka + "."
# f string - Python 3.10
zdanie3 = f"Mój ulubiony język to {jezyk}. Jest on {typ_jezyka}."

print(zdanie2)
print(zdanie3)

film = "haRRy pOtTer: Zakon Feniksa"

duza_litera = film.upper()
tytul = film.title()
zastap_znaki = tytul.replace("r","_")
zastap_fraze = film.replace("Zakon Feniksa", "Czara Ognia")

policz = film.count("R")
policz_bez_czulosci_na_litery = film.lower().count("r")


print(duza_litera)
print(film)

akapit = "To jest mój tekst"

pierwsza_litera = akapit[0]
ostatnia_litera = akapit[-1]
fragment = akapit[0:7]
rozpocznij_od = akapit[5::]

print(rozpocznij_od)

# TRY...EXCEPT

print("aplikacja działa 1")

print("aplikacja działa 2")

try:
    print("try 1")
    print(zmienna)
    print("try 2")
except:
    print("złapałem błąd!")
finally:
    print("Operacja zakończona")

print("aplikacja działa 3")

x = input("Podaj liczbę: ")

# ktoś może: dzielić przez 0, brak liczby, nic nie podać
try:
    dzialanie = 100 / float(x)
    if float(x) == 7:
        raise NameError("Wiadomość błędu")
    print(dzialanie)
except ZeroDivisionError as e:
    print("Nie możesz dzielić przez 0!")
    print(e)
except ValueError as e:
    print("Musisz podać liczbę!")
    print(e)
except NameError as e:
    print("Mój własny błąd! Nie można podac liczby 7")
    print(e)
except Exception as e:
    print("Wystąpił błąd")
    print(e)
    
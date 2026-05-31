# bool
# Typ prosty / prymitywny

prawda = True
fałsz = False

a = "abc"

sprawdz1 = a.isnumeric()
sprawdz2 = a.islower()

# Bool mogę uzyskać z operatorów logicznych

x = 7 > 4 # większe od
y = 8 < 4 # mniejsze od
z = 10 >= 10 #większe bądź równe
h = 10 <= 12 # mniejsze bądź równe
rowne = "abc" == "abc" # porównanie
print(rowne)

a = 15

# Blok kodu if
# odpali się jeśli warunek spełniony
if a >= 10:
    print("zgadza się")
    print("kolejna operacja")
    print("jeszcze jedna")
else:
    print("liczba jest za mała")

typ_konta = "mod"

if typ_konta == "admin":
    print("witaj w panelu admina")
elif typ_konta == "mod":
    print("witaj moderatorze")
elif typ_konta == "klient":
    print("witaj klient")
else:
    print("nie rozpoznano")

koszyk = 198.00
kod = "ABC2026"
kraj = "PL"

# if koszyk >= 200 and kod == "ABC2026":
#     koszyk *= 0.9
#     print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
# else:
#     print("Nie udało się uzyskać rabatu")

if koszyk >= 200 and kod == "ABC2026" and kraj == "PL":
    koszyk *= 0.9
    print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
else:
    print("Nie udało się uzyskać rabatu")

# if koszyk > 150 or kod == "ABC2026":
#     print("uzyskano rabat")
# else:
#     print("brak rabatu")

login = "admin"
dzien = "sobota"
aktualizacja = True

if login == "admin123" and (dzien == "sobota" or aktualizacja):
    print("można przeprowadzić update")

# Do prawdy: -99...99, "..",[...], {...}, (...)
# Do fałszu: 0,"", None,[],{},()

konwersja = bool(12)

print(konwersja)

email = "jan@gmail.com"

if email:
    inicjaly = email[0].upper()
    print(inicjaly)

from datetime import datetime

x = datetime.now()
rok = x.year
miesiac = x.month
dzien = x.day
print(f"{dzien}/{miesiac}/{rok}")

data = x.strftime("%d/%m/%Y, %H:%M:%S")

print(data)

# Instrukcja match

match(user_role):
    case "ADMIN" | "A": # or
        print("witaj adminie")
    case "MOD":
        print("witaj w panelu moderatora")
    case "USER":
        print("Panel klienta")
    case _:
        print("Wystąpił błąd")


from datetime import datetime

month = datetime.now().month

miesiac = None
match(month):
    case 1:
        miesiac = "Styczeń"
    case 5:
        miesiac = "Maj"
    case 12:
        miesiac = "Grudzień"
    case _:
        miesiac = "Brak"

print(miesiac)
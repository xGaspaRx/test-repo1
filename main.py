
# zmienna
# nazwwa = wartosc

obliczenie =100 * 100 / 20 + 7
imie = "Anna"
czesc = "siemaneczko"

print(obliczenie)
print(imie)
print(czesc)

nazwisko = "Kowalski"
# print(nazwisko)

rok = 2025

rok = 2026

print(rok)

#snake case
kwota_do_zalaty = 120

# camel case

kwotaDoZaplaty = 120

# STALE
# NAZWA_BAZY = "mysql_db"
# PORT = 3303

# bardziej zaawansowany sposób na stałe
# CTRL + / : kometnowanie danych "#"
class Config:
    port = 3303
    host = "localhost"

print(Config.port)

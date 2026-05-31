#ZADANIE_1

imie = "Jan"
nazwisko = "Kowalski"
miasto = "Kraków"

#Konkatencja

zdanie = f"To jest { imie} { nazwisko}. Jego miesjce urodzenia to { miasto}"

print(zdanie)

#ZADANIE_2

result = "to jest krótkie zdanie na temat Jana"

zastap_znaki = result.replace(" ", "_")
print(zastap_znaki)

#ZADANIE_3

getting = "hello world"

#a)
dlugosc = len(getting)

#b)
duze_litery = getting.upper()

#c)
pierwsza_litera = getting.capitalize()

print(dlugosc)
print(duze_litery)
print(pierwsza_litera)

#ZADANIE_4

movie = "lord of the rings"

movie_title = movie.title()

print(movie_title)

#ZADANIE_5

movie = "dzisiaj jest sobota"

litera = movie[4]

print(litera)
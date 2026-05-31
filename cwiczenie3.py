#ZADANIE_1
from turtledemo.clock import current_day

user_role = "admin"
is_logged = True

if is_logged == True and user_role == "admin":
    print("Witaj w panelu admina")
elif is_logged == True and user_role == "moderator":
    print("Witaj w panelu moderatora")
elif is_logged == True and user_role == "user":
    print("Witaj w panelu user")
else:
    print("błąd logowania")

#ZADANIE_2

user_country = "Belgia"

allowed_countries = ["Polska", "Niemcy", "Czechy"]
if user_country not in allowed_countries:
    print("Dostawa towaru niemożliwa")


#ZADANIE_3

from datetime import datetime

current_hour = datetime.now().hour

if 6<= current_hour <= 12:
    print("Good Morning")
elif 12 <= current_hour <= 18:
    print("Good Afternoon")
elif current_hour > 18 or current_hour < 6:
    print("Good Evening")
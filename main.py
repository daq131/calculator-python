import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calc(a, b, operation):
    if operation == 1:
        logging.info(f" Dodaję {a} i {b}")
        return a + b
    elif operation == 2:
        logging.info(f" Odejmuję {a} i {b}")
        return a - b
    elif operation == 3:
        logging.info(f" Mnożę {a} i {b}")
        return a * b
    elif operation == 4:
        logging.info(f" Dzielę {a} i {b}")
        return a / b
    
if __name__ == "__main__":
    
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    while True:
        try:
            a = float(input("Podaj 1 składnik: "))
            b = float(input("Podaj 2 składnik: "))
            break
        except ValueError:
            logging.debug("Musisz podac liczbę")
            
    wynik = calc(a, b, operation)
    print(f"Wynik to: {wynik:.2f}")
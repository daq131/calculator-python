import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def add(list):
    if operation == 1:
        suma = sum(list[:])
        print(f"Wynik dodawania to {suma}")
    
def subtraction(list):
    if operation == 2:
        sub = list[1] - list[0]
        print(f"Wynik odejmowania liczb to {sub}")
    

def multiply(list):
    if operation == 3:
        res = 1
        for val in list:
            res = res * val
        print(f"Wynik mnożenia to {res:.2f}")
    
def division(list):
    if operation == 4:
        res = 1
        for val in list:
            res = res / val
        print(f"Wynik dzielenia to {res:.2f}")

 
if __name__ == "__main__":
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))    
    while True:
        try:
            n = int(input('podaj ile liczb chcesz uzyc do wykonania tego działania: '))
            lista = []
            for i in range(0, n):
                lista.append(int(input('')))
            break
        except ValueError:
            logging.debug("Musisz podac liczbę")
    add(lista)
    multiply(lista)
    division(lista)
    subtraction(lista)
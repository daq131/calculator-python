import sys
import logging
logging.basicConfig(level=logging.DEBUG)

# def add(lista):
#     logging.info(f"dodaję {len(lista)} elementy/ów")
#     return sum(lista)

def add(a, b):
    logging.info(f" Dodaję {a} i {b}")
    return a + b

def sub(a, b):
    logging.info(f" Odejmuję {a} i {b}")
    return a - b

def mul(a, b):
    logging.info(f" Mnożę {a} i {b}")
    return a * b

def div(a, b):
    logging.info(f" Dzielę {a} i {b}")
    return a / b

def get_data():
    op = input("Operacja (+-*/): ")
    a = input("a: ")
    b = input("b: ")
    # n = int(input('podaj ile liczb chcesz uzyc do wykonania tego działania: '))
    # lista = []
    # for i in range(0, n):
    #     lista.append(int(input('')))

    return op, int(a), int(b)


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def main():
    op, a, b = get_data()
    # result = operations["+"](lista)
    result = operations[op](a, b)
    logging.info(f" Wynik to :{result}")

main()
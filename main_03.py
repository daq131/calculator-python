def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def get_data():
	op = input("Operacja (+-*/): ")
	a = input("a: ")
	b = input("b: ")

	return op, int(a), int(b)

operations = {
	"+": add,
	"-": sub,
    "*": mul,
    "/": div
}

def main():
	op, a, b = get_data()
	result = operations[op](a, b)
	print("Wynik: ", result)

main()
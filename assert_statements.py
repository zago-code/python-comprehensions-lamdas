def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")
    try:
        if num.startswith("-") or num == '0':
            raise ValueError("Ingrese un número mayor que cero")
    except ValueError as ve:
        print(ve)
    else:
        assert num.isnumeric(), "Debes ingresar un número"
        print(divisors(int(num)))
        print("Terminó el programa")


if __name__ == '__main__':
    run()

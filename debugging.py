def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Ingrese un número mayor que cero")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return []


def run():
    while True:
        try:
            num = int(input("Ingresa un número: "))
            print(divisors(num))
            print("Terminó el programa")
            break

        except ValueError:
            print("Debes ingresar un número")


if __name__ == '__main__':
    run()

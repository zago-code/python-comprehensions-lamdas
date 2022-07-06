def run():
    # squares = []
    # for i in range(1, 101):
    #   if(i%3 != 0):
    #     squares.append(i**2)

    # generate lists without cycles (List comprehensions)
    # [element for element in iterable if condition]
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)
    print("\n")

    # CHALLENGE !!
    # Do a program that prints an array of numbers(no bigger than five-digit numbers),
    # where these are divisible among 4, 6, and 9.

    # multiples_of_4_6_and_9 = []
    # for i in range(1, 10000):
    #     if(i % 4 == 0 and i % 6 == 0 and i % 9 == 0):
    #         multiples_of_4_6_and_9.append(i)

    # List comprehensions
    multiples_of_4_6_and_9 = [i for i in range(
        1, 10001) if i % 36 == 0]  # i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(multiples_of_4_6_and_9)
    # print(len(multiples_of_4_6_and_9))


if __name__ == '__main__':
    run()

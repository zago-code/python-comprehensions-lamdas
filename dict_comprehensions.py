def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if(i % 3 != 0):
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

    # CHALLENGE!!
    # Do a program that prints an array of numbers whose keys
    # are natural numbers and its value are its square roots.

    square_roots = {i: round(pow(i, 0.5), 2) for i in range(1, 1001)}
    print(square_roots)

if __name__ == '__main__':
    run()

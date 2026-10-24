#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    """Imprime x elementos y devuelve la cantidad impresa."""
    count = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            break
        count += 1

    print()
    return count

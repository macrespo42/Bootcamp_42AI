import sys

def inverseCase(str):
    strlen = len(str)
    new_str = list()
    i = 0;
    while (i < strlen):
        if (str[i].isupper()):
            new_str.append(str[i].lower())
        elif (str[i].islower()):
            new_str.append(str[i].upper())
            i += 1
    return (new_str)

nb_of_arg = len(sys.argv) - 1
while (nb_of_arg > 0):
    sys.argv[nb_of_arg] = inverseCase(sys.argv[nb_of_arg]);
    print("".join(sys.argv[nb_of_arg])[::-1], end="")
    if (nb_of_arg > 0):
        print(" ", end="")
    nb_of_arg -= 1

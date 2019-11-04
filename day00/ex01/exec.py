import sys
import string

nb_of_arg = len(sys.argv) - 1
while (nb_of_arg > 0):
    print(sys.argv[nb_of_arg].swapcase()[::-1], end="")
    if (nb_of_arg > 0):
        print(" ", end="")
    nb_of_arg -= 1
print()

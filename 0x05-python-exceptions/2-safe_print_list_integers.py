#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    pos = num = 0
    while True:
        try:
            if pos < x:
                print("{:d}".format(my_list[pos]), end='')
                pos += 1
                num += 1
            else:
                print()
                return num
        except (ValueError, TypeError):
            pos += 1

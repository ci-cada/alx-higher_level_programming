#!/usr/bin/python3
import hidden_4


def who():
    find = dir(hidden_4)
    for i in find:
        if i[:2] != "__":
            print("{:s}".format(i))


if __name__ == "__main__":
    who()

#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_me = sorted(a_dictionary.keys())
    for key in sort_me:
        print(f"{key}: {a_dictionary[key]}")

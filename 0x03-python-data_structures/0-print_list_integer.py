#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer
my_list = [1,2,3,4]
def print_list_integer(my_list=[]):

    for i in range(0,len(my_list)):
    print("{:d}".format(my_list[i]))


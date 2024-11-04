#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length) n_list = []

for i in range(list_length).
 try:

div = my_list_1[i]/my_list_2[1] except TypeError: print("wrong type")

div = 0 except ZeroDivisionError: except IndexError: print("out of range") div = 0 finally n_list.append(div)

print("division by 0") div = 0

return n_list

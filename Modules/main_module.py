import data_module

print(data_module.patient)

# importing modules with alias
import data_module as m1

print(m1.patient)

# importing specific thing from module

from data_module import patient

print(patient)

# you can import all but directly use it by name

from data_module import *

print_detail(patient)

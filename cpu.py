###
### Author: Xin Li
### Description: CPU
###
from os import _exit as exit
gigahertz = float(input('Enter CPU gigahertz:\n'))
count = int(input('Enter CPU core count:\n'))
hyperthreading = input('Enter CPU hyperthreading (True or False):\n')
if count >= 20:
    print('\nThat is a high-performance CPU.')
    exit(0)
if hyperthreading == 'True':
    if gigahertz >= 2.7 and count >= 6:
        print('\nThat is a high-performance CPU.')
    elif 2.4 <= gigahertz < 2.7 and count >= 4:
        print('\nThat is a medium-performance CPU.')
    elif 1.9 <= gigahertz < 2.4 and count >= 2:
        print('\nThat is a low-performance CPU.')
    elif gigahertz >= 2.7:
        if count < 6:
            print('\nThat is a low-performance CPU.')
    elif 2.4 <= gigahertz < 2.7:
        if count < 4:
            print('\nThat is a low-performance CPU.')
    elif 1.9 <= gigahertz < 2.4:
        if count < 2:
            print('\nThat is a low-performance CPU.')
    else:
        print('\nThat CPU could use an upgrade.')
if hyperthreading == 'False':
    if gigahertz >= 3.2 and count >= 8:
        print('\nThat is a high-performance CPU.')
    elif 2.8 <= gigahertz < 3.2 and count >= 6:
        print('\nThat is a medium-performance CPU.')
    elif 2.4 <= gigahertz < 2.8 and count >= 2:
        print('\nThat is a low-performance CPU.')
    elif gigahertz >= 3.2:
        if count < 8:
            print('\nThat is a low-performance CPU.')
    elif 2.8 <= gigahertz < 3.2 :
        if count < 6:
            print('\nThat is a low-performance CPU.')
    elif 2.4 <= gigahertz < 2.8:
        if count < 2:
            print('\nThat is a low-performance CPU.')
    else:
        print('\nThat CPU could use an upgrade.')

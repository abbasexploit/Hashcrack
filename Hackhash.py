import os

import colored

os.system('cls' or 'clear')

os.system('color a')

import hashlib

from Banner import banner

banner()

hash_input = input('Please Enter your hash for crack: ')

list_password  =input ('Please Enter your file list password name: ')

file = open(list_password,'r').readlines()



for i in file :

    hash = hashlib.md5(i.strip().encode()).hexdigest()

    if hash_input == hash :

        print (f'password is : {i.strip()}')

        break

else:

    print ('password not found')

    exit()

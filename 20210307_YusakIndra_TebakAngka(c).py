#
# Copyright (c) 2021- Team 4 Talend Imagine
# Yusak Indra (yusakibdrah@gmail.com)
#
# Licensed under the terms of the MIT License
# (see spyder_kernels/__init__.py for details)
# -----------------------------------------------------------------------------
#
# IMPORTANT NOTE: 
# Don't add a coding line here! It's not necessary for site files
# 
# Spyder consoles sitecustomize
#

import bdb
from distutils.version import LooseVersion
import io
import os
import os.path as osp
import pdb
import shlex
import sys
import time
import warnings
import random
import getpass

from IPython.core.getipython import get_ipython


#==============================================================================
# Function Mainan Acak:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================
def mainanacak(nama):
    acak = random.randrange(1,100)
    peluang  = 10
    nilai = 100
    
    while peluang > 0:
        data = int(input("Masukan Angka Tebakan: "))
        if data > acak:
            peluang -=1
            nilai -=10
            print("Angka tebakan nilai lebih besar")
            print(f'Tersisa {peluang} kesempatan lagi\n')
            print(f'Sisa {nilai} point lagi\n')
        if data < acak:
            peluang -=1
            nilai -=10
            print("Angka tebakan nilai lebih kecil")
            print(f'Tersisa {peluang} kesempatan lagi\n')
            print(f'Sisa {nilai} point lagi\n')
        if data == acak:
            peluang -=1
            print("Selamat, tebakanmu benar")
            print(f'nilai score anda {nilai} point \n')
            daftarscore(nama,str(nilai))
            print_menu()
        if peluang == 0:
            print("Kesempatanmu telah habis, kamu kalah")
            print(f'nilai score anda {nilai} point \n')
            print(f'Angka tebakan adalah {acak}')
            daftarscore(nama,str(nilai))
            print_menu()


#==============================================================================
# Function Daftar:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================

def daftar():
    username = input("Masukan UserName : ")
    password = getpass.getpass("Masukan Password : ")
    file = open("accountfile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()

#==============================================================================
# Function Login:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================

#def login():
#    username = input("Masukan UserName :")
#    password = getpass.getpass("Masukan Password :")  
#    for line in open("accountfile.txt","r").readlines(): # Read the lines
#        login_info = line.split() # Split on the space, and store the results in a list of two strings
#        if username == login_info[0] and password == login_info[1]:
#            print("User dan Password Benar!")
#            return username
#        else :
#            print("User Password Tidak Benar")
#            return False

def login():

    passwordAttemptLoop = 3 #attempts you want to give the user
    print("You have chosen to login!\n")

    while passwordAttemptLoop > 0:
        usernameAttempt = input("Please print your username below\n")
        passwordAttempt = getpass.getpass("Please print your password below\n")

        for line in open("/Users/jusak/Desktop/accountfile.txt","r").readlines():
            loginDetails = line.split()
            if usernameAttempt == loginDetails[0] and passwordAttempt == loginDetails[1]:
                print("OK")
                return True

        print("Your username and/ or password is incorrect! Please try again!")
        passwordAttemptLoop = passwordAttemptLoop - 1
        

    print('You are out of login attempts. Please try again later')
    return False

#==============================================================================
# Input Score:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================    
def showscrore():
    lines = []
    
    with open('userscore.txt') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            print(f'line {count}: {line}')   


#==============================================================================
# Function Dafter Score:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================

def daftarscore(username,score):
    file = open("userscore.txt","a")
    file.write(username)
    file.write(" ")
    file.write(score)
    file.write("\n")
    file.close()
        
#==============================================================================
# Main Menu:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================

## menu Tebak Angka
def print_menu():   
    print (30 * "*")  
    print (2 * " ", "PERMAINAN TEBAK ANGKA")
    print (30 * "*")
    print ("1. Main")
    print ("2. Daftar")
    print ("3. High Score")
    print ("4. Keluar")
    print (30 * "*")
    
    pilihmenu()

  
#==============================================================================
# Main Menu:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================    
def pilihmenu():
     choice = input("Enter your choice [1-4]: ")
         
     if choice == "1":
         hasil = login()
         if (hasil!=False):
             print ("Point Awal anda 100")
             mainanacak(hasil)
         else:
             print ("user password salah")
             print_menu()
         
     if choice == "2":
         daftar()
         print_menu()
         
     if choice == "3":
         showscrore()
         print_menu()
         
     if choice == "4":
         print ("Terima Kasih")
         quit()
         
        

#==============================================================================
# Main Menu:
#
# We avoid importing spyder here, so we are handling Python 3 compatiblity
# by hand.
#==============================================================================    

print_menu()  


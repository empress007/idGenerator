from ids import id_card

# generate f0r 20 personnels 
import sys

# RUN PROGRAM 
for n in range(20):
    if n < 5 :
        print('EXECUTIVE RESERVED ID')
    elif n == 20 :
        sys.exit('completed')
    else :  
      name = input('Enter your your name: ')
      id_card(name,n)

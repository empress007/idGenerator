
import random
import sys

def id_card(name,n):
    letters= ['a','b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = random.sample(letters,2)
    number = random.sample(numbers,2)
    letter.extend(number)
    id = [l.replace("'", '') for l in letter]
    random.shuffle(id)
    generatedId = ''.join(id)
    generatedIdd = "fh-" + generatedId
    
    print("------------------------------------------------------")
    print(f"Dear {name}, Your identification number is : {generatedIdd} and assigned to Location{n+1}")
    print("------------------------------------------------------")
    print('')
for n in range(20):
    if n < 5 :
        print('EXECUTIVE RESERVED ID')
    elif n == 20 :
        sys.exit('completed')
    else :  
      name = input('Enter your your name: ')
      id_card(name,n)
 

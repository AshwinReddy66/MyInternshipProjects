import random 
import string 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
length=int(input('Enter the length of the passward ,minimum length is 6 :')) 
number=int(input('How many passwards do you want?')) 
def passward_generator(): 
    passward='' 
    for _ in range(length-5): 
        passward+=random.choice(letters) 
    for _ in range(3): 
        passward+=random.choice(numbers) 
    for _ in range(2): 
        passward+=random.choice(symbols) 
    print(passward) 
for passward in range(number): 
 passward_generator()

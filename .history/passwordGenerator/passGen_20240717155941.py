import string 
import random

all_characters = string.ascii_letters + string.digits + string.punctuation 
length = int(input("Enter the Length of the password"))

password = .join(random.choices(all_characters,k=))
import random
import string

def generate_password(length):
   
    low_let = string.ascii_lowercase
    upper_let = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

  
    all_characters = low_let + upper_let + digits + special_characters

  
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    
    password_length = int(input("Enter the desired length of the password: "))

   
    password = generate_password(password_length)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()

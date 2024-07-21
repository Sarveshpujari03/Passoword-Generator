import random
import string

def Easy(a):
    characters = string.ascii_letters 
    return ''.join(random.choices(characters, k=a))
    return Password
def Medium(a):
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choices(characters, k=a))
    return Password
def Hard(a):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=a))
    return Password
def main():
    print("Welcome to the password generator!!!")
    a=int(input("Please enter the length of the password you want to generate:"))
    print("What should be the complexity of the password according to you?")
    print("Please select an option below")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice: ")
    if(choice ==1):
        Easy()
    elif(choice==2):
        Medium()
    elif(choice==3):
        Hard()
    Password = Easy(a)
    Password = Medium(a)
    Password = Hard(a)


    print(f"Your password is: {Password}")

if __name__ == "__main__":
    main()
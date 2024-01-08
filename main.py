# This is simple Random Password Generator App
import random

def generatePassword(passwordlength):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    passwords = [] 
    for i in passwordlength:
        password = "" 
        for j in range(i):
            index = random.randrange(len(alphabets))
            password = password + alphabets[index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        passwords.append(password)

    return passwords

def replaceWithNumber(password):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2)
        password = password[0:replace_index] + str(random.randrange(10)) + password[replace_index+1:]
        return password

def replaceWithUppercaseLetter(password):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(password)//2,len(password))
        password = password[0:replace_index] + password[replace_index].upper() + password[replace_index+1:]
        return password

def main():
    numberOfPasswords = int(input("How many random passwords do you want to generate? "))
    print("Generating " +str(numberOfPasswords)+" passwords")
    print("Minimum length of password should be 3")
    
    passwordLengths = []
    for i in range(numberOfPasswords):
        length = int(input("Enter the length of Password " + str(i+1) + ": "))
        if length<3:
            length = 3
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i in range(numberOfPasswords):
        print ("Password "+str(i+1)+" = " + Password[i])

main()

# Trying to create a number guessing game that allows the computer try to guess a number
# import random as rand

# SecretNumber = 10
# count = 3

# def DisplayRandom():
#     num = rand.randint(1,11)
#     print(f"Computer Guess: {num}")

#     while count == 3:
#         if num != SecretNumber:
#             return f"{num} is Incorrect!"
#             break
#         else: 

#             return f"{num} is Correct"
#             break
            
            
# print(DisplayRandom())

#Create a number guessing game that allows the user try to guess a number

number = 10

user = int(input("Try "))
        
if user < number:
    print("Too Low")
    
    
elif user > number:
    print("Too high")
    
elif user == number:
    print("Congratulations! You guessed the secret number Right")
     
    
     
    
    
import random

print("Welcome the the number guessing Game.")
print("Im Thinking of a number between 1 and 100.")

r_number=random.randint(1,100)
# print(f"psssst, The correct answer is {r_number}.")

mode=input("Choose a Difficulty, Type 'easy' or 'hard': ")
def easy():
  print("You have 10 attempts left to guess the number.")
  user_guess=int(input("Make a Guess: "))
  if user_guess!=r_number:
    for item in range(9,0,-1):
      print(f"You have {item} attempts left to guess the number. ")
      user_guess=int(input("Make a Guess: "))
      if user_guess==r_number:
        print(f"You Got it The Answer is {r_number}. ")
        quit()
        
      elif r_number>user_guess:
        print("Too Low.")
        print("Guess Again.")
      elif r_number<user_guess:
        print("Too High.")
        print("Guess Again.")
    
    print("You have used all your attempts \n You Lost.")
  else:  
    print(f"You Got it The Answer is {r_number}. ")

def hard():
  print("You have 5 attempts left to guess the number.")
  user_guess=int(input("Make a Guess: "))
  if user_guess!=r_number:
    for item in range(4,0,-1):
      print(f"You have {item} attempts left to guess the number. ")
      user_guess=int(input("Make a Guess: "))
      if user_guess==r_number:
        print(f"You Got it The Answer is {r_number}.")
        quit()
        
      elif r_number>user_guess:
        print("Too Low.")
        print("Guess Again.")
      elif r_number<user_guess:
        print("Too High.")
        print("Guess Again.")
    
    print("You have used all your attempts..\nYou Lost.")
  else:  
    print(f"You Got it The Answer is {r_number}")
  

if mode=="easy":
  easy()
else:
  hard()
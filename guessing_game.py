import random

def start_game():
    print("============      ============")
    print("Welcome to Number Guessing Game!")
    print("============      =============")
    
    random_number= random.randint(1,10)
    counter = 0
    
    while True:
        try:
            guess_number = int(input("\nGuess a number between 1-10:  "))
        except ValueError as err:
            print("{}  ,Please pick only numbers between 1-10.".format(err))
           
        else:
            if guess_number < 1 or guess_number > 10:
                print("****Pick a number between 1-10")
            else:
            
                if guess_number > random_number:
                    print("It's too high.")
                    counter += 1
                    random_number= random.randint(1,10)
                elif guess_number < random_number:
                        print("It's too low")
                        counter += 1
                        random_number= random.randint(1,10)
                elif guess_number == random_number:
                    print("You guessed right!!")
                    counter += 1
                    print("You attempted {} time(s).".format(counter))
                
                    again = input("\nWould you like to try again? [Y]es/[N]o?  ")
                    if again.lower() != 'y':
                        print("Thanks for playing!")
                        print("Goodby")
                        break
                    else:
                        random_number= random.randint(1,10)
                        continue
                
  

start_game()

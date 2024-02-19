import random

def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "it is draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or\
         (user_choice == 'scissors' and computer_choice == 'paper') or\
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def game_play():
    user_choice = input("choose rock,paper,scissors:").lower()
    while user_choice not in ['rock','paper','scissors']:
        print("nvalid! choose rock,paper,scissors")
        user_choice = input("choose rock,paper,scissors:").lower()

    computer_choice = random.choice(['rock','paper','scissors'])

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    results = winner(user_choice, computer_choice)
    print(results)
    return results

def main():
    user_score = 0
    computer_score = 0
    one_more = True
    while one_more:
        results = game_play()
        if "win" in results:
            user_score +=1
        elif "lose" in results:
            computer_score +=1


        
        print(f"Score: Yours {user_score} - {computer_score} Computer")

        choice = input("Do you want to play one more? (yes/no): ").lower()
        while choice not in ['yes', 'no']:
            print("Invalid choice! Please enter yes or no.")
            choice = input("Do you want to play one more? (yes/no): ").lower()

        if choice == 'no':
            one_more = False

    print("Thanks for playing..!")

if __name__ == "__main__":
    main()    
        



        
          
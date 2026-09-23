import random
import sys

def display_banner():
    """Displays the game welcome banner."""
    print("=" * 45)
    print(" 🎮  WELCOME TO ROCK, PAPER, SCISSORS!  🎮 ")
    print("=" * 45)
    print("First to score 3 points wins the game!")
    print("Type 'exit' or 'quit' anytime to stop playing.\n")

def main():
    display_banner()
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    winning_score = 3

    # Main game loop
    while player_score < winning_score and computer_score < winning_score:
        print("-" * 45)
        player_input = input("Choose (rock / paper / scissors): ").strip().lower()

        # Check for exit command
        if player_input in ['exit', 'quit']:
            print("\n👋 Thanks for playing! Goodbye!")
            sys.exit()

        # Validate user input
        if player_input not in choices:
            print("⚠️  Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer randomly selects a choice
        computer_choice = random.choice(choices)

        print(f"\n👤 You chose:     {player_input.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}\n")

        # Determine round winner
        if player_input == computer_choice:
            print("🤝 It's a tie!")
        elif (player_input == 'rock' and computer_choice == 'scissors') or \
             (player_input == 'paper' and computer_choice == 'rock') or \
             (player_input == 'scissors' and computer_choice == 'paper'):
            player_score += 1
            print("✨ You win this round!")
        else:
            computer_score += 1
            print("💻 Computer wins this round!")

        # Display current scores
        print(f"\n📊 CURRENT SCORE | You: {player_score}  VS  Computer: {computer_score}")

    # Final result display
    print("\n" + "=" * 45)
    print("                 GAME OVER                 ")
    print("=" * 45)
    if player_score > computer_score:
        print("🎉 CONGRATULATIONS! YOU WON THE GAME! 🏆")
    else:
        print("😭 YOU LOST! BETTER LUCK NEXT TIME! 🤖")

    print(f"\nFINAL SCORE -> Player: {player_score} | Computer: {computer_score}")
    print("=" * 45)

if __name__ == "__main__":
    main()

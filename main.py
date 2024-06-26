#!/usr/bin/env python3

import random

from flask import Flask, jsonify

CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

app = Flask(__name__)

def run_a_quick_game():
    pass

@app.route('/rock', methods=['POST'])
def rock():
    computer_choice = random.choice(CHOICES)
    result = compare_choices('rock', computer_choice)
    return jsonify(result=result), 200

@app.route('/paper', methods=['POST'])
def paper():
    computer_choice = random.choice(CHOICES)
    result = compare_choices('paper', computer_choice)
    return jsonify(result=result), 200

@app.route('/scissors', methods=['POST'])
def scissors():
    computer_choice = random.choice(CHOICES)
    result = compare_choices('scissors', computer_choice)
    return jsonify(result=result), 200

@app.route('/spock', methods=['POST'])
def spock():
    computer_choice = random.choice(CHOICES)
    result = compare_choices('spock', computer_choice)
    return jsonify(result=result), 200

@app.route('/lizard', methods=['POST'])
def lizard():
    computer_choice = random.choice(CHOICES)
    result = compare_choices('lizard', computer_choice)
    return jsonify(result=result), 200

def compare_choices(user_choice, computer_choice):
    user_choice = user_choice.lower()
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice in ['scissors', 'lizard']) or \
        (user_choice == 'scissors' and computer_choice in ['paper', 'lizard']) or \
        (user_choice == 'paper' and computer_choice in ['rock', 'spock']) or \
        (user_choice == 'spock' and computer_choice in ['scissors', 'rock']) or \
        (user_choice == 'lizard' and computer_choice in ['spock', 'paper']):
        return "You win!"
    else:
        return "You lose!"

def get_user_choice():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Spock")
    print("5. Lizard")
    choice = input()
    if choice == '1':
        return 'rock'
    elif choice == '2':
        return 'paper'
    elif choice == '3':
        return 'scissors'
    elif choice == '4':
        return 'spock'
    elif choice == '5':
        return 'lizard'
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        return get_user_choice()

def main():
    continue_game = 'yes'

    while continue_game.lower() == 'yes':
        computer_choice = random.choice(CHOICES)
        user_choice = get_user_choice()

        if user_choice.lower() not in CHOICES:
            print("Invalid choice, please try again.")
            continue

        print(f"\nComputer chose {computer_choice}")
        print(f"You chose {user_choice}")

        result = compare_choices(user_choice, computer_choice)
        print(result)

        # continue_game = input("\nDo you want to continue? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    # main()
    app.run(debug=True)


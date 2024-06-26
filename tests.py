import unittest
from main import compare_choices

class TestCompareChoices(unittest.TestCase):
    def test_tie(self):
        choices = ['rock', 'paper', 'scissors', 'spock', 'lizard']
        for choice in choices:
            self.assertEqual(compare_choices(choice, choice), "It's a tie!")

    def test_user_wins(self):
        winning_combinations = [
            ('rock', 'scissors'),
            ('rock', 'lizard'),
            ('scissors', 'paper'),
            ('scissors', 'lizard'),
            ('paper', 'rock'),
            ('paper', 'spock'),
            ('spock', 'scissors'),
            ('spock', 'rock'),
            ('lizard', 'spock'),
            ('lizard', 'paper')
        ]
        for user_choice, computer_choice in winning_combinations:
            self.assertEqual(compare_choices(user_choice, computer_choice), "You win!")

    def test_user_loses(self):
        losing_combinations = [
            ('rock', 'paper'),
            ('rock', 'spock'),
            ('scissors', 'rock'),
            ('scissors', 'spock'),
            ('paper', 'scissors'),
            ('paper', 'lizard'),
            ('spock', 'paper'),
            ('spock', 'lizard'),
            ('lizard', 'rock'),
            ('lizard', 'scissors')
        ]
        for user_choice, computer_choice in losing_combinations:
            self.assertEqual(compare_choices(user_choice, computer_choice), "You lose!")

if __name__ == '__main__':
    unittest.main()

import random
# Python version 3.12.7
def generate_equation():
    """Generate a random equation and return coefficient, result, and answer."""
    coefficient = random.randint(1, 10)
    answer = random.randint(1, 10)
    result = coefficient * answer
    return coefficient, result, answer

def display_equation(coefficient, result):
    """Display the equation to the user."""
    print(f"\n{coefficient} × x = {result}")

def get_user_answer():
    """Get and validate user input."""
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            print("Please enter a valid number!")

def play_game():
    """Main game function."""
    score = 0
    num_questions = 5
    
    print("Welcome to the Math Equation Game!")
    print(f"Solve {num_questions} equations.\n")
    
    for question_num in range(1, num_questions + 1):
        print(f"Question {question_num}:")
        
        # Generate and display equation
        coefficient, result, correct_answer = generate_equation()
        display_equation(coefficient, result)
        
        # Get user's answer
        user_answer = get_user_answer()
        
        # Check answer
        if user_answer == correct_answer:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The answer is {correct_answer}")
    
    # Show final score
    print(f"\nGame Over!")
    print(f"Your score: {score}/{num_questions}")

# Run the game
play_game()

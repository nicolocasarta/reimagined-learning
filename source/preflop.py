def check_poker_move(Position, Hand, Action):
    # Check Position
    if Position != 'UTG':
        return 'Error: Only UTG position is acceptable.'

    # Check Hand
    # You can add more complex validation logic for poker hands if needed
    # For simplicity, we are assuming any two cards input is valid
    if len(Hand) != 4:
        return 'Error: Invalid poker hand.'

    # Check Action
    if Action.lower() not in ['raise', 'fold']:
        return 'Error: Action must be either "raise" or "fold".'

    # If all checks passed, return 'Correct'
    return 'Correct'

# Example usage:
user_position = input("Enter position: ")
user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ")
user_action = input("Enter action (raise or fold): ")

result = check_poker_move(user_position, user_hand, user_action)
print(f"Result: {result}")
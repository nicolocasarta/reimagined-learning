def check_poker_move(Position, Hand, Action):
    # Check Position
    if Position != 'utg':
        return 'Error: Only UTG position is acceptable.'

    # Check Hand
    # For simplicity, we are assuming any two cards input is valid

    #Valid cards
    cardArray = ['a','k','q','j','2','3','4','5','6','7','8','9','t']
    
    valid = 0

    #Checks first and third position for valid card values

    for i in cardArray:
        if Hand[0] == i:
            valid += 1
        if Hand[2] == i:
            valid += 1

    if valid != 2:
        return 'Error: Invalid Poker Hand'      
   
   #Valid suits
    
    suitArray = ['s','d','h','c']

    #Checks second and fourth position for valid suit values

    for i in suitArray:
        if Hand[1] == i:
            valid += 1
        if Hand[3] == i:
            valid += 1

    if valid != 4:
        return 'Error: Invalid Poker Hand'  
    
    if len(Hand) != 4:
        return 'Error: Invalid Poker Hand' 
    
    if Hand[0] == Hand[2]:
        if Hand[1] == Hand[3]:
            return 'Error: Invalid Poker Hand'


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
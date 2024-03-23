def check_poker_move(position, hand, action):
    # Check Position
    if position != 'utg':
        return 'Error: Only UTG position is acceptable.'

    # Check Hand
    if len(hand) != 4:
        return 'Error: Invalid Poker Hand' 

    #Valid cards
    cardArray = ['a','k','q','j','2','3','4','5','6','7','8','9','t']
    
    valid = 0

    #Checks first and third position for valid card values

    for i in cardArray:
        if hand[0] == i:
            valid += 1
        if hand[2] == i:
            valid += 1

    if valid != 2:
        return 'Error: Invalid Poker Hand'      
   
   #Valid suits
    
    suitArray = ['s','d','h','c']

    #Checks second and fourth position for valid suit values

    for i in suitArray:
        if hand[1] == i:
            valid += 1
        if hand[3] == i:
            valid += 1

    if valid != 4:
        return 'Error: Invalid Poker Hand'  
    
    
    if hand[0] == hand[2]:
        if hand[1] == hand[3]:
            return 'Error: Invalid Poker Hand'


    # Check Action
    if action.lower() not in ['raise', 'fold']:
        return 'Error: Action must be either "raise" or "fold".'

    # If all checks passed, return 'Correct'
    return 'Correct'

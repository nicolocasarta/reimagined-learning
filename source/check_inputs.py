
def check_position(position):

    accepted_positions = ["utg", "utg+1", "lj","hj", "co", "sb", "btn"]
    # Check Position
    if position not in accepted_positions:
        return 'Error: Position Not Acceptable.'
    return True

def check_hand(hand):
    # Check Hand
    if len(hand) != 4:
        return 'Error: Invalid Poker Hand' 

    #Valid cards
    card_list = ['a','k','q','j','2','3','4','5','6','7','8','9','t']
    
    
    #Checks first and third position for valid card values
    if hand[0] not in card_list or hand[2] not in card_list:
        return 'Error: Invalid Poker Hand'
        
   
   #Valid suits
    suit_list = ['s','d','h','c']

    #Checks second and fourth position for valid suit values
    if hand[1] not in suit_list or hand[3] not in suit_list:
        return 'Error: Invalid Poker Hand'
    
    
    # Checks if duplicate ranks have same suit
    if hand[0] == hand[2]:
        if hand[1] == hand[3]:
            return 'Error: Invalid Poker Hand'
        

    return True

def check_action(action):
    # Check Action
    if action.lower() not in ['raise', 'fold', 'bet', 'call']:
        return "Error: Action must be raise or fold or bet or call"

    # If all checks passed, return 'Correct'
    return True

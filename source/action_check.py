from source.utils.util import jason_to_dict

# dictionary that holds all preflop proper actions for a given hand
PREFLOP_ACTION = jason_to_dict("preflop_action.json")

# get the correct action from a hand in a position
def get_correct_action(position, hand):
    # locate the correct action from a hand at the position
    correct_action = PREFLOP_ACTION[position][hand]
    return correct_action


#check if user action matches the correct response
def action_check(correct_action, user_action):

    if (user_action == correct_action):
        print("Your decision to " + user_action.upper() + " was CORRECT!")
    else:
        print("Your decision to " + user_action.upper() + " was INCORRECT!")







    
    

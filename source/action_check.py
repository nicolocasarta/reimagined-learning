from source.utils.util import jason_to_dict

# dictionary that holds all preflop proper actions for a given hand
PREFLOP_ACTION = jason_to_dict("preflop_action.json")

#check if user action matches the correct response
def action_check(position, hand, action):

    if position == "utg":
        proper_action = preflop_utg_action(hand)
    if position == "utg+1":
        proper_action = preflop_utg1_action(hand)

    if position == "btn":
        proper_action = preflop_btn_action(hand)

    if position == "lj":
        proper_action = preflop_lj_action(hand)


    if (action == proper_action):
        print("Your decision to " + action.upper() + " was CORRECT!")
    else:
        print("Your decision to " + action.upper() + " was INCORRECT!")



def preflop_utg_action(hand):
    # get dictionary at key, "utg_action"
    utg = PREFLOP_ACTION["utg_action"]
    # get the action from the key associated with the hand
    action = utg[hand]
    
    return action



def preflop_utg1_action(hand):
    # get dictionary at key, "utg1_action"
    utg1 = PREFLOP_ACTION["utg1_action"]
    # get the action from the key associated with the hand
    action = utg1[hand]
    
    return action
   



def preflop_btn_action(hand):
    # get dictionary at key, "btn_action"
    btn = PREFLOP_ACTION["btn_action"]
    # get the action from the key associated with the hand
    action = btn[hand]
    
    return action



def preflop_lj_action(hand):
    # get dictionary at key, "lj_action"
    lj = PREFLOP_ACTION["lj_action"]
    # get the action from the key associated with the hand
    action = lj[hand]
    
    return action





    
    

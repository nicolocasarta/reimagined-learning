

#check if user action matches the correct response
def action_check(position, hand, action):

    if position == "utg":
        proper_action = preflop_utg_action(hand)
    if position == "utg+1":
        proper_action = preflop_utg1_action(hand)

    if (action == proper_action):
        print("Your decision to " + action.upper() + " was CORRECT!")
    else:
        print("Your decision to " + action.upper() + " was INCORRECT!")



def preflop_utg_action(hand):

    #hands that the user should raise when in utg position
    good_hands = ["aa", "aks", "aqs", "ajs", "ats", "a9s", "a8s", "a7s", "a6s", "a5s", "a4s", "a3s",
    "ako", "aqo", "kk", "kqs", "kjs", "kts", "k9s", "kqo", "qq", "qjs", "qts", "jj", "jts", "tt", "99",
    "88", "77", "65s"]

    # if the user's hand is a good hand, then raise
    if hand in good_hands:
        return "raise"
    # otherwise fold
    return "fold"


def preflop_utg1_action(hand):

    good_hands = ["aa", "aks", "aqs", "ajs", "ats", "a9s", "a8s", "a7s", "a6s", "a5s", "a4s", "a3s",
                  "ako", "kk", "kqs", "kjs", "kts", "k9s", "aqo", "kqo", "qq", "qjs", "qts", "ajo", 
                  "jj", "jts", "tt", "t9s", "99", "88", "77", "65s"]
    
    if hand in good_hands:
        return "raise"
    return "fold"
   










    
    

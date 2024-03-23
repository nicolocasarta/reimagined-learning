

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
   

<<<<<<< HEAD

def preflop_btn_action(hand):
    good_hands = ["aa", "aks", "aqs", "ajs", "ats", "a9s", "a8s", "a7s", "a6s", "a5s", "a4s", "a3s",
                  "a2s", "ako", "kk", "kqs", "kjs", "kts", "k9s", "k8s", "k7s", "k6s", "k5s", "k4s", 
                    "k3s", "k2s", "aqo", "kqo", "qq", "qjs", "qts", "q9s", "q8s", "q7s", "q6s", "q5s", 
                    "q4s", "q3s", "ajo", "kjo", "qjo", "jj", "jts", "j9s", "j8s", "j7s", "j6s", "j5s",
                     "ato", "kto", "qto", "jto", "tt", "t9s", "t8s", "t7s", "t6s", "a9o", "k9o", "q9o",
                      "k9o", "q9o", "j9o", "t9o", "99", "98s", "97s", "96s", "a8o", "a7o", "a6o", "a5o",
                       "a4o", "a3o", "88", "87s", "86s", "77", "76s", "75s", "66", "65s", "55", "54s", 
                       "44", "33", "22" ]
=======
def preflop_lj_action(hand):
    good_hands = ["aa", "aks", "aqs", "ajs", "ats", "a9s", "a8s", "a7s", "a6s", "a5s", "a4s", "a3s",
                  "a2s", "ako", "kk", "kqs", "kjs", "kts", "k9s", "k8s", "k7s", "aqo", "kqo", "qq", "qjs", 
                  "qts", "ajo", "jj", "jts", "tt", "t9s", "99", "88", "77", "66", "65s"]
    
    if hand in good_hands:
        return "raise"
    return "fold"
>>>>>>> main


    if hand in good_hands:
        return "raise"
    return "fold"




    
    

from source.cards import handReformat


#check if user action matches the correct response
def responseCheck(position, hand, action):

    hand = handReformat(hand)

    if (action == properResponse(position, hand)):
        print("Your decision to " + action.upper() + " was CORRECT!")
    else:
        print("Your decision to " + action.upper() + " was INCORRECT!")

#return proper response based on user position
def properResponse(position, hand):

    if (position == "utg"):
        return utgResponse(hand)
    else:
        print("DATA FOR DECISION NOT AVAILABLE YET")


def utgResponse(hand):

    #hands that the user should raise when in utg position
    goodHands = ["aa", "aks", "aqs", "ajs", "ats", "a9s", "a8s", "a7s", "a6s", "a5s", "a4s", "a3s",
    "ako", "aqo", "kk", "kqs", "kjs", "kts", "k9s", "kqo", "qq", "qjs", "qts", "jj", "jts", "tt", "99",
    "88", "77", "65s"]

    #loop through good hands
    for i in goodHands:
        #if user hand matches one of the good hands, then return raise
        if hand == i:
            return "raise"
    #if user hand does not match one of the good hands, then return fold
    return "fold"






# # test code
# user_position = input("Enter position: ")
# user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ")
# user_action = input("Enter action (raise or fold): ")

# responseCheck(user_position, user_hand, user_action)




    
    

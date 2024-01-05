


#check if user action match the correct response
def responseCheck(position, hand, action):

    hand = handFormat(hand)

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
    "ako", "aqo", "kk", "kqs", "kjs", "kts", "k9s", "kqo", "qq", "qjs", "qts", "jj", "jts", "tt", "t9s", 
    "99", "88", "77", "66","65s", "55", "54s"]

    #loop through good hands
    for i in goodHands:
        #if user hand matches one of the good hands, then return raise
        if hand == i:
            return "raise"
    #if user hand does not match one of the good hands, then return fold
    return "fold"


#reformat user hand to match the format in goodHands array
def handFormat(hand):

    #if card values match, suited or unsuited designation is not needed
    if hand[0] == hand[2]:
        newHand = hand[0] + hand[2]

        return newHand

#TODO: if suits match, make newHand = to the value of the cards and place an s at the end eg. aks
#      if suits do not match, place o at the end eg. ako
#      write a funaction that makes sure the higher value card comes first eg. aks not kas



#test code
user_position = input("Enter position: ")
user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ")
user_action = input("Enter action (raise or fold): ")

responseCheck(user_position, user_hand, user_action)




    
    

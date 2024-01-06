
#reformat user hand to match the format in goodHands array
def handReformat(hand):

    #if card values match, suited or unsuited designation is not needed
    if hand[0] == hand[2]:
        newHand = hand[0] + hand[2]
        
        return newHand
    
    #if suits match, make newHand = to the value of the cards and place an s at the end eg. aks
    elif hand[1] == hand[3]:
        newHand = hand[0] + hand[2] + "s"
        
        return handReorder(newHand)
    
    #if suits do not match, place o at the end eg. ako
    else:
        newHand = hand[0] + hand[2] + "o"

        return handReorder(newHand)
    

   
#reorder the user hand: card of higher value comes before card of lower value   
def handReorder(hand):

    #if 'a' is in second position, place it in first position
    if (hand[1] == 'a'):
        newHand = hand[1] + hand[0] + hand[2]
        return newHand

    #if 'k' is in the second position, but a higher value than first position, swap places
    elif (hand[1] == 'k' and hand[0] != 'a'):
        newHand = hand[1] + hand[0] + hand[2]
        return newHand

    #if 'q' is in the second position, but a higher value than first position, swap places
    elif (hand[1] == 'q' and (hand[0] != 'a' and hand[0] != 'k')):
        newHand = hand[1] + hand[0] + hand[2]
        return newHand
    
    #if 'j' is in the second position, but a higher value than first position, swap places
    elif (hand[1] == 'j' and (hand[0] != 'a' and hand[0] != 'k' and hand[0] != 'q')):
        newHand = hand[1] + hand[0] + hand[2]
        return newHand
    
    #if 't' is in the second position, but a higher value than first position, swap places
    elif(hand[1] == 't' and (hand[0] != 'a' and hand[0] != 'k' and hand[0] != 'q' and hand[0] != 'j')):
        newHand = hand[1] + hand[0] + hand[2]
        return newHand
    
    #if the card values are numeric, then place higher number in first position
    elif (hand[0] < hand[1] and hand[0] < 'a'):
        newHand = hand[1] + hand[0] + hand[2]
        return newHand
    
    #if order is correct, return hand
    return hand
    

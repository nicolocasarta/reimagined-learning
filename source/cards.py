
#reformat user hand to match the format in goodHands array
def handReformat(hand):

    #if card values match, suited or unsuited designation is not needed
    if hand[0] == hand[2]:
        simple_hand = hand[0] + hand[2]
        
        return simple_hand
    
    #if suits match, make newHand = to the value of the cards and place an s at the end eg. aks
    elif hand[1] == hand[3]:
        simple_hand = hand[0] + hand[2] + "s"
        
        return simple_hand
    
    #if suits do not match, place o at the end eg. ako
    else:
        simple_hand = hand[0] + hand[2] + "o"

        return simple_hand
    

   
#reorder the user hand: card of higher value comes before card of lower value   
def handReorder(hand):

    #if card values match, there is no need to reorder
    if(hand[0] == hand[1]):
        return hand
    
    #if 'a' is in second position, place it in first position
    elif (hand[1] == 'a'):
        reordered_hand = hand[1] + hand[0] + hand[2]
        return reordered_hand

    #if 'k' is in the second position, but a higher value than first position, swap places
    elif (hand[1] == 'k' and hand[0] != 'a'):
        reordered_hand = hand[1] + hand[0] + hand[2]
        return reordered_hand

    #if 'q' is in the second position, but a higher value than first position, swap places
    elif (hand[1] == 'q' and (hand[0] != 'a' and hand[0] != 'k')):
        reordered_hand = hand[1] + hand[0] + hand[2]
        return reordered_hand
    
    #if 'j' is in the second position, but a higher value than first position, swap places
    elif (hand[1] == 'j' and (hand[0] != 'a' and hand[0] != 'k' and hand[0] != 'q')):
        reordered_hand = hand[1] + hand[0] + hand[2]
        return reordered_hand
    
    #if 't' is in the second position, but a higher value than first position, swap places
    elif(hand[1] == 't' and (hand[0] != 'a' and hand[0] != 'k' and hand[0] != 'q' and hand[0] != 'j')):
        reordered_hand = hand[1] + hand[0] + hand[2]
        return reordered_hand
    
    #if the card values are numeric, then place higher number in first position
    elif (hand[0] < hand[1] and hand[0] < 'a'):
        reordered_hand = hand[1] + hand[0] + hand[2]
        return reordered_hand
    
    #if order is correct, return hand
    return hand
    

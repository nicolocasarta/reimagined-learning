
RANK_DICT = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "t": 8,
    "j": 9,
    "q": 10,
    "k": 11,
    "a": 12
}
#reformat user hand into the proper format
def hand_reformat(hand):

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
def hand_reorder(hand):

    first_card_rank = hand[0]
    second_card_rank = hand[1]

    # if the ranks of the cards are the same, there is no need to reorder
    if first_card_rank == second_card_rank:
        return hand
    
    # if the rank of the card in the first position is lower, switch the positions
    elif RANK_DICT[first_card_rank] < RANK_DICT[second_card_rank]:
        reordered_hand = hand[1] + hand[0] + hand[2]

        return reordered_hand
    
    # otherwise the hand is in the correct order
    else:
        return hand




   
    

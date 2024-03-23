
#card ranks in order of strength
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

#reformat user hand into simple hand
def to_simple_hand(hand):

    #if card values match, suited or offsuit designation is not needed
    if hand[0] == hand[2]:
        simple_hand = hand[0] + hand[2]
        
        return simple_hand
    
    #if suits match, make simple hand be the card ranks with the "s" designation at the end, e.g. aks
    elif hand[1] == hand[3]:
        simple_hand = hand[0] + hand[2] + "s"
        
        return simple_hand
    
    #if suits do not match, place the "o" designation at the end, eg. ako
    else:
        simple_hand = hand[0] + hand[2] + "o"

        return simple_hand
    

   
#reorder simple hand: card of higher value comes before card of lower value   
def simple_hand_reorder(simple_hand):

    first_card_rank = simple_hand[0]
    second_card_rank = simple_hand[1]

    # if the ranks of the cards are the same, there is no need to reorder
    if first_card_rank == second_card_rank:
        return simple_hand
    
    # if the rank of the card in the first position is lower, switch the positions
    elif RANK_DICT[first_card_rank] < RANK_DICT[second_card_rank]:
        reordered_simple_hand = simple_hand[1] + simple_hand[0] + simple_hand[2]

        return reordered_simple_hand
    
    # otherwise the hand is in the correct order
    else:
        return simple_hand




   
    

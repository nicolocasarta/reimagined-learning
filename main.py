from source.action_check import action_check, get_correct_action
from source.cards import to_simple_hand
from source.cards import simple_hand_reorder
from source.preflop import check_poker_move



def main(): 

    while True:
        user_position = input("Enter position (UTG, UTG+1, LJ, HJ, CO, SB, BTN): ").lower().replace(" ","")
        user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ").lower().replace(" ","")
        user_action = input("Enter action (raise or fold): ").lower().replace(" ","")

        result = check_poker_move(user_position, user_hand, user_action)
        if result == 'Correct':
            break
        else:
            print(f"{result}")
    

    simple_hand = to_simple_hand(user_hand)
    simple_hand = simple_hand_reorder(simple_hand)
    correct_action = get_correct_action(user_position, simple_hand)
    action_check(correct_action, user_action)
    
    
if __name__ == "__main__":
    main()
from source.action_check import action_check, get_correct_action
from source.cards import to_simple_hand
from source.cards import simple_hand_reorder
from source.check_inputs import check_position, check_action, check_hand



def main(): 

    while True:
        user_position = input("Enter position (UTG, UTG+1, LJ, HJ, CO, SB, BTN): ").lower().replace(" ","")
       
        result = check_position(user_position)
        if result == True:
            break
        else:
            print(f"{result}")

        
    while True:
        user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ").lower().replace(" ","")

        result = check_hand(user_hand)
        if result == True:
            break
        else:
            print(f"{result}")
    
    while True:
        user_action = input("Enter action (raise, fold, bet, or call): ").lower().replace(" ","")

        result = check_action(user_action)
        if result == True:
            break
        else:
            print(f"{result}")

       
    

    simple_hand = to_simple_hand(user_hand)
    simple_hand = simple_hand_reorder(simple_hand)
    correct_action = get_correct_action(user_position, simple_hand)
    action_check(correct_action, user_action)
    
    
if __name__ == "__main__":
    main()
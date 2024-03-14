from source.responseCheck import responseCheck
from source.cards import hand_reformat
from source.cards import hand_reorder



def main(): 
    user_position = input("Enter position: ").lower()
    user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ").lower()
    user_action = input("Enter action (raise or fold): ").lower()

    simple_hand = hand_reformat(user_hand)
    simple_hand = hand_reorder(simple_hand)
    responseCheck(user_position, simple_hand, user_action)
    
    
if __name__ == "__main__":
    main()
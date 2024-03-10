from source.responseCheck import responseCheck
from source.cards import handReformat
from source.cards import handReorder



def main(): 
    user_position = input("Enter position: ")
    user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ")
    user_action = input("Enter action (raise or fold): ")

    simple_hand = handReformat(user_hand)
    simple_hand = handReorder(simple_hand)
    responseCheck(user_position, simple_hand, user_action)
    
    
if __name__ == "__main__":
    main()
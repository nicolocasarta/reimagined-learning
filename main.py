
from source.responseCheck import responseCheck
from tests.utils.util import get_data


def main(): 
    user_position = input("Enter position: ")
    user_hand = input("Enter hand (e.g., 'AsKd', '2h3c'): ")
    user_action = input("Enter action (raise or fold): ")

    responseCheck(user_position, user_hand, user_action)
    print(get_data())
    

if __name__ == "__main__":
    main()
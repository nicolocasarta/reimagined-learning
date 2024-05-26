import pytest
from source import check_inputs
from tests.utils.util import get_data

@pytest.mark.parametrize('hand, message', get_data("correct_hands_test.csv"))
def test_correct_hands(hand, message):
    assert check_inputs.check_hand(hand) == eval(message)

@pytest.mark.parametrize('hand, message', get_data("incorrect_hands_test.csv"))
def test_incorrect_hand(hand, message):
    assert check_inputs.check_hand(hand) == message

@pytest.mark.parametrize("action, message", get_data("correct_action_input_test.csv"))
def test_correct_action_input(action, message):
    assert check_inputs.check_action(action) == eval(message)

@pytest.mark.parametrize("action, message", get_data("incorrect_action_input_test.csv"))
def test_incorrect_action_input(action, message):
    assert check_inputs.check_action(action) == message

@pytest.mark.parametrize("position, message", get_data("correct_position_input_test.csv"))
def test_correct_position_input(position, message):
    assert check_inputs.check_position(position) == eval(message)

@pytest.mark.parametrize("position, message", get_data("incorrect_position_input_test.csv"))
def test_incorrect_position_input(position, message):
    assert check_inputs.check_position(position) == message
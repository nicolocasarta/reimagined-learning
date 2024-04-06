import pytest
from source import check_inputs
from tests.utils.util import get_data

@pytest.mark.parametrize('hand, message', get_data("correct_input_test.csv"))
def test_correct_inputs(hand, message):
    assert check_inputs.check_poker_move('utg', hand,'raise') == message

@pytest.mark.parametrize('hand, message', get_data("incorrect_inputs_test.csv"))
def test_incorrect_inputs(hand, message):
    assert check_inputs.check_poker_move('utg',hand,'raise') == message

import pytest
from source import cards
from tests.utils.util import get_data

@pytest.mark.parametrize("input, expected_result", get_data("to_simple_hand_test.csv"))
def test_to_simple_hand(input, expected_result):
    assert cards.to_simple_hand(input) == expected_result
     
@pytest.mark.parametrize("input, expected_result", get_data("simple_hand_reorder_test.csv"))
def test_simple_hand_reorder(input, expected_result):
    assert cards.simple_hand_reorder(input) == expected_result
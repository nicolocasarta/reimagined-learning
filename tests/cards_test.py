import pytest
from source import cards
from tests.utils.util import get_data

@pytest.mark.parametrize("input, expected_result", get_data("simple_hand_reorder_test.csv"))
def test_handReorder(input, expected_result):
    assert cards.handReorder(input) == expected_result
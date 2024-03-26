import pytest
from source import action_check
from tests.utils.util import get_data



@pytest.mark.parametrize("hand, expected_action", get_data("preflop_utg_action_test.csv"))
def test_preflop_utg_action(hand, expected_action):
    assert action_check.get_correct_action("utg", hand) == expected_action

@pytest.mark.parametrize("hand, expected_action", get_data("preflop_utg1_action_test.csv"))
def test_preflop_utg1_action(hand, expected_action):
    assert action_check.get_correct_action("utg1", hand) == expected_action

@pytest.mark.parametrize("hand, expected_action", get_data("preflop_btn_action_test.csv"))
def test_preflop_btn_action(hand, expected_action):
    assert action_check.get_correct_action("btn", hand) == expected_action
    
@pytest.mark.parametrize("hand, expected_action", get_data("preflop_lj_action_test.csv"))
def test_preflop_lj_action(hand, expected_action):
    assert action_check.get_correct_action("lj", hand) == expected_action

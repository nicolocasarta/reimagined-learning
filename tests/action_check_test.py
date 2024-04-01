import pytest
from source import action_check
from tests.utils.util import get_data



@pytest.mark.parametrize("correct_action, user_action, match", get_data("action_check_test.csv"))
def test_action_check(correct_action, user_action, match):
    assert action_check.action_check(correct_action, user_action) == eval(match)

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

@pytest.mark.parametrize("hand, expected_action", get_data("preflop_hj_action_test.csv"))
def test_preflop_hj_action(hand, expected_action):
    assert action_check.get_correct_action("hj", hand) == expected_action

@pytest.mark.parametrize("hand, expected_action", get_data("preflop_co_action_test.csv"))
def test_preflop_co_action(hand, expected_action):
    assert action_check.get_correct_action("co", hand) == expected_action

@pytest.mark.parametrize("hand, expected_action", get_data("preflop_sb_action_test.csv"))
def test_preflop_sb_action(hand, expected_action):
    assert action_check.get_correct_action("sb", hand) == expected_action
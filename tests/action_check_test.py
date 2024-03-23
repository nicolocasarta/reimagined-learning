import pytest
from source import action_check
from tests.utils.util import get_data



@pytest.mark.parametrize("input, expected_result", get_data("preflop_utg_action_test.csv"))
def test_preflop_utg_action(input, expected_result):
    assert action_check.preflop_utg_action(input) == expected_result

@pytest.mark.parametrize("input, expected_result", get_data("preflop_utg1_action_test.csv"))
def test_preflop_utg1_action(input, expected_result):
    assert action_check.preflop_utg1_action(input) == expected_result 

def test_preflop_lj_action():
    assert action_check.preflop_lj_action("aa") == "raise"
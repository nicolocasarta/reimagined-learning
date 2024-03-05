import pytest
from source import responseCheck
from tests.utils.util import get_data



@pytest.mark.parametrize("input, expected_result", get_data("utg_responses_test.txt"))
def test_utgResponse(input, expected_result):
    assert responseCheck.utgResponse(input) == expected_result



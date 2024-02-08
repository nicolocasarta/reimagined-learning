import source.responseCheck
import pytest


@pytest.mark.parametrize(
    ("input_n, expected"),
    (
        ("aa", "raise"),
        ("aks", "raise"),
        ("aqs", "raise"),
        ("ajs", "raise"),
        ("ats", "raise"),
        ("a9s", "raise"),
        ("a8s", "raise"),
        ("a7s", "raise"),
        ("a6s", "raise"),
        ("a5s", "raise"),
        ("a4s", "raise"),
        ("a3s", "raise"),
        ("ako", "raise"),
        ("aqo", "raise"),
        ("kk", "raise"),
        ("kqs", "raise"),
        ("kjs", "raise"),
        ("kts", "raise"),
        ("k9s", "raise"),
        ("kqo", "raise"),
        ("qq", "raise"),
        ("qjs", "raise"),
        ("qts", "raise"),
        ("jj", "raise"),
        ("jts", "raise"),
        ("tt", "raise"),
        ("t9s", "raise"), 
        ("99", "raise"),
        ("88", "raise"),
        ("77", "raise"),
        ("66", "raise"),
        ("65s", "raise"),
        ("55", "raise"),
        ("54s", "raise"),
    )
)



def test_utgResponse(input_n, expected):
    assert source.responseCheck.utgResponse(input_n) == expected


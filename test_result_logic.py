
from result_logic import calculate_result

def test_pass():
    assert calculate_result(75) == "PASS"

def test_fail():
    assert calculate_result(25) == "FAIL"

def test_boundary():
    assert calculate_result(40) == "PASS"

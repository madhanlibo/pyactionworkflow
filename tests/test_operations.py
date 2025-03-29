from src.math_operations import add, sub

def test_add() -> None:
    """
    Test that the add function works correctly.
    
    It takes two floats, adds them together and returns a float.
    """
    assert add(2.0, 3.0) == 5.0
    assert add(-1.0, 1.0) == 0.0

def test_sub() -> None:
    """
    Test that the sub function works correctly.
    
    It takes two floats, subtracts the second from the first and returns a float.
    """
    assert sub(5.0, 3.0) == 2.0
    assert sub(4.0, 3.0) == 1.0
    assert sub(3.0, 3.0) == 0.0
    assert sub(2.0, 3.0) == -1.0

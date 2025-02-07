from src.math_operations import add,subract

def test_add():
    #gives whether true or not
    assert add(5,3) == 8         
    assert add(3,3) == 6

def test_subract():
    assert subract(5,4) == 1
    assert subract(2,3) == -1
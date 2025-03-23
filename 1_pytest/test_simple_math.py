from simple_math import SimpleMath

def test_positive_square():
    assert SimpleMath().square(2) == 4
    assert SimpleMath().square(1) == 1
    assert SimpleMath().square(3) == 9
    assert SimpleMath().square(10) == 100

def test_negative_square():
    assert SimpleMath().square(-2) == 4
    assert SimpleMath().square(-1) == 1
    assert SimpleMath().square(-3) == 9

def test_zero_square():
    assert SimpleMath().square(0) == 0

def test_symmetry_square():
    assert SimpleMath().square(2) == SimpleMath().square(-2)

def test_positive_cube():
    assert SimpleMath().cube(2) == 8
    assert SimpleMath().cube(1) == 1
    assert SimpleMath().cube(3) == 27
    assert SimpleMath().cube(10) == 1000

def test_negative_cube():
    assert SimpleMath().cube(-2) == -8
    assert SimpleMath().cube(-1) == -1
    assert SimpleMath().cube(-3) == -27


def test_zero_cube():
    assert SimpleMath().cube(0) == 0

def test_non_symmetry_square():
    assert SimpleMath().cube(3) == -1 * SimpleMath().cube(-3)
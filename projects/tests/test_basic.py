from projects.password_strength_checker.main import entropy_bits
def test_entropy_bits_increases_with_length():
    assert entropy_bits("aaaa") < entropy_bits("aaaaaaaa")

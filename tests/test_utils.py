from src.utils import is_prime


def test_is_prime_true():
    assert is_prime(37) is True


def test_is_prime_false():
    assert is_prime(35) is False

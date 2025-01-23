from app import random_fruit
from app import random_task


def test_random_fruit():
    assert "apple" or "pear" or "orange" in random_fruit()


def test_random_task():
    assert "apple" or "pear" or "orange" in random_task()

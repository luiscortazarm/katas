import pytest
from kata3 import solution

def test_solution():
    # Example 1 should return "yes"
    assert solution(["yoda", "best", "has"]) == "yes"

    # Example 2 should return "cost"
    assert solution(["cat", "dog", "fish", "Gnat"]) == "cost"

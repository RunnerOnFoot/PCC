"""Testing the Employee Class"""

import pytest

from employee import Employee


@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    employee_0 = Employee('sam', 'white', 65_000)
    return employee_0


def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 70_000


def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 75_000

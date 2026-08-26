import pytest

from df06_calculator_samybenjelloun.math_operations import add, subtract, multiply, divide


def test_add() -> None:
    # Arrange
    input_value_1 = 10
    input_value_2 = 20
    expected_output = 30

    # Act
    actual_output = add(input_value_1, input_value_2)

    # Assert
    assert actual_output == expected_output


def test_subtract() -> None:
    # Arrange
    input_value_1 = 20
    input_value_2 = 10
    expected_output = 10

    # Act
    actual_output = subtract(input_value_1, input_value_2)

    # Assert
    assert actual_output == expected_output


def test_multiply() -> None:
    # Arrange
    input_value_1 = 5
    input_value_2 = 4
    expected_output = 20

    # Act
    actual_output = multiply(input_value_1, input_value_2)

    # Assert
    assert actual_output == expected_output


def test_divide() -> None:
    # Arrange
    input_value_1 = 20
    input_value_2 = 4
    expected_output = 5

    # Act
    actual_output = divide(input_value_1, input_value_2)

    # Assert
    assert actual_output == expected_output


def test_divide_zero_division_message() -> None:
    # Arrange
    input_value_1 = 10
    input_value_2 = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        divide(input_value_1, input_value_2)

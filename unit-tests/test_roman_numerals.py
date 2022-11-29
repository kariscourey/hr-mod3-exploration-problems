from roman_numerals import from_roman_to_arabic
from unittest import TestCase

def test_25():
    # Arrange
    input = 'XXV'

    # Act
    result = from_roman_to_arabic(input)

    # Assert
    assert result == 25


def test_52():
    # Arrange
    input = 'LII'

    # Act
    result = from_roman_to_arabic(input)

    # Assert
    assert result == 52


class TestRomanNumnerals(TestCase):
    def test_111(self):
        # Arrange
        input = 'CXI'

        # Act
        result = from_roman_to_arabic(input)

        # Assert
        self.assertEqual(result, 111)

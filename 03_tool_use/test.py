import unittest
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):
    """Test suite for the calculate_pi function."""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated correctly to 5 decimal places."""
        result = calculate_pi(5)
        expected = 3.14159  # pi to 5 decimal places
        self.assertEqual(result, expected, 
                        f"Expected {expected}, but got {result}")
    
    def test_pi_to_1_digit(self):
        """Test that pi is calculated correctly to 1 decimal place."""
        result = calculate_pi(1)
        expected = 3.1
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_to_2_digits(self):
        """Test that pi is calculated correctly to 2 decimal places."""
        result = calculate_pi(2)
        expected = 3.14
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_to_3_digits(self):
        """Test that pi is calculated correctly to 3 decimal places."""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_to_4_digits(self):
        """Test that pi is calculated correctly to 4 decimal places."""
        result = calculate_pi(4)
        expected = 3.1416
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_default_parameter(self):
        """Test that the default parameter calculates to 5 digits."""
        result = calculate_pi()
        expected = 3.14159
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_to_higher_precision(self):
        """Test that pi can be calculated to higher precision (10 digits)."""
        result = calculate_pi(10)
        expected = 3.1415926536
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_return_type(self):
        """Test that the function returns a float."""
        result = calculate_pi(5)
        self.assertIsInstance(result, float,
                            f"Expected float type, but got {type(result)}")
    
    def test_pi_greater_than_3(self):
        """Test that pi is greater than 3."""
        result = calculate_pi(5)
        self.assertGreater(result, 3,
                          f"Pi should be greater than 3, but got {result}")
    
    def test_pi_less_than_4(self):
        """Test that pi is less than 4."""
        result = calculate_pi(5)
        self.assertLess(result, 4,
                       f"Pi should be less than 4, but got {result}")


if __name__ == '__main__':
    # Run the tests with verbose output
    unittest.main(verbosity=2)

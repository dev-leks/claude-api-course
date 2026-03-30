def greeting():
    print("Hi there!")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits using the Machin formula.
    
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Approximation of pi to the specified number of digits
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to get accurate result
    # We need extra precision for intermediate calculations
    getcontext().prec = digits + 10
    
    def arctan(x, num_terms=100):
        """Calculate arctan using Taylor series expansion."""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi_over_4 = 4 * arctan(Decimal(1) / Decimal(5), 500) - arctan(Decimal(1) / Decimal(239), 500)
    pi_value = 4 * pi_over_4
    
    # Round to the specified number of digits
    return round(float(pi_value), digits)
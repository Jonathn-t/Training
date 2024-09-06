import math

def calculate_first_expression(x:float, y:float)->float:
    # 3x^2 + sqrt(x^2 + y^2) + e^ln(x)
    if x <= 0:
        raise ValueError("x must be positive for ln(x)")
    
    return 3 * (x ** 2) + math.sqrt((x ** 2) + (y ** 2)) + math.exp(math.log(x))

def calculate_second_expression(x: float, a: int, b: int, c: int) -> float:
    #log(a * x^2 + b * x + c) - sin(a * x^2 + b * x + c)) / (4 * pi * x^2 + cos(x - 2) * (a * x^2 + b * x + c)

    polynomial_value = a * (x ** 2) + b * x + c

    if polynomial_value <= 0:
        raise ValueError("The logarithm input (a * x^2 + b * x + c) must be positive.")
    
    numerator = math.log(polynomial_value) - math.sin(polynomial_value)
    denominator = 4 * math.pi * (x ** 2) + math.cos(x - 2) * polynomial_value

    if denominator == 0:
        raise ZeroDivisionError("The denominator in the second expression cannot be zero.")
    
    return numerator / denominator


if __name__ == "__main__":
    # Test the first expression
    try:
        result_1 = calculate_first_expression(1, 2)
        print(f"Result of the first expression: {result_1}")
    except ValueError as e:
        print(f"Error in first expression: {e}")

    # Test the second expression
    try:
        result_2 = calculate_second_expression(9, 1, 3, 5)
        print(f"Result of the second expression: {result_2}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error in second expression: {e}")
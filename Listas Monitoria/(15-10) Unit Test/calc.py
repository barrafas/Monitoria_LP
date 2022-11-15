def add(x, y):
    """Add Function"""

    return x + y
    
def subtract(x, y):
    """Subtract Function"""

    return x - y

def multiply(x, y):
    """Multiply Function"""

    return x * y

def divide(x, y):
    """Divide Function"""

    if y == 0:
        raise ValueError('you cannot divide by zero!')

    return x / y

def exp(x,b):
	"""Exponencial Function"""
	
	return b**x
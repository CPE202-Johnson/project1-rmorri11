
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if type(num) != int: raise ValueError
    if b > 16 or b < 2:  raise ValueError
    if num < b: return str(num)

    remainder = num % b
    if remainder == 10: remainder = 'A'
    elif remainder == 11: remainder = 'B'
    elif remainder == 12: remainder = 'C'
    elif remainder == 13: remainder = 'D'
    elif remainder == 14: remainder = 'E'
    elif remainder == 15: remainder = 'F'
    else: remainder = str(remainder)

    quotient = num // b
    return convert(quotient, b) + remainder


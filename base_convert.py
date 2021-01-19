
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if type(num) != int: raise ValueError
    if b > 16 or b < 2:  raise ValueError
    if num < b: 
        if num == 10: numstr = 'A'    #convert to hex if necessary
        elif num == 11: numstr = 'B'
        elif num == 12: numstr = 'C'
        elif num == 13: numstr = 'D'
        elif num == 14: numstr = 'E'
        elif num == 15: numstr = 'F'
        else: numstr = str(num)
        return numstr

    remainder = num % b
    if remainder == 10: remainder = 'A'    #convert to hex if necessary
    elif remainder == 11: remainder = 'B'
    elif remainder == 12: remainder = 'C'
    elif remainder == 13: remainder = 'D'
    elif remainder == 14: remainder = 'E'
    elif remainder == 15: remainder = 'F'
    else: remainder = str(remainder)

    quotient = num // b
    return convert(quotient, b) + remainder


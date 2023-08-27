import re

def validate_input(P, allow_float=True):
    if allow_float:
        pattern = r"^\d*\.?\d*$"
    else:
        pattern = r"^[0-9]*$"
    return re.match(pattern, P) is not None

def validate_time_input(P, check_hours=True):
    if check_hours:
        pattern = r"^(?:[01]?\d|2[0-3])?$"
    else:
        pattern = r"^(?:[0-5]?\d)?$"
    return re.match(pattern, P) is not None

def calculate_total(operation, *numbers, tax=0, discount=0):
    """

    calculates total amount
    Parameters:
        operation : int
        numbers : tuple
    Returns:
        total amount :  float
    """

    if operation == "sum":
        res = sum(numbers)
    res = res - res * discount / 100
    res = res + res * tax / 100
    return res


def another():
    pass

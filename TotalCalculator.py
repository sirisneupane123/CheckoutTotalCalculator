def calculate_total(state_code, items):
    """
    Calculate the total charge for a customer at checkout, including sales tax.

    Args:
        state_code (str): The two-character state abbreviation ('MT', 'ID', 'WA').
        items (list of dict): A list where each dict contains 'type' (str) and 'price' (float).

    Returns:
        float: The total charge, including any applicable sales tax, rounded to two decimal places.

    Raises:
        ValueError: If the state_code is not supported or item type is incorrect.
    """
    # Validate state code.
    if state_code not in ('MT', 'ID', 'WA'):
        raise ValueError("Unsupported state code. Choose from 'MT', 'ID', 'WA'.")

    total = 0
    for item in items:
        # Validate item type.
        if item['type'] not in ('Wic Eligible food', 'Software', 'everything else'):
            raise ValueError("Unsupported item type.")

        # Accumulate total after calculating individual item totals.
        total += _calculate_item_total(state_code, item)

    # Return the total rounded to two decimal places.
    return round(total, 2)

def _calculate_item_total(state_code, item):
    """
    Calculate the total price of a single item, considering the state tax exemptions.

    Args:
        state_code (str): The state code.
        item (dict): Contains 'type' (str) and 'price' (float).

    Returns:
        float: The total price of the item after tax.
    """
    # Calculate and return item price including tax rate.
    tax_rate = _get_tax_rate(state_code, item['type'])
    return item['price'] * (1 + tax_rate)

def _get_tax_rate(state_code, item_type):
    """
    Determine the applicable sales tax rate based on the state and item type.

    Args:
        state_code (str): The state code.
        item_type (str): The type of the item.

    Returns:
        float: The applicable sales tax rate.
    """
    # Return tax rates based on state and item type.
    if item_type == 'Wic Eligible food':
        return 0
    if state_code == 'MT':
        return 0
    elif state_code == 'ID':
        return 0.06 if item_type != 'Software' else 0
    elif state_code == 'WA':
        return 0.0938

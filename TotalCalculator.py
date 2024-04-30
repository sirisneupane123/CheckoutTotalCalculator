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


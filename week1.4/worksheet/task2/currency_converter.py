
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Martha Cawood
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here
    
    if amount >= 0:
        for key, value in conversion_rate.items():
            if key == from_currency:
                specific_conversion_rates = value

                for key, value in specific_conversion_rates.items():
                    if key == to_currency:
                        specific_to_currency = value

        conversion = amount * specific_to_currency
        

        return conversion
    
    else:
        return 0.0

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
print(currency_converter(-100, "GBP", "PHP"))
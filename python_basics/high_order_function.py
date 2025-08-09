

def rateList_process(rates, function):
    return [ function(obj) for obj in rates ]


ars_rates = [1000, -200, 500, -150, 1200, 1700]

def usd_convertion(amount):
    return amount / 1350  # Example: rate of 1USD = 1350 ARS

def absolute_value(amount):
    return abs(amount)


usd_rates = rateList_process(ars_rates, usd_convertion)
absolute_rate_values = rateList_process(ars_rates, absolute_value)


print("Rates in USD: {}".format(usd_rates))
print("Absolute rate values: {}".format(absolute_rate_values))



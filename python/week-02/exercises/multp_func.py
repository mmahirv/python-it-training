def make_multiplier(multiplier):
    return lambda y: multiplier * y

double = make_multiplier(2)


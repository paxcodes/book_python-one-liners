import numpy as np


def get_highest_after_tax_income(salaries, taxation):
    afterTaxSalaries = salaries * (1.0 - taxation)
    return np.max(afterTaxSalaries)
    # one-liner would be np.max(salaries * (1.0 - taxation))

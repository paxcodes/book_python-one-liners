import numpy as np


def get_person_with_highest_net_income(folks, salaries, taxation):
    netIncomes = salaries * (1.0 - taxation)
    maxNetIncome = np.max(netIncomes)
    rowIndex = np.nonzero(netIncomes == maxNetIncome)[0][0]
    return folks[rowIndex]
    # netIncomes = salaries * (1.0 - taxation)
    # folks[np.nonzero(netIncomes == np.max(netIncomes))[0][0]]


def get_highest_net_income(salaries, taxation):
    afterTaxSalaries = salaries * (1.0 - taxation)
    return np.max(afterTaxSalaries)
    # one-liner would be np.max(salaries * (1.0 - taxation))

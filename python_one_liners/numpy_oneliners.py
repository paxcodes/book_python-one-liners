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


def get_outlier_days(data):
    """
    Args:
        data: 2-dimensional array where row = day and col =
            (users, bounce, duration).

    Returns:
    """
    mean, stddev = np.mean(data, axis=0), np.std(data, axis=0)
    # mean and stddev would be a flat array [x, y, z]
    outliers = (
        (np.abs(data[:, 0] - mean[0]) > stddev[0])
        * (np.abs(data[:, 1] - mean[1]) > stddev[1])
        * (np.abs(data[:, 2] - mean[2]) > stddev[2])
    )
    return data[outliers]

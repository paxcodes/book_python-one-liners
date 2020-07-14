import numpy as np

from python_one_liners import numpy_oneliners


def test_highest_after_tax_salary_should_be_81():
    alice = [99, 101, 103]
    bob = [110, 108, 105]
    tim = [90, 88, 85]
    givenSalaries = np.array([alice, bob, tim])
    givenTaxation = np.array(
        [[0.2, 0.25, 0.22], [0.4, 0.5, 0.5], [0.1, 0.2, 0.1]]
    )
    actualHighestAfterTaxSalary = numpy_oneliners.get_highest_after_tax_income(
        givenSalaries, givenTaxation
    )
    assert actualHighestAfterTaxSalary == 81

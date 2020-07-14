import numpy as np

from python_one_liners import numpy_oneliners as npol


def test_person_with_highest_after_tax_salary_should_be_Tim():
    givenFolks = ["Alice", "Bob", "Tim"]
    alice = [99, 101, 103]
    bob = [110, 108, 105]
    tim = [90, 88, 85]
    givenSalaries = np.array([alice, bob, tim])
    givenTaxation = np.array(
        [[0.2, 0.25, 0.22], [0.4, 0.5, 0.5], [0.1, 0.2, 0.1]]
    )
    actual = npol.get_person_with_highest_net_income(
        givenFolks, givenSalaries, givenTaxation
    )
    assert actual == "Tim"


def test_highest_after_tax_salary_should_be_81():
    alice = [99, 101, 103]
    bob = [110, 108, 105]
    tim = [90, 88, 85]
    givenSalaries = np.array([alice, bob, tim])
    givenTaxation = np.array(
        [[0.2, 0.25, 0.22], [0.4, 0.5, 0.5], [0.1, 0.2, 0.1]]
    )
    actualHighestNetIncome = npol.get_highest_net_income(
        givenSalaries, givenTaxation
    )
    assert actualHighestNetIncome == 81


def test_getting_outlier_days():
    data = np.array(
        [
            [815, 70, 115],
            [767, 80, 50],
            [912, 74, 77],
            [554, 88, 70],
            [1008, 65, 128],
        ]
    )
    actual = npol.get_outlier_days(data)
    expected = np.array([[1008, 65, 128]])
    assert np.array_equal(actual, expected)

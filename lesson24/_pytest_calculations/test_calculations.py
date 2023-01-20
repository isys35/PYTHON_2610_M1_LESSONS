import pytest

from lesson23._unittest.project_1.code.my_calculations import Calculations


@pytest.fixture
def calculation_fixture():
    return Calculations(8, 2)


@pytest.fixture
def calculated_ten(calculation_fixture):
    return calculation_fixture.get_sum()


@pytest.mark.parametrize("num1,num2,result", [
    (8, 2, 10),
    (8, 5, 13),
    (4, 2, 5),
    (7, 3, 10),
    (2, 4, 6),
    (11, 22, 33),
    (0, 0, 0),
])
def test_sum(num1, num2, result):
    assert Calculations(num1, num2).get_sum() == result, 'Сумма посчитана неправильно.'


def test_diff(calculation_fixture):
    assert calculation_fixture.get_difference() == 6, 'Разность посчитана неправильно.'


@pytest.mark.faster
def test_product(calculation_fixture):
    assert calculation_fixture.get_product() == 16, 'Умножение посчитано неправильно.'


@pytest.mark.faster
def test_quotient(calculation_fixture):
    assert calculation_fixture.get_quotient() == 4, 'Деление посчитано неправильно.'


def test_ten(calculated_ten):
    assert calculated_ten == 10

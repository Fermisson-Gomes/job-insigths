from src.pre_built.sorting import sort_by

mock = [
    {"min_salary": 0, "max_salary": 20},
    {"min_salary": 100, "max_salary": 200},
]

order_min_salary = [
    {"min_salary": 0, "max_salary": 20},
    {"min_salary": 100, "max_salary": 200},
]

order_max_salary = [
    {"min_salary": 100, "max_salary": 200},
    {"min_salary": 0, "max_salary": 20},
]


def test_sort_by_criteria():
    sort_by(mock, "max_salary")
    assert mock == order_max_salary
    sort_by(mock, "min_salary")
    assert mock == order_min_salary

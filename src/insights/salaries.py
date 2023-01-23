from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = [
        int(job["max_salary"]) for job in data if job["max_salary"].isdigit()
        ]
    return int(max(max_salary))
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = [
        int(job["min_salary"]) for job in data if job["min_salary"].isdigit()
        ]
    return int(min(min_salary))
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary missing")
    if not (
        isinstance(job["min_salary"], (int, float)) and isinstance(job["min_salary"], (int, float))
        ):
        raise ValueError("min_salary or max_salary is not a number")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    return job["min_salary"] <= int(salary) <= job["max_salary"]
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

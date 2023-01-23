import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_types = [job["job_type"] for job in data]
    return list(set(job_types))
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
    raise NotImplementedError

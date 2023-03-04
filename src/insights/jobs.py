import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    # função criada com base na presente no course presente no dia 2 da sessão 1 do modulo de CS
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    # pega todos o tipo de trabalho presente na data e o coloca na variavel job types
    job_types = [job["job_type"] for job in data]
    # retorna uma lista de conjuntos com os tipos de trabalho presentes na variavel job types
    return list(set(job_types))
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    # retorna todos os trabalhos que possuem o tipo de trabalho passado como parametro do dicionario jobs
    return [job for job in jobs if job["job_type"] == job_type]
    raise NotImplementedError

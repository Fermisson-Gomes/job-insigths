from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    # busca em todos os trabalhos os salarios maximos que forem numeros e os converte em inteiros, em seguida os coloca na variavel max_salary
    max_salary = [
        int(job["max_salary"]) for job in data if job["max_salary"].isdigit()
        ]
    # retorna o maior salario dentro da variavel max_salary já o convertendo a um numero inteiro
    return int(max(max_salary))
    raise NotImplementedError

# essa função foi feita com base na anterior apenas invertendo sua logica de busca de maior para menor salario
def get_min_salary(path: str) -> int:
    data = read(path)
    # busca em todos os trabalhos os salarios minimos que forem numeros e os converte em inteiros, em seguida os coloca na variavel min_salary
    min_salary = [
        int(job["min_salary"]) for job in data if job["min_salary"].isdigit()
        ]
    # retorna o menor salario dentro da variavel min_salary já o convertendo a um numero inteiro
    return int(min(min_salary))
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try: 
        # pega os salarios maximo e minimo do parametro job e os converte em inteiros
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        # converte o parametro salary e o converte em inteiro
        salary = int(salary)
    except (ValueError, KeyError, TypeError):
        raise ValueError
    # valida se o salario minimo e maior que o salario maximo e se for true levanta um erro
    if min_salary > max_salary:
        raise ValueError
    # se a validação a cima retornar false, retornamos o resultado da validação a baixo
    # valida se o parametro salary esta entre o salario minimo e o salario maximo
    return min_salary <= salary <= max_salary
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    # percorre o parametro jobs e obseva cada job dele
    for job in jobs:
        try:
            # executa a função anterior usando cada trabalho de jobs e o parametro salary e coloca seu retono na variavel matches_salary
            matches_salary = matches_salary_range(job, salary)

            # se o retorno da variavel matches_salary for true o job é adicionado a lista de trabalhos filtrados
            if matches_salary is True:
                filtered_jobs.append(job)
        except ValueError:
            print('Error finding jobs')
    # retorna a lista de trabalhos filtrados
    return filtered_jobs
    raise NotImplementedError

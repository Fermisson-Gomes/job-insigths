from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    # realiza a leitura do arquivo por meio da função read importada do arquivo jobs.py
    data = read(path)
    # pega tudo que esteja na "chave" industry dentro de cada job presente em data e coloca na variavel industries
    industries = [job["industry"] for job in data]
    # pega todas as categorias de industria localizadas dentro de industries e redefine o conteudo da variavel industries
    industries = [x for x in industries if x]
    # retorna uma lista de conjuntos com os valores que estão dentro da varivel industries.
    return list(set(industries))
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    # retorna todos os trabalhos que possuem o tipo de industria passado como parametro buscando do dicionario jobs
    return [job for job in jobs if job["industry"] == industry]
    raise NotImplementedError


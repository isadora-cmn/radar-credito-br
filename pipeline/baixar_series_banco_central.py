import pandas as pd
import requests

URL_BASE_API_BANCO_CENTRAL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados"


def baixar_serie_banco_central(codigo_serie: int) -> pd.DataFrame:
    """Baixa uma série do Banco Central e devolve uma tabela com data, valor e codigo_serie."""
    url_da_serie = URL_BASE_API_BANCO_CENTRAL.format(codigo_serie=codigo_serie)

    resposta = requests.get(url_da_serie, params={"formato": "json"}, timeout=30)
    resposta.raise_for_status()

    tabela_da_serie = pd.DataFrame(resposta.json())
    tabela_da_serie["data"] = pd.to_datetime(tabela_da_serie["data"], format="%d/%m/%Y")
    tabela_da_serie["valor"] = pd.to_numeric(tabela_da_serie["valor"])
    tabela_da_serie["codigo_serie"] = codigo_serie
    return tabela_da_serie
# Códigos das séries do Sistema Gerenciador de Séries Temporais (SGS) do Banco Central.
# Os itens marcados com "confirmar" precisam ter o nome conferido no site do SGS.
# A série 432 (meta da Selic) ficou de fora porque é diária e a API exige um período de datas.
# Usamos a série 4390 (Selic acumulada no mês), que é mensal como as demais.

CODIGOS_SERIES_BANCO_CENTRAL = {
    "selic_acumulada_no_mes": 4390,
    "ipca_variacao_mensal": 433,
    "inadimplencia_total": 21082,
    "inadimplencia_pessoa_juridica": 21083,
    "inadimplencia_pessoa_fisica": 21084,  # confirmar
    "inadimplencia_recursos_livres": 21085,
    "concessoes_credito_total": 20631,  # confirmar
    "juro_medio_credito_total": 20714,  # confirmar
    "taxa_desocupacao": 24369,  # confirmar
}
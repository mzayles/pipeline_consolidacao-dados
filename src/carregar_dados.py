# importando bibliotecas

import pandas as pd
import os
import unidecode

# criando função para consolidar planilhas

def carregar_arquivos(pasta: str) -> pd.DataFrame:
    if not os.path.exists(pasta):
        raise FileNotFoundError(f"Pasta '{pasta}' não encontrada.")

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.csv') or f.endswith('.xlsx')]
    if not arquivos:
        raise ValueError("Nenhum arquivo .csv ou .xlsx encontrado na pasta.")

    total = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)

        try:
            if arquivo.endswith('.csv'):
                df = pd.read_csv(caminho)
            else:
                df = pd.read_excel(caminho)

            df.columns = [unidecode.unidecode(col).strip().lower().replace(' ', '_') for col in df.columns]

            print(f"Arquivo carregado: {arquivo} | Colunas: {list(df.columns)}")
            total.append(df)
        except Exception as erro:
            print(f"Erro ao carregar '{arquivo}': {erro}")

    if not total:
        raise ValueError("Nenhum arquivo pôde ser carregado com sucesso.")

    return pd.concat(total, ignore_index=True)
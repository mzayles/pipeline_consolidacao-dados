## Aquisição e Padronização de Dados

Este projeto contém uma função reutilizável para carregar, padronizar e unificar múltiplos arquivos `.csv` e `.xlsx` a partir de uma pasta local. É a etapa inicial de um pipeline de análise de dados.

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)

### Funcionalidades

- Leitura de múltiplos arquivos `.csv` e `.xlsx`
- Padronização de nomes de colunas (sem acentos, espaços e com letras minúsculas)
- Concatenação dos dados em um único DataFrame
- Exportação do DataFrame final para `.csv`

### Como usar
1. Coloque seus arquivos na pasta `dados/`
2. Execute o script principal:

```bash
python main.py

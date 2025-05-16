from src.carregar_dados import carregar_arquivos

# chamando função
df = carregar_arquivos('dados/')

# testando DataFrame
df.sample(5)

# exportando arquivo consolidado em formato CSV
df.to_csv('base_completa.csv', index=False)
files.download('base_completa.csv')

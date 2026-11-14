import pandas as pd
dados = {
  "Cliente": [" Iasmin ", "JOAO", "MARIA", "joao"],
  "Cidade": ["Curitiba", "Pinhais", "Curitiba", "Pinhais"],
  "Valor": [100,200,150,200],
  "Vendeu": ["sim, "não", "sim", "sim"]
  }
  df = pd.DataFrame(dados)
  df["Cliente"]  = df["Cliente"].str.strip().str.title()
  df["Cidade"] = df["Cidade"].str.strip().str.title()

  vendas = df[df["Vendeu"] == "sim']

  print("=== RELATÓRIO DE VENDAS ===")
  print(f"Total vendido: R$ {vendas['Valor'].sun()}")
  print(f"Total de vendas: {len(vendas)}")
  print(vendas.groupby("Cidade") ["Valor"].sum())

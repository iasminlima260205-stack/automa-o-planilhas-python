import pandas as pd
import matplotlib.pyplot as plt

#1.LER A PLANILHA
df = pd.read_csv('vendas.csv')

# Deixa o nome bonito
df["Cliente"] = df["Cliente"].Str.strip().str.title()
df["Cidade"] = df["Cidade"].str.strip().str.title()

# So quem vendeu 
vendas = df[df["Vendeu"] == "sim"]

print("=== RELATORIO DE VENDAS ==="]
print(f"Total vendido:R${vendas['Valor'].sum()})
print(vendas.groupby("Cidade")["Valor"].sum())

# 2. GRAFICO
plt.figure(figsize=(8, 5))
plt.bar(vendas["Cidade"], vendas["Valor"],color='skyblue')
plt.title('Vendas por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Valor (R$)')
plt.tight_layout()
plt.savefig('grafico_vendas.png')
plt.show()

# 3. EXPORTAR EM EXCEL
resumo = pd.DataFrame({
  'Metrica':['Total Vendido','Total de Vendas'],
  'Valor':[vendas['Valor'].sum(),len(vendas)]
})

with pd.ExcelWriter('relatorio_vendas.xlsx') as writer:
  vendas.to_excel(writer,sheet_name='Vendas', index=False)
  resumo.to_excel(writer,sheet_name='Resumo', index=False)

print("Pronto! relatorio_vendas.xlsx'criado!")

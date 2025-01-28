import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")
print(dir(df))

#df.to_csv("archivos_problemas_graficos\\pedos-nuevos.csv",index=False)

id_pedo_max = df['pedos'].idxmax()
maximo_pedo = df['pedos'].max()

#creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)


#creando un punto en el momento de mas pedos
plt.plot(id_pedo_max,maximo_pedo,"o")

#mostrando el grafico
plt.show()

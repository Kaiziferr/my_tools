import seaborn as sns
import matplotlib.pyplot as plt


def porcentaje_nulos_x_caracteristica(data, **kwargs):
  """Calcular el porcentaje de valores nulos por caracteristicas"""
  data.isnull().melt().pipe(
        lambda df: (
            sns.displot(
                data=df,
                y='variable',
                hue='value',
                multiple='fill',
                aspect=2
            ).set(**kwargs)
        )
    )
#porcentaje_nulos_x_caracteristica(data, title="Porcentaje de valores nulos", xlabel='Porcentaje de nulos', ylabel='Caracteristicas')


def null_features_per_record(data, figsize=(9,8), **kwargs):
  """Identifica el número de caracteristicas nulas por registro"""
  plt.figure(figsize=figsize)
  (
      data
      .isnull()
      .transpose()
      .pipe(
          lambda df: (
              sns.heatmap(
                  data = df
                  
              ).set(**kwargs)
          )
      )
  )
# null_features_per_record(data,title="Caracteristicas nulas por registro", xlabel='Index', ylabel='Caracteristicas')
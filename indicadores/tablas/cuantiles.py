# Tablas
def quantile_table(data, quantils=[0.25, 0.5, 0.75]):
  """Genera una tabla con los cuantiles y su RIC"""
  print("Cauntiles and his iqr")
  print("**********************")
  data_quantil=(
      data.quantile(q=quantils)
      .T
      .rename_axis('feature')
      .reset_index()
      .assign(
          iqr = lambda df: df[0.75]-df[0.25]
      )
  )
  return data_quantil